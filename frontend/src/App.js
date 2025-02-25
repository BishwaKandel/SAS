import React from "react";
import { BrowserRouter as Router, Routes, Route, useLocation } from "react-router-dom";
import { Layout } from "antd";
import Login from "./login/login";
import Signup from "./signup/signup";
import Home from "./home/home";
import EmployeeForm from "./form/employeedetails";
import ShiftSwap from "./shiftswap/shiftswap";
import Navbar from "./navbar/navbar";
import AddEmployeeRecord from "./add employee/addemplyee";

const { Content } = Layout;

const AppLayout = () => {
  const location = useLocation();
  
  // Hide Navbar on Login and Signup pages
  const hideNavbar = location.pathname === "/login" || location.pathname === "/signup";

  return (
    <Layout style={{ minHeight: "100vh" }}>
      {!hideNavbar && <Navbar />}
      <Content style={{ padding: "20px", marginTop: hideNavbar ? 0 : 64 }}> 
        <Routes>
          {/* <Route path="/" element={<Login />} /> */}
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/home" element={<Home />} />
          <Route path="/employeeform" element={<EmployeeForm />} />
          <Route path="/shiftswap" element={<ShiftSwap />} />
          <Route path="/addemployeerecords" element={<AddEmployeeRecord />} />


        </Routes>
      </Content>
    </Layout>
  );
};

function App() {
  return (
    <Router>
      <AppLayout />
    </Router>
  );
}

export default App;
