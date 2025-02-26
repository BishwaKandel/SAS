import React, { useState } from "react";
import {
	Card,
	Form,
	Input,
	Button,
	Typography,
	Row,
	Col,
	message,
	Select,
} from "antd";
import {
	SwapOutlined,
	IdcardOutlined,
	CheckCircleOutlined,
	ThunderboltOutlined,
} from "@ant-design/icons";

const { Title, Text } = Typography;
const { Option } = Select;

const ShiftSwap = () => {
	const [form] = Form.useForm();
	const [swapAvailable, setSwapAvailable] = useState(false);
	const [resultMessage, setResultMessage] = useState("");

	const checkSwap = () => {
		const values = form.getFieldsValue();
		if (
			values.employee1Id &&
			values.employee2Id &&
			values.shiftName1 !== values.shiftName2
		) {
			setResultMessage("Valid for Swap");
			setSwapAvailable(true);
			message.success("Shift swap is valid.");
		} else {
			setResultMessage("Not Valid for Swap");
			setSwapAvailable(false);
			message.error("Shift swap is not valid.");
		}
	};

	const swapShifts = () => {
		message.success("Shifts swapped successfully!");
		form.resetFields();
		setSwapAvailable(false);
	};

	return (
		<div
			style={{
				display: "flex",
				justifyContent: "center",
				alignItems: "center",
				height: "100vh",
				background: "#f0f2f5",
				padding: "20px",
			}}
		>
			<Card
				style={{
					width: 800,
					padding: "20px",
					borderRadius: "10px",
					boxShadow: "0px 4px 15px rgba(0, 0, 0, 0.2)",
					background: "#fff",
				}}
			>
				<Title level={3} style={{ textAlign: "center" }}>
					🔄 Shift Exchange Portal
				</Title>
				<Text
					type="secondary"
					style={{
						display: "block",
						textAlign: "center",
						marginBottom: "20px",
					}}
				>
					Facilitate smooth shift transitions between team
					members
				</Text>

				<Form form={form} layout="vertical">
					<Row gutter={16} style={{ marginBottom: 20 }}>
						<Col span={12}>
							<Form.Item
								name="shiftDay"
								label="Shift Day"
								rules={[{ required: true }]}
							>
								<Select placeholder="Select Day">
									{Array.from({ length: 7 }, (_, i) => (
										<Option
											key={i + 1}
											value={`day${i + 1}`}
										>
											Day {i + 1}
										</Option>
									))}
								</Select>
							</Form.Item>
						</Col>
						<Col span={12}>
							<Form.Item
								name="designation"
								label="Designation"
								rules={[{ required: true }]}
							>
								<Select placeholder="Select Designation">
									<Option value="cashier">Cashier</Option>
									<Option value="manager">Manager</Option>
									<Option value="customer_help">
										Customer Help
									</Option>
									<Option value="supervisor">
										Supervisor
									</Option>
									<Option value="cleaning_staff">
										Cleaning Staff
									</Option>
									<Option value="inventory_manager">
										Inventory Manager
									</Option>
								</Select>
							</Form.Item>
						</Col>
					</Row>

					<Row gutter={16} align="middle" justify="center">
						<Col span={10}>
							<Card title="👤 Employee 1" bordered>
								<Form.Item
									name="employee1Id"
									label="Employee ID"
									rules={[{ required: true }]}
								>
									<Input
										prefix={<IdcardOutlined />}
										placeholder="E-1001"
									/>
								</Form.Item>
							</Card>
						</Col>

						<Col
							span={4}
							style={{
								display: "flex",
								justifyContent: "center",
								alignItems: "center",
							}}
						>
							<SwapOutlined
								style={{
									fontSize: "36px",
									color: "#1890ff",
								}}
							/>
						</Col>

						<Col span={10}>
							<Card title="👤 Employee 2" bordered>
								<Form.Item
									name="employee2Id"
									label="Employee ID"
									rules={[{ required: true }]}
								>
									<Input
										prefix={<IdcardOutlined />}
										placeholder="E-1002"
									/>
								</Form.Item>
							</Card>
						</Col>
					</Row>

					<div
						style={{
							textAlign: "center",
							marginTop: "20px",
						}}
					>
						<Button
							type="primary"
							style={{
								background:
									"linear-gradient(135deg, #1890ff 0%, #0050b3 100%)",
								borderColor: "#52c41a",
								fontSize: "18px",
								padding: "12px 24px",
							}}
							onClick={checkSwap}
							icon={<CheckCircleOutlined />}
						>
							Verify Swap Eligibility
						</Button>
						<Button
							type="primary"
							style={{
								marginLeft: "80px",
								background: "linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%)",
								
								fontSize: "18px",
								padding: "12px 24px",
							}}
							onClick={swapShifts}
							disabled={!swapAvailable}
							icon={<ThunderboltOutlined />}
						>
							Generate
						</Button>
					</div>

					{resultMessage && (
						<div
							style={{
								textAlign: "center",
								marginTop: "15px",
								fontSize: "16px",
								fontWeight: "bold",
								color: swapAvailable
									? "#52c41a"
									: "#ff4d4f",
							}}
						>
							{swapAvailable ? "✅ " : "⚠️ "}
							{resultMessage}
						</div>
					)}
				</Form>
			</Card>
		</div>
	);
};

export default ShiftSwap;
