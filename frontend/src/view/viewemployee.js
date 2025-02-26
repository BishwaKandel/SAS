import React, { useState } from "react";
import {
	Card,
	Row,
	Col,
	Typography,
	Button,
	Divider,
	Tag,
} from "antd";
import {
	UserOutlined,
	ClockCircleOutlined,
	MailOutlined,
	IdcardOutlined,
	DeleteOutlined,
	StarFilled,
} from "@ant-design/icons";

const { Title, Text } = Typography;

const EmployeeView = () => {
	// ... [keep the same useState initialization]
	const [employees, setEmployees] = useState([
		{
			e_id: 1,
			e_name: "Alice Johnson",
			no_of_hours_worked: 0,
			designation: "Cashier",
			e_gmail: "alice.johnson@email.com",
			e_priority: 8,
		},
		{
			e_id: 2,
			e_name: "Bob Smith",
			no_of_hours_worked: 5,
			designation: "Manager",
			e_gmail: "bob.smith@email.com",
			e_priority: 10,
		},
		{
			e_id: 3,
			e_name: "Charlie Brown",
			no_of_hours_worked: 3,
			designation: "Inventory Manager",
			e_gmail: "charlie.brown@email.com",
			e_priority: 6,
		},
		{
			e_id: 4,
			e_name: "Daisy Evans",
			no_of_hours_worked: 4,
			designation: "Cleaning Staff",
			e_gmail: "daisy.evans@email.com",
			e_priority: 7,
		},
		{
			e_id: 5,
			e_name: "Ethan Wright",
			no_of_hours_worked: 8,
			designation: "Supervisor",
			e_gmail: "ethan.wright@email.com",
			e_priority: 9,
		},
		{
			e_id: 6,
			e_name: "Fiona Green",
			no_of_hours_worked: 2,
			designation: "Cashier",
			e_gmail: "fiona.green@email.com",
			e_priority: 5,
		},
		{
			e_id: 7,
			e_name: "George Hill",
			no_of_hours_worked: 7,
			designation: "Cashier",
			e_gmail: "george.hill@email.com",
			e_priority: 4,
		},
		{
			e_id: 8,
			e_name: "Hannah Scott",
			no_of_hours_worked: 6,
			designation: "Manager",
			e_gmail: "hannah.scott@email.com",
			e_priority: 7,
		},
		{
			e_id: 9,
			e_name: "Ian Clark",
			no_of_hours_worked: 9,
			designation: "Cleaning Staff",
			e_gmail: "ian.clark@email.com",
			e_priority: 8,
		},
		{
			e_id: 10,
			e_name: "Julia Adams",
			no_of_hours_worked: 1,
			designation: "Customer Help",
			e_gmail: "julia.adams@email.com",
			e_priority: 3,
		},
	]);

	const handleDelete = (id) => {
		const updatedEmployees = employees.filter(
			(emp) => emp.e_id !== id
		);
		setEmployees(updatedEmployees);
	};
	const getPriorityStars = (priority) => {
		return Array.from({ length: 5 }, (_, index) => (
			<StarFilled
				key={index}
				style={{
					color:
						index < priority / 2 ? "#ffc107" : "#e0e0e0",
					fontSize: "16px",
					marginRight: 2,
				}}
			/>
		));
	};

	const designationColor = {
		Manager: "#ff4d4f",
		"Cleaning Staff": "#1890ff",
		"Inventory Manager": "#52c41a",
		
		Supervisor: "#fa8c16",
		"Cashier": "#13c2c2",
		"Customer Help": "#eb2f96",
		Technician: "#2f54eb",
		Analyst: "#f5222d",
		Intern: "#a0d911",
	};

	return (
		<div style={{ padding: "24px" }}>
			<Title
				level={2}
				style={{ color: "#2d3436", marginBottom: "24px" }}
			>
				👥 Employee Records
			</Title>
			{employees.map((emp) => (
				<Card
					key={emp.e_id}
					style={{
						marginBottom: 8,
						borderRadius: 12,
						boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
						transition: "all 0.3s",
						borderLeft: `4px solid ${
							designationColor[emp.designation]
						}`,
					}}
					bodyStyle={{ padding: "16px" }}
					hoverable
				>
					<Row
						align="middle"
						gutter={[16, 16]}
						justify="space-between"
					>
						<Col flex="200px">
							<div
								style={{
									display: "flex",
									alignItems: "center",
								}}
							>
								<UserOutlined
									style={{
										fontSize: "18px",
										color: "#595959",
										marginRight: 8,
									}}
								/>
								<Text strong style={{ fontSize: "16px" }}>
									{emp.e_name}
								</Text>
							</div>
						</Col>

						<Col>
							<Tag
								icon={<IdcardOutlined />}
								color={designationColor[emp.designation]}
								style={{
									borderRadius: 12,
									padding: "4px 12px",
								}}
							>
								{emp.designation}
							</Tag>
						</Col>

						<Col flex="250px">
							<div
								style={{
									display: "flex",
									alignItems: "center",
								}}
							>
								<MailOutlined
									style={{
										fontSize: "16px",
										color: "#ff4d4f",
										marginRight: 8,
									}}
								/>
								<Text type="secondary">{emp.e_gmail}</Text>
							</div>
						</Col>

						<Col>
							<div
								style={{
									display: "flex",
									alignItems: "center",
								}}
							>
								<ClockCircleOutlined
									style={{
										fontSize: "16px",
										color: "#fa8c16",
										marginRight: 8,
									}}
								/>
								<Text strong>{emp.no_of_hours_worked}</Text>
								<Text
									type="secondary"
									style={{ marginLeft: 4 }}
								>
									hours
								</Text>
							</div>
						</Col>

						<Col>
							<div
								style={{
									display: "flex",
									alignItems: "center",
								}}
							>
								{getPriorityStars(emp.e_priority)}
							</div>
						</Col>

						<Col>
							<Button
								danger
								shape="circle"
								icon={<DeleteOutlined />}
								onClick={() => handleDelete(emp.e_id)}
								style={{
									boxShadow: "0 2px 4px rgba(0,0,0,0.1)",
								}}
							/>
						</Col>
					</Row>
				</Card>
			))}
		</div>
	);
};

export default EmployeeView;
