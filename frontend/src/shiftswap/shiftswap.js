import React, { useState } from "react";
import "./shiftswap.css"; // Import the CSS file

const ShiftSwap = () => {
  const [employee1Id, setEmployee1Id] = useState("");
  const [employee2Id, setEmployee2Id] = useState("");
  const [shiftId1, setShiftId1] = useState("");
  const [shiftId2, setShiftId2] = useState("");
  const [shiftDay1, setShiftDay1] = useState("");
  const [shiftDay2, setShiftDay2] = useState("");
  const [swapAvailable, setSwapAvailable] = useState(false);
  const [resultMessage, setResultMessage] = useState("");

  const checkSwap = () => {
    if (employee1Id && employee2Id && shiftId1 !== shiftId2) {
      setResultMessage("Valid for Swap");
      setSwapAvailable(true);
    } else {
      setResultMessage("Not Valid for Swap");
      setSwapAvailable(false);
    }
  };

  const swapShifts = () => {
    alert("Shifts swapped successfully!");
    // Logic to update backend or database can be added here.
  };

  return (
    <div className="shift-swap-container">
      <h1 className="text-center">Shift Swap Portal</h1>
      <form className="shift-swap-form">
        <div className="form-group">
          <label htmlFor="employee1Id">Employee 1 ID</label>
          <input
            type="text"
            id="employee1Id"
            value={employee1Id}
            onChange={(e) => setEmployee1Id(e.target.value)}
            placeholder="Enter Employee 1 ID"
          />
        </div>

        <div className="form-group">
          <label htmlFor="shiftDay1">Shift Day of Employee 1</label>
          <input
            type="date"
            id="shiftDay1"
            value={shiftDay1}
            onChange={(e) => setShiftDay1(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label htmlFor="shiftId1">Employee 1 Shift ID</label>
          <input
            type="text"
            id="shiftId1"
            value={shiftId1}
            onChange={(e) => setShiftId1(e.target.value)}
            placeholder="Enter Employee 1 Shift ID"
          />
        </div>

        <div className="form-group">
          <label htmlFor="employee2Id">Employee 2 ID</label>
          <input
            type="text"
            id="employee2Id"
            value={employee2Id}
            onChange={(e) => setEmployee2Id(e.target.value)}
            placeholder="Enter Employee 2 ID"
          />
        </div>

        <div className="form-group">
          <label htmlFor="shiftDay2">Shift Day of Employee 2</label>
          <input
            type="date"
            id="shiftDay2"
            value={shiftDay2}
            onChange={(e) => setShiftDay2(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label htmlFor="shiftId2">Employee 2 Shift ID</label>
          <input
            type="text"
            id="shiftId2"
            value={shiftId2}
            onChange={(e) => setShiftId2(e.target.value)}
            placeholder="Enter Employee 2 Shift ID"
          />
        </div>

        <button
          type="button"
          className="btn btn-primary"
          onClick={checkSwap}
        >
          Check Swap Availability
        </button>

        <div className="result-message">
          <p className={swapAvailable ? "valid" : "invalid"}>{resultMessage}</p>
        </div>

        {swapAvailable && (
          <button
            type="button"
            className="btn btn-success"
            onClick={swapShifts}
          >
            Swap Shifts
          </button>
        )}
      </form>
    </div>
  );
};

export default ShiftSwap;