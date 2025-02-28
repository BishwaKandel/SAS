import { Navigate } from "react-router-dom";

const ProtectedRoute = ({ children }) => {
  const token = localStorage.getItem("authToken");

  // If no token, redirect to login page
  return token ? children : <Navigate to="/login" replace />;
};

export default ProtectedRoute;
