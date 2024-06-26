import ReactDOM from 'react-dom/client';
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import Error from './components/Error';
import Navbar from './components/Navbar';
import Personal from './components/Personal/Personal';
import Main from './components/Main';
import Post from './components/Post/Post';
import Cars from './components/Cars/Cars';
import './css/style.css';
import StatusPage from './components/Status/Status';
import CallPage from './components/Call/Call';
import BrigadePage from './components/Brigade/Brigade';


const router = [
  {
    path: '/',
    element: <></>,
    errorElement: <Error/>,
    children: [
      {
        path: '',
        element: <Main/>
      },
      {
        path: 'personal',
        element: <Personal/>
      },
      {
        path: 'posts',
        element: <Post/>
      },
      {
        path: 'cars',
        element: <Cars/>
      },
      {
        path: 'status',
        element: <StatusPage/>
      },
      {
        path: 'call',
        element: <CallPage/>
      },
      {
        path: 'brigade',
        element: <BrigadePage/>
      },
    ]
  }
];

router[0].element = <Navbar data={router[0].children.slice(1).map((data) => `/${data.path}`)}/>;

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);

root.render(
  <RouterProvider router={createBrowserRouter(router)}/>
);
