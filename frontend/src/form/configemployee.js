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
} from "antd";
import {
	TeamOutlined,
	FileDoneOutlined,
} from "@ant-design/icons";

const { Title } = Typography;

const EmployeeForm = () => {
	const [employees, setEmployees] = useState({});

	const positions = [
		"Cashiers",
		"Inventory Managers",
		"Managers",
		"Customer Help",
		"Cleaning Staff",
		"Supervisor",
	];

	const shifts = [
		{ name: "Morning", time: "06:00 - 12:00" },
		{ name: "Day", time: "12:00 - 18:00" },
		{ name: "Evening", time: "18:00 - 00:00" },
		{ name: "Night", time: "00:00 - 06:00" },
	];

	const handleInputChange = (
		position,
		shiftIndex,
		value
	) => {
		setEmployees((prev) => ({
			...prev,
			[position]: {
				...prev[position],
				[shiftIndex]: value,
			},
		}));
	};

	return (
		<div
			style={{
				width: "90%",
				margin: "0 auto",
				padding: "40px 0",
			}}
		>
			<Card
				title={
					<Title
						level={2}
						style={{
							marginTop: 8,
							color: "#fff",
							background:
								"linear-gradient(135deg, #6366f1 0%, #a855f7 100%)",
							padding: "16px 14px",
							borderRadius: "8px 8px 0 0",
							transform: "translateY(-24px)",
							boxShadow: "0 4px 6px rgba(0, 0, 0, 0.1)",
						}}
					>
						<TeamOutlined style={{ marginRight: 12 }} />{" "}
						Employee Configuration Form
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
						<TeamOutlined
							style={{ marginRight: 8, color: "#1890ff" }}
						/>{" "}
						Employee Configuration Per Shift
					</Title>

					{positions.map((position) => (
						<Card
							key={position}
							title={
								<>
									<TeamOutlined
										style={{ color: "#1890ff" }}
									/>{" "}
									{position}
								</>
							}
						>
							<Row gutter={[24, 16]}>
								{shifts.map((shift, shiftIndex) => (
									<Col span={6} key={shiftIndex}>
										<Form.Item
											label={`${shift.name} (${shift.time})`}
										>
											<InputNumber
												min={0}
												max={50}
												placeholder="0"
												onChange={(value) =>
													handleInputChange(
														position,
														shiftIndex,
														value
													)
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
						style={{
							width: "100%",
							background:
								"linear-gradient(135deg, #36D1DC 0%, #5B86E5 100%)",

							marginTop: 24,
							height: 48,
							borderRadius: 8,
						}}
					>
						Generate Report
					</Button>
				</Form>
			</Card>
		</div>
	);
};

export default EmployeeForm;
