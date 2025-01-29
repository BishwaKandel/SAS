import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios"; // Import Axios for API calls
import "./login.css";

const Login = () => {
    const [managerId, setManagerId] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState(""); // Error state
    const navigate = useNavigate();

    const handleLogin = async (e) => {
        e.preventDefault();
        setError(""); // Clear previous errors

        try {
            const response = await axios.post("http://127.0.0.1:8000/login/", {
                ManagerID: managerId,
                password: password,
            });

            if (response.data.status) {
                console.log("Login successful:", response.data);
                navigate("/EmployeeForm"); // Redirect on success
            } else {
                setError("Invalid Manager ID or Password");
            }
        } catch (err) {
            if (err.response && err.response.data) {
                // Customize the error message based on backend response
                setError(err.response.data.message || "Something went wrong. Please try again.");
            } else {
                setError("Network Error: Unable to reach the server.");
            }
        }
    };

    return (
        <div className="login-container">
            <div className="login-box">
                <h2>Login</h2>
                <form onSubmit={handleLogin}>
                    <input
                        type="text"
                        placeholder="Manager ID (4 digits)"
                        value={managerId}
                        onChange={(e) => setManagerId(e.target.value)}
                        required
                        maxLength="4"
                        minLength="4"
                        pattern="\d{4}"
                        className="login-input"
                    />
                    <input
                        type="password"
                        placeholder="Password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                        className="login-input"
                    />
                    <button type="submit" className="login-button">Login</button>
                </form>
                {error && <p className="error-message">{error}</p>} {/* Display errors */}
                <p>
                    Don't have an account? <a href="/signup" className="signup-link">Sign up</a>
                </p>
            </div>
        </div>
    );
};

export default Login;
