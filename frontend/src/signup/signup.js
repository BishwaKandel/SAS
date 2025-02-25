import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import {
	Form,
	Input,
	Button,
	Card,
	Typography,
	Space,
} from "antd";
import {
	LockOutlined,
	UserOutlined,
	MailOutlined,
} from "@ant-design/icons";

const { Title, Text } = Typography;

const Signup = () => {
	const [loading, setLoading] = useState(false);
	const navigate = useNavigate();

	const handleSignup = async (values) => {
		setLoading(true);
		try {
			console.log(
				"Signing up with",
				values.userName,
				values.email,
				values.password
			);
			navigate("/login"); // Redirect after signup
		} catch (err) {
			alert("Error signing up.");
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
					boxShadow: "0px 4px 20px rgba(0, 0, 0, 0.2)", // Dark shadow only around card
					background: "#fff",
				}}
			>
				<Title level={3} style={{ marginBottom: "10px" }}>
					Create an account
				</Title>
				<Text type="secondary">
					Enter your details to sign up
				</Text>

				<Form
					name="signup-form"
					onFinish={handleSignup}
					layout="vertical"
					style={{ marginTop: "20px" }}
				>
					<Form.Item
						name="userName"
						rules={[
							{
								required: true,
								message: "Please enter your username!",
							},
						]}
					>
						<Input
							prefix={<UserOutlined />}
							placeholder="Username"
						/>
					</Form.Item>

					<Form.Item
						name="email"
						rules={[
							{
								required: true,
								message: "Please enter your email!",
							},
							{
								type: "email",
								message: "Please enter a valid email!",
							},
						]}
					>
						<Input
							prefix={<MailOutlined />}
							placeholder="Email address"
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

					<Form.Item>
						<Button
							type="primary"
							htmlType="submit"
							loading={loading}
							block
							style={{ height: "40px", fontSize: "16px" }}
						>
							Sign Up
						</Button>
					</Form.Item>
				</Form>

				<Space direction="vertical" size="small">
					<Text type="secondary">
						Already have an account?{" "}
						<a href="/login">Login</a>
					</Text>
				</Space>
			</Card>
		</div>
	);
};

export default Signup;
