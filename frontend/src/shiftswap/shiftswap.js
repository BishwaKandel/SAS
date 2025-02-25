import React, { useState } from "react";
import {
	Card,
	Form,
	Input,
	Button,
	DatePicker,
	Typography,
	Row,
	Col,
	message,
} from "antd";
import {
	SwapOutlined,
	UserOutlined,
	IdcardOutlined,
	CalendarOutlined,
} from "@ant-design/icons";
import dayjs from "dayjs";

const { Title, Text } = Typography;

const ShiftSwap = () => {
	const [form] = Form.useForm();
	const [swapAvailable, setSwapAvailable] = useState(false);
	const [resultMessage, setResultMessage] = useState("");

	const checkSwap = () => {
		const values = form.getFieldsValue();
		if (
			values.employee1Id &&
			values.employee2Id &&
			values.shiftId1 !== values.shiftId2
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
				alignItems: "flex-start",
				height: "100vh",
				background: "#f0f2f5",
				padding: "20px",
			}}
		>
			<Card
				style={{
					width: 600,
					padding: "20px",
					borderRadius: "10px",
					boxShadow: "0px 4px 15px rgba(0, 0, 0, 0.2)",
					background: "#fff",
				}}
			>
				<Title
					level={3}
					style={{
						textAlign: "center",
						marginBottom: "15px",
					}}
				>
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
					<Row gutter={16}>
						{/* Employee 1 Section */}
						<Col span={11}>
							<Card title="👤 Employee 1" bordered>
								<Form.Item
									name="employee1Id"
									label="Staff ID"
									rules={[
										{
											required: true,
											message: "Please enter Staff ID!",
										},
									]}
								>
									<Input
										prefix={<IdcardOutlined />}
										placeholder="E-1234"
									/>
								</Form.Item>

								<Form.Item
									name="shiftDay1"
									label="Shift Date"
									rules={[
										{
											required: true,
											message: "Please select shift date!",
										},
									]}
								>
									<DatePicker
										format="YYYY-MM-DD"
										style={{ width: "100%" }}
									/>
								</Form.Item>

								<Form.Item
									name="shiftId1"
									label="Shift ID"
									rules={[
										{
											required: true,
											message: "Please enter Shift ID!",
										},
									]}
								>
									<Input
										prefix={<CalendarOutlined />}
										placeholder="SH-5678"
									/>
								</Form.Item>
							</Card>
						</Col>

						{/* Swap Icon */}
						<Col
							span={2}
							style={{
								display: "flex",
								alignItems: "center",
								justifyContent: "center",
							}}
						>
							<SwapOutlined
								style={{
									fontSize: "30px",
									color: "#1890ff",
								}}
							/>
						</Col>

						{/* Employee 2 Section */}
						<Col span={11}>
							<Card title="👤 Employee 2" bordered>
								<Form.Item
									name="employee2Id"
									label="Staff ID"
									rules={[
										{
											required: true,
											message: "Please enter Staff ID!",
										},
									]}
								>
									<Input
										prefix={<IdcardOutlined />}
										placeholder="E-5678"
									/>
								</Form.Item>

								<Form.Item
									name="shiftDay2"
									label="Shift Date"
									rules={[
										{
											required: true,
											message: "Please select shift date!",
										},
									]}
								>
									<DatePicker
										format="YYYY-MM-DD"
										style={{ width: "100%" }}
									/>
								</Form.Item>

								<Form.Item
									name="shiftId2"
									label="Shift ID"
									rules={[
										{
											required: true,
											message: "Please enter Shift ID!",
										},
									]}
								>
									<Input
										prefix={<CalendarOutlined />}
										placeholder="SH-1234"
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
							icon={<UserOutlined />}
							onClick={checkSwap}
						>
							Verify Swap Eligibility
						</Button>
					</div>

					{resultMessage && (
						<div
							style={{
								textAlign: "center",
								marginTop: "15px",
								color: swapAvailable
									? "#52c41a"
									: "#ff4d4f",
								fontSize: "16px",
								fontWeight: "bold",
							}}
						>
							{swapAvailable
								? `✅ ${resultMessage}`
								: `⚠️ ${resultMessage}`}
						</div>
					)}

					{swapAvailable && (
						<div
							style={{
								textAlign: "center",
								marginTop: "20px",
							}}
						>
							<Button
								type="primary"
								danger
								icon={<SwapOutlined />}
								onClick={swapShifts}
							>
								Confirm Shift Exchange
							</Button>
						</div>
					)}
				</Form>
			</Card>
		</div>
	);
};

export default ShiftSwap;
