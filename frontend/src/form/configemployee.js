import React, { useState } from "react";
import "antd/dist/reset.css";
import {
    Form,
    InputNumber,
    Card,
    Typography,
    Row,
    Col,
    Button,
    message,
} from "antd";
import { TeamOutlined, FileDoneOutlined, FrownOutlined } from "@ant-design/icons";


const { Title } = Typography;

const EmployeeForm = () => {
    const [employees, setEmployees] = useState({});
    const [loading, setLoading] = useState(false);

    const positions = [
        "Cashier",
        "Inventory Manager",
        "Manager",
        "Customer Help",
        "Cleaning Staff",
        "Supervisor",
    ];
    
    const shifts = [
        { name: "Morning", time: "7am to 11am" },
        { name: "Day", time: "11am to 3pm" },
        { name: "Evening", time: "3pm to 7pm" },
        { name: "Night", time: "7pm to 11pm" },
    ];

    const handleInputChange = (position, shiftName, value) => {
        setEmployees((prev) => ({
            ...prev,
            [position]: { ...prev[position], [shiftName]: value || 0 },
        }));
    };

	const handleSubmit = async () => {
		setLoading(true);
		try {
			
			const response = await fetch("http://127.0.0.1:8000/configure/assign-shifts/", {
				method: "POST",
				headers: { "Content-Type": "application/json" },
				body: JSON.stringify({ designation_counts: employees }),
			});
			
			const data = await response.json();
			if (response.ok) {
				message.success("Shift assignment successful! Click below to download.");
	
				// Provide the download link
				if (data.csv_file) {
                    const downloadLink = document.createElement("a");
                    downloadLink.href = `http://127.0.0.1:8000/media/Updated_Schedule.csv`;
                    downloadLink.target = "_blank"; // Open in a new tab
                    document.body.appendChild(downloadLink);
                    downloadLink.click();
                    document.body.removeChild(downloadLink);
                }
                
			} else {
				message.error("Error: " + (data.error || "Something went wrong"));
			}
		} catch (error) {
			console.error("Error assigning shifts:", error);
			message.error("Failed to assign shifts. Try again.");
		}
		setLoading(false);
	};
	

    return (
        <div style={{ width: "90%", margin: "0 auto", padding: "40px 0" }}>
            <Card
                title={
                    <Title
                        level={2}
                        style={{
                            marginTop: 8,
                            color: "#fff",
                            background: "linear-gradient(135deg, #6366f1 0%, #a855f7 100%)",
                            padding: "16px 14px",
                            borderRadius: "8px 8px 0 0",
                            transform: "translateY(-24px)",
                            boxShadow: "0 4px 6px rgba(0, 0, 0, 0.1)",
                        }}
                    >
                        <TeamOutlined style={{ marginRight: 12 }} /> Required Employee
                    </Title>
                }
                bordered={false}
                headStyle={{ border: "none", padding: 0 }}
                bodyStyle={{ padding: "24px" }}
                style={{
                    borderRadius: 16,
                    boxShadow: "0 8px 24px rgba(0, 0, 0, 0.1)",
                    background: "#f8fafc",
                    overflow: "hidden",
                }}
            >
                <Form layout="vertical">
                    <Title level={3} style={{ marginBottom: 16 }}>
                        <TeamOutlined style={{ marginRight: 8, color: "#1890ff" }} /> Employee Configuration Per Shift
                    </Title>

                    {positions.map((position) => (
                        <Card
                            key={position}
                            title={
                                <>
                                    <TeamOutlined style={{ color: "#1890ff" }} /> {position}
                                </>
                            }
                        >
                            <Row gutter={[24, 16]}>
                                {shifts.map((shift) => (
                                    <Col span={6} key={shift.name}>
                                        <Form.Item label={`${shift.name} (${shift.time})`}>
                                            <InputNumber
                                                min={0}
                                                max={50}
                                                placeholder="0"
                                                onChange={(value) =>
                                                    handleInputChange(position, shift.name, value)
                                                }
                                                style={{ width: "100%" }}
                                            />
                                        </Form.Item>
                                    </Col>
                                ))}
                            </Row>
                        </Card>
                    ))}

                    <Button
                        type="primary"
                        icon={<FileDoneOutlined />}
                        size="large"
                        style={{ width: "100%", marginTop: 24, height: 48, borderRadius: 8 }}
                        onClick={handleSubmit}
                        loading={loading}
                    >
                        {loading ? "Generating Report..." : "Generate Workforce Report"}
                    </Button>
                </Form>
            </Card>
        </div>
    );
};

export default EmployeeForm;
