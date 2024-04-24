import datetime
from pydantic import BaseModel


class ID:
    id: int


class PostScheme(BaseModel, ID):
    name: str
    is_driver: bool

    class Config:
        from_attributes = True


class PostSchemePatch(BaseModel):
    name: str | None = None
    is_driver: bool | None = None


class HumanScheme(BaseModel):
    first_name: str
    second_name: str
    patronymic: str | None = None


class WorkerSchemeRead(HumanScheme):
    post_id: int


class WorkerSchemePatch(BaseModel):
    first_name: str | None = None
    second_name: str | None = None
    patronymic: str | None = None
    post_id: int | None = None
    is_ill: bool | None = None


class WorkerScheme(HumanScheme, ID):
    post: PostScheme
    is_ill: bool

    class Config:
        from_attributes = True


class CarSchemeRead(BaseModel):
    model: str


class CarScheme(CarSchemeRead, ID):
    class Config:
        from_attributes = True


class CarFullScheme(CarSchemeRead, ID):
    used: bool

    class Config:
        from_attributes = True


class BrigadeSchemeRead(BaseModel):
    workers: list[int]
    car_id: int


class StatusSchemeRead(BaseModel):
    name: str


class StatusScheme(StatusSchemeRead, ID):
    class Config:
        from_attributes = True


class StatusSchemeFull(StatusSchemeRead, ID):
    used: bool

    class Config:
        from_attributes = True


class PatientSchemeRead(HumanScheme):
    address: str
    descriptions: str


class PatientScheme(PatientSchemeRead, ID):
    class Config:
        from_attributes = True


class CallSchemeRead(BaseModel):
    patient: PatientSchemeRead
    status: StatusScheme


class CallScheme(BaseModel, ID):
    status: StatusScheme
    patient: PatientScheme

    created_at: datetime.datetime
    updated_at: datetime.datetime
    end_at: datetime.datetime | None = None

    class Config:
        from_attributes = True


class CallPatchScheme(BaseModel):
    descriptions: str | None = None
    status_id: int | None = None


class BrigadeScheme(BaseModel):
    id: int

    car: CarScheme
    call: CallScheme | None = None
    start_time: datetime.datetime
    end_time: datetime.datetime | None = None

    workers: list[WorkerScheme]

    class Config:
        from_attributes = True
