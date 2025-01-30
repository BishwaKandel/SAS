import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import { useNavigate } from "react-router-dom";
import "./employeeform.css"; // Import the CSS file

const EmployeeForm = () => {
    const navigate = useNavigate();
    const [employees, setEmployees] = useState({
        Cashiers: "",
        InventoryManagers: "",
        Managers: "",
        CustomerHelp: "",
        CleaningStaff: "",
        Supervisors: "",
    });

    // Handle input change
    const handleInputChange = (field, value) => {
        setEmployees({ ...employees, [field]: value });
    };

    // Generate Report
    const generateReport = () => {
        console.log("Employee Data:", employees);
        alert("Report Generated! Check console for details.");
    };

    // Swap Options
    const swap = () => {
        alert("Swap function called!");
        navigate("/ShiftSwap");
    };

    return (
        <div className="form-container container mt-5">
            <h1 className="text-center mb-4 form-title">Employee Configuration</h1>
            
            {Object.keys(employees).map((key, index) => (
                <div className="mb-3" key={index}>
                    <label className="form-label" htmlFor={key}>
                        {"Number of " + key.replace(/([A-Z])/g, ' $1').replace(/^./, str => str.toUpperCase())}
                    </label>
                    <input
                        type="number"
                        className="form-control input-field"
                        id={key}
                        placeholder={"Enter number of " + key.replace(/([A-Z])/g, ' $1')}
                        min={0}
                        value={employees[key]}
                        onChange={(e) => handleInputChange(key, e.target.value)}
                    />
                </div>
            ))}
            
            <div className="button-group d-flex gap-3 mt-4">
                <button type="button" className="btn btn-primary w-50 generate-btn" onClick={generateReport}>
                    Generate
                </button>
                <button type="button" className="btn btn-secondary w-50 swap-btn" onClick={swap}>
                    Swap Options
                </button>
            </div>
        </div>
    );
};

export default EmployeeForm;
