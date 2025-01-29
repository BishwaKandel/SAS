import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./signup.css"; // Import CSS file

const Signup = () => {
    const [userName, setUserName]= useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const navigate = useNavigate();

    const handleSignup = (e) => {
        e.preventDefault();
        console.log("Signing up with", email, password);
        navigate("/login"); // Redirect after signup
    };

    return (
        <div className="signup-container">
            <div className="signup-box">
                <h2>Sign Up</h2>
                <form onSubmit={handleSignup}>
                <input
                        type="userName"
                        placeholder="UserName"
                        value={userName}
                        onChange={(e) => setUserName(e.target.value)}
                        required
                        className="signup-input"
                    />
                    <input
                        type="email"
                        placeholder="Email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                        className="signup-input"
                    />
                    <input
                        type="password"
                        placeholder="Password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                        className="signup-input"
                    />
                    <button type="submit" className="signup-button">Sign Up</button>
                </form>
                <p>
                    Already have an account? <a href="/login" className="login-link">Login</a>
                </p>
            </div>
        </div>
    );
};

export default Signup;
