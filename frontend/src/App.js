import {
	BrowserRouter as Router,
	Routes,
	Route,
	useLocation,
	Navigate,
  } from "react-router-dom";
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
  import ProtectedRoute from "./protectedroute"; // Import ProtectedRoute
  
  const { Content } = Layout;
  
  const AppLayout = () => {
	const location = useLocation();
  
	// Hide Navbar on Login and Signup pages
	const hideNavbar =
	  location.pathname === "/login" || location.pathname === "/signup";
  
	return (
	  <Layout
		style={{
		  minHeight: "100vh",
		  backgroundColor: "#E0F7FA",
		}}
	  >
		{!hideNavbar && <Navbar />}
		<Content
		  style={{
			padding: "20px",
			marginTop: hideNavbar ? 0 : 64,
		  }}
		>
		  <Routes>
			{/* Routes that don't require protection */}
			<Route path="/login" element={<Login />} />
			<Route path="/signup" element={<Signup />} />
  
			{/* Default route to Login page */}
			<Route path="/" element={<Navigate to="/login" />} />
  
			{/* Protected Routes wrapped with ProtectedRoute */}
			<Route
			  path="/home"
			  element={
				<ProtectedRoute>
				  <Home />
				</ProtectedRoute>
			  }
			/>
			<Route
			  path="/employeeform"
			  element={
				<ProtectedRoute>
				  <EmployeeForm />
				</ProtectedRoute>
			  }
			/>
			<Route
			  path="/shiftswap"
			  element={
				<ProtectedRoute>
				  <ShiftSwap />
				</ProtectedRoute>
			  }
			/>
			<Route
			  path="/addemployeerecords"
			  element={
				<ProtectedRoute>
				  <AddEmployeeRecord />
				</ProtectedRoute>
			  }
			/>
			<Route
			  path="/shiftdetails"
			  element={
				<ProtectedRoute>
				  <ShiftConfiguration />
				</ProtectedRoute>
			  }
			/>
			<Route
			  path="/viewemployeedetails"
			  element={
				<ProtectedRoute>
				  <ViewEmployee />
				</ProtectedRoute>
			  }
			/>
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
  