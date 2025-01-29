import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import { useNavigate } from "react-router-dom";
import "./employeeform.css"; // Import the CSS file

const EmployeeForm = () => {
	const navigate = useNavigate();
	const [file, setFile] = useState(null);
	const [departments, setDepartments] = useState([
		{ name: "", employees: "" },
	]);

	// Handle file input change
	const handleFileChange = (e) => {
		const uploadedFile = e.target.files[0];
		setFile(uploadedFile);
		console.log("Uploaded file:", uploadedFile);
	};

	// Handle department input change
	const handleDepartmentChange = (index, field, value) => {
		const updatedDepartments = [...departments];
		updatedDepartments[index][field] = value;
		setDepartments(updatedDepartments);
	};

	const addDepartment = () => {
		if (departments.length > 0) {
			const lastDepartment =
				departments[departments.length - 1];

			// Ensure last department has both fields filled
			if (
				!lastDepartment.name.trim() ||
				!lastDepartment.employees.trim()
			) {
				alert(
					"Please fill in all fields before adding a new department."
				);
				return;
			}
		}

		// Add a new empty department
		setDepartments([
			...departments,
			{ name: "", employees: "" },
		]);
	};

	// Remove a department
	const removeDepartment = (index) => {
		const updatedDepartments = departments.filter(
			(_, i) => i !== index
		);
		setDepartments(updatedDepartments);
	};

	// Generate Report
	const generateReport = () => {
		console.log("Uploaded File:", file);
		console.log("Departments:", departments);
		alert("Report Generated! Check console for details.");
	};

	// Swap Options
	const swap = () => {
		alert("Swap function called!");
		navigate("/ShiftSwap");
	};

	return (
		<div className="form-container container mt-5">
			<h1 className="text-center mb-4 form-title">
				Employee Configuration
			</h1>

			{/* File Input */}

			{/* Scrollable Department Section */}
			<div className="department-container">
				{departments.map((department, index) => (
					<div className="department-form mb-4" key={index}>
						<div className="d-flex justify-content-between align-items-center">
							<h5>Department {index + 1}</h5>
							{departments.length > 1 && (
								<button
									type="button"
									className="remove-btn"
									onClick={() => removeDepartment(index)}
								>
									&times;
								</button>
							)}
						</div>
						<div className="mb-3">
							<label
								htmlFor={`departmentName${index}`}
								className="form-label"
							>
								Department Name
							</label>
							<input
								type="text"
								className="form-control input-field"
								id={`departmentName${index}`}
								placeholder="Department name"
								value={department.name}
								onChange={(e) =>
									handleDepartmentChange(
										index,
										"name",
										e.target.value
									)
								}
							/>
						</div>
						<div className="mb-3">
							<label
								htmlFor={`employees${index}`}
								className="form-label"
							>
								Number of Employees Required
							</label>
							<input
								type="number"
								className="form-control input-field"
								id={`employees${index}`}
								placeholder="Numbers"
								min={0}
								value={department.employees}
								onChange={(e) =>
									handleDepartmentChange(
										index,
										"employees",
										e.target.value
									)
								}
							/>
						</div>
					</div>
				))}
			</div>

			{/* Add Department Button */}
			<button
				type="button"
				className="btn btn-info mb-4"
				onClick={addDepartment}
			>
				Next Add Department
			</button>

			{/* Generate and Swap Buttons */}
			<div className="button-group d-flex gap-3 mt-4">
				<button
					type="button"
					className="btn btn-primary w-50 generate-btn"
					onClick={generateReport}
				>
					Generate
				</button>
				<button
					type="button"
					className="btn btn-secondary w-50 swap-btn"
					onClick={swap}
				>
					Swap Options
				</button>
			</div>
		</div>
	);
};

export default EmployeeForm;
