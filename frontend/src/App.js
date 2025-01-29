import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import Login from "./login/login";
import Signup from "./signup/signup";
import Home from "./home/home";
import EmployeeForm  from "./form/employeedetails";
import ShiftSwap from './shiftswap/shiftswap';


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/home" element={<Home />} />
        <Route path="/employeeform" element={<EmployeeForm />} />
		  <Route path = "/shiftswap" element = {<ShiftSwap/>}/>
   
      </Routes>
    </Router>
  );
}

export default App;
