import React from "react";
import {
  Route,
  Routes,
} from "react-router-dom";
import ProtectedRoute from "./routes/ProtectedRoute";
import Login from "./pages/Login";
import Registration from "./pages/Registration";
import Home from './pages/Home';


function App() {
  return (
    <Routes>
      <Route path='/' element={
        <ProtectedRoute>
          <Home />
        </ProtectedRoute>
      } />
      <Route path='/login/' element={<Login />} />
      <Route path='/register/' element={<Registration />} />
    </Routes>
  );
}

export default App;
