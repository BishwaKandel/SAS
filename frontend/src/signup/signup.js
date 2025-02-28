import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Form, Input, Button, Card, Typography, Space, message, Modal } from "antd";
import { LockOutlined, UserOutlined, MailOutlined } from "@ant-design/icons";
import { motion } from "framer-motion";
import axios from "axios";  // Import axios to handle API requests

const { Title, Text } = Typography;

const Signup = () => {
  const [loading, setLoading] = useState(false);
  const [managerId, setManagerId] = useState(null); // State to store the generated Manager ID
  const navigate = useNavigate();

  const handleSignup = async (values) => {
	setLoading(true);
	message.loading({ content: "Creating account...", key: "signup" });
  
	try {
	  const response = await axios.post(
		"http://127.0.0.1:8000/api/auth/register", // Backend registration endpoint
		{
		  username: values.userName,
		  email: values.email,
		  password: values.password,
		}
	  );
  
	  console.log("Signup response:", response.data); // For debugging
  
	  // Check if the response contains the success status
	  if (response.data.status) {
		// If managerId is returned in the response, save it
		setManagerId(response.data.managerId);
  
		// Show success message and the Manager ID
		message.success({
		  content: "Account created successfully! Redirecting to login...",
		  key: "signup",
		});
  
		// Show the Manager ID in a success modal before redirecting
		Modal.success({
		  title: "Manager ID Assigned",
		  content: `Your Manager ID is: ${response.data.managerId}`,
		  onOk: () => {
			// Redirect to the login page after the modal is closed
			navigate("/login");
		  },
		});
	  } else {
		// Handle failure: if status is not true
		message.error({
		  content: response.data.message || "Error signing up. Please try again.",
		  key: "signup",
		});
	  }
	} catch (err) {
	  // Handle error if request fails
	  message.error({ content: "Error signing up. Please try again.", key: "signup" });
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
        background: "linear-gradient(135deg, #74EBD5 0%, #9FACE6 100%)",
      }}
    >
      <motion.div initial={{ scale: 0.9 }} animate={{ scale: 1 }} transition={{ duration: 0.3 }}>
        <Card
          style={{
            width: 420,
            padding: "30px",
            textAlign: "center",
            borderRadius: "12px",
            boxShadow: "0px 10px 30px rgba(0, 0, 0, 0.1)",
            background: "#ffffff",
          }}
        >
          <Title level={2} style={{ marginBottom: "10px", color: "#333" }}>
            Create an Account
          </Title>
          <Text type="secondary">Enter your details to sign up</Text>

          <Form name="signup-form" onFinish={handleSignup} layout="vertical" style={{ marginTop: "20px" }}>
            <Form.Item name="userName" rules={[{ required: true, message: "Please enter your username!" }]}>
              <Input prefix={<UserOutlined />} placeholder="Username" />
            </Form.Item>

            <Form.Item
              name="email"
              rules={[
                { required: true, message: "Please enter your email!" },
                { type: "email", message: "Please enter a valid email!" },
              ]}
            >
              <Input prefix={<MailOutlined />} placeholder="Email address" />
            </Form.Item>

            <Form.Item name="password" rules={[{ required: true, message: "Please enter your password!" }]}>
              <Input.Password prefix={<LockOutlined />} placeholder="Password" />
            </Form.Item>

            <Form.Item>
              <Button
                type="primary"
                htmlType="submit"
                loading={loading}
                block
                style={{ height: "40px", fontSize: "16px", background: "#1890ff", borderColor: "#1890ff" }}
              >
                Sign Up
              </Button>
            </Form.Item>
          </Form>

          <Space direction="vertical" size="small">
            <Text type="secondary">
              Already have an account? <a href="/login">Login</a>
            </Text>
          </Space>
        </Card>
      </motion.div>
    </div>
  );
};

export default Signup;
