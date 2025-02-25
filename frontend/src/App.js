import React from "react";
import { BrowserRouter as Router, Routes, Route, useLocation } from "react-router-dom";
import { Layout } from "antd";
import Login from "./login/login";
import Signup from "./signup/signup";
import Home from "./home/home";
import EmployeeForm from "./form/configemployee";
import ShiftSwap from "./shiftswap/shiftswap";
import Navbar from "./navbar/navbar";
import AddEmployeeRecord from "./add employee/addemplyee";
import ShiftConfiguration from "./form/configshifts";
import ViewEmployee from "./view/viewemployee";

const { Content } = Layout;

const AppLayout = () => {
  const location = useLocation();
  
  // Hide Navbar on Login and Signup pages
  const hideNavbar = location.pathname === "/login" || location.pathname === "/signup";

  return (
    <Layout style={{ minHeight: "100vh", backgroundColor: "#E0F7FA" }}> {/* Light blue background */}
      {!hideNavbar && <Navbar />}
      <Content style={{ padding: "20px", marginTop: hideNavbar ? 0 : 64 }}> 
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/home" element={<Home />} />
          <Route path="/employeeform" element={<EmployeeForm />} />
          <Route path="/shiftswap" element={<ShiftSwap />} />
          <Route path="/addemployeerecords" element={<AddEmployeeRecord />} />
          <Route path="/shiftdetails" element={<ShiftConfiguration />} />
          <Route path="/viewemployeedetails" element={<ViewEmployee />} />
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
