import React from "react";
import { useNavigate } from "react-router-dom";

const Home = () => {
    const navigate = useNavigate();
    
    return (
        <div style={styles.container}>
            <h1>Welcome to Home Page</h1>
            <button onClick={() => navigate("/login")}>Logout</button>
        </div>
    );
};

const styles = {
    container: { textAlign: "center", padding: "20px" },
};

export default Home;
