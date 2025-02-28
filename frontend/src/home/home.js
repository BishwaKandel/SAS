import React from "react";
import { useNavigate } from "react-router-dom";
import { Button, Card, Typography, Space } from "antd";
import {
	PlusCircleOutlined,
	TeamOutlined,
} from "@ant-design/icons";

const { Title } = Typography;

const Home = () => {
	const navigate = useNavigate();

	return (
		<div
			style={{
				display: "flex",
				justifyContent: "center", // Changed to right alignment
				alignItems: "center",
				minHeight: "100vh",
				background: "#f0f2f5",
				paddingRight: "5%", // Add right padding
			}}
		>
			<Card
				style={{
					width: "35vw", // 35% of viewport width
					minWidth: 400, // Minimum width for mobile
					padding: 40,
					borderRadius: 16,
					boxShadow: "0 4px 12px rgba(0, 0, 0, 0.1)",
					marginRight: "5%", // Add some margin from right edge
					height: "60vh", // 60% of viewport height
					display: "flex",
					flexDirection: "column",
					justifyContent: "center",
				}}
			>
				<Title
					level={2}
					style={{
						marginBottom: 40,
						color: "#1890ff",
						textAlign: "center",
						background:
							"linear-gradient(135deg, #1890ff 0%, #0050b3 100%)",
						WebkitBackgroundClip: "text",
						WebkitTextFillColor: "transparent",
						fontSize: "2rem", // Responsive font size
					}}
				>
					SAS Features
				</Title>

				<Space
					direction="vertical"
					size="large"
					style={{ width: "100%" }}
				>
					<Button
						type="primary"
						icon={<PlusCircleOutlined />}
						onClick={() => navigate("/shiftdetails")}
						size="large"
						style={{
							width: "100%",
							height: 70, // Reduced height
							fontSize: "1.1rem",
							borderRadius: 12,
							background:
								"linear-gradient(135deg, #36D1DC 0%, #5B86E5 100%)",
							border: "none",
							boxShadow:
								"0 4px 6px rgba(54, 209, 220, 0.3)",
							transition: "all 0.3s",
							padding: "0 25px",
						}}
						onMouseEnter={(e) => {
							e.target.style.transform = "translateY(-2px)";
							e.target.style.boxShadow =
								"0 6px 8px rgba(54, 209, 220, 0.4)";
						}}
						onMouseLeave={(e) => {
							e.target.style.transform = "translateY(0)";
							e.target.style.boxShadow =
								"0 4px 6px rgba(54, 209, 220, 0.3)";
						}}
					>
						Add New Shifts
					</Button>

					<Button
						type="primary"
						icon={<TeamOutlined />}
						onClick={() => navigate("/viewemployeedetails")}
						size="large"
						style={{
							width: "100%",
							height: 70, // Reduced height
							fontSize: "1.1rem",
							borderRadius: 12,
							background:
								"linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%)",
							border: "none",
							boxShadow:
								"0 4px 6px rgba(255, 107, 107, 0.3)",
							transition: "all 0.3s",
							padding: "0 25px",
						}}
						onMouseEnter={(e) => {
							e.target.style.transform = "translateY(-2px)";
							e.target.style.boxShadow =
								"0 6px 8px rgba(255, 107, 107, 0.4)";
						}}
						onMouseLeave={(e) => {
							e.target.style.transform = "translateY(0)";
							e.target.style.boxShadow =
								"0 4px 6px rgba(255, 107, 107, 0.3)";
						}}
					>
						View Employee Records
					</Button>
				</Space>
			</Card>
		</div>
	);
};

export default Home;
