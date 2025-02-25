import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

import {
	Form,
	Input,
	Button,
	Checkbox,
	Card,
	Typography,
	Space,
} from "antd";
import {
	LockOutlined,
	UserOutlined,
	GoogleOutlined,
} from "@ant-design/icons";

const { Title, Text } = Typography;

const Login = () => {
	const [loading, setLoading] = useState(false);
	const navigate = useNavigate();
	const handleLogin = async (values) => {
		setLoading(true);

		// Temporary Credentials
		const tempManagerID = "1234";
		const tempPassword = "123456";

		if (
			values.managerID === tempManagerID &&
			values.password === tempPassword
		) {
			alert("Logged in using temporary credentials!");
			localStorage.setItem("authToken", "tempToken"); // Store fake auth token
			navigate("/home"); // Ensure lowercase
			setLoading(false);
			return;
		}

		try {
			const response = await axios.post(
				"http://127.0.0.1:8000/login/",
				{
					ManagerID: values.managerID,
					password: values.password,
				}
			);

			console.log(response.data); // Debug API response

			if (response.data.token) {
				localStorage.setItem(
					"authToken",
					response.data.token
				);
				navigate("/home"); // Ensure lowercase
			} else {
				alert("Invalid Manager ID or Password");
			}
		} catch (err) {
			alert("Network Error: Unable to reach the server.");
		} finally {
			setLoading(false);
		}
	};

	return (
		<div
			style={{
				position: "fixed",
				top: 0,
				left: 0,
				width: "100vw",
				height: "100vh",
				display: "flex",
				justifyContent: "center",
				alignItems: "center",
				background: "#F8F9FC",
			}}
		>
			<Card
				style={{
					width: 400,
					padding: "30px",
					textAlign: "center",
					borderRadius: "10px",
					boxShadow: "0px 4px 20px rgba(0, 0, 0, 0.2)", // Darker shadow only around the card
					background: "#fff",
				}}
			>
				<Title level={3} style={{ marginBottom: "10px" }}>
					Welcome back
				</Title>
				<Text type="secondary">
					Please enter your login details
				</Text>

				<Form
					name="login-form"
					onFinish={handleLogin}
					layout="vertical"
					style={{ marginTop: "20px" }}
				>
					<Form.Item
						name="managerID"
						rules={[
							{
								required: true,
								message: "Please enter your Manager ID!",
							},
							{
								pattern: /^[0-9]{4}$/,
								message:
									"Manager ID must be exactly 4 digits!",
							},
						]}
					>
						<Input
							prefix={<UserOutlined />}
							placeholder="Enter 4-digit Manager ID"
							maxLength={4}
						/>
					</Form.Item>

					<Form.Item
						name="password"
						rules={[
							{
								required: true,
								message: "Please enter your password!",
							},
						]}
					>
						<Input.Password
							prefix={<LockOutlined />}
							placeholder="Password"
						/>
					</Form.Item>

					<div
						style={{
							display: "flex",
							justifyContent: "space-between",
							alignItems: "center",
							marginBottom: "15px",
						}}
					>
						<Checkbox>Remember for 30 days</Checkbox>
						<a href="/forgot-password">Forgot password</a>
					</div>

					<Form.Item>
						<Button
							type="primary"
							htmlType="submit"
							loading={loading}
							block
							style={{ height: "40px", fontSize: "16px" }}
						>
							Sign in
						</Button>
					</Form.Item>
				</Form>

				<Space
					direction="vertical"
					size="small"
					style={{ marginTop: "15px" }}
				>
					<Text type="secondary">
						Don't have an account?{" "}
						<a href="/signup">Sign up</a>
					</Text>
				</Space>
			</Card>
		</div>
	);
};

export default Login;
