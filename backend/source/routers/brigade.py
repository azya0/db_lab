from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload

from db.engine import get_async_session
from db.models import Brigade, Brigade_xref_Worker, Worker
from routers.schemas import BrigadeScheme, BrigadeSchemeRead, WorkerScheme


router = APIRouter(
    prefix="/brigade",
    tags=["brigade"],
)


@router.post('', response_model=BrigadeScheme)
async def post_brigade(data: BrigadeSchemeRead, session: AsyncSession = Depends(get_async_session)):
    worker_shemas: list[WorkerScheme] = []
    has_driver = False
    
    for id in data.workers:
        worker = await session.get(Worker, id, options=(selectinload(Worker.post), ))

        if worker is None:
            raise HTTPException(404, 'wrong worker id')
        
        already = await session.scalar(select(Brigade_xref_Worker).where(
            (Brigade_xref_Worker.worker_id == id) & (Brigade_xref_Worker.active == True)))

        if already is not None:
            raise HTTPException(400, 'worker already used')
        
        if not has_driver and worker.post.is_driver:
            has_driver = True

        worker_shemas.append(WorkerScheme.model_validate(worker))
    
    if not has_driver:
        raise HTTPException(400, 'brigade has no drivers')
    
    result = Brigade()
    
    session.add(result)
    await session.commit()
    await session.refresh(result)

    for id in data.workers:
        session.add(Brigade_xref_Worker(brigade_id=result.id, worker_id=id))
    
    await session.commit()
    
    print(worker_shemas)

    return BrigadeScheme(
        id=result.id,
        start_time=result.start_time,
        end_time=result.end_time,
        workers=worker_shemas
    )


@router.get('/by_id/{id}', response_model=BrigadeScheme)
async def get_brigade_by_id(id: int, session: AsyncSession = Depends(get_async_session)):
    data = await session.get(Brigade, id, options=(selectinload(Brigade.workers), selectinload(Brigade.workers, Worker.post)))

    if data is None:
        raise HTTPException(404, 'no brigade found')
    
    return BrigadeScheme.model_validate(data)


@router.get('/all', response_model=list[BrigadeScheme])
async def get_brigades(session: AsyncSession = Depends(get_async_session)):
    request = select(Brigade).options(selectinload(Brigade.workers), selectinload(Brigade.workers, Worker.post))
    result = (await session.scalars(request)).all()

    print(result)

    return [BrigadeScheme.model_validate(data) for data in result]


@router.delete('/by_id/{id}')
async def delete_brigade_by_id(id: int, session: AsyncSession = Depends(get_async_session)):
    brigade = await session.get(Brigade, id)

    if brigade is None:
        raise HTTPException(404, 'no brigade found')
    
    xrefs = (await session.scalars(select(Brigade_xref_Worker).where(Brigade_xref_Worker.brigade_id == brigade.id))).all()

    for xref in xrefs:
        await session.delete(xref)
    
    await session.delete(brigade)