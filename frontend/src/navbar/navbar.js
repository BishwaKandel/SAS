import React, { useState, useEffect } from "react";
import { Layout, Menu, ConfigProvider } from "antd";
import { Link, useLocation } from "react-router-dom";
import {
	HomeOutlined,
	FormOutlined,
	SwapOutlined,
	UserAddOutlined,
	LogoutOutlined,
	EyeOutlined,
	PoweroffOutlined,
} from "@ant-design/icons";

const { Header } = Layout;

const Navbar = () => {
	const location = useLocation();
	const [selectedKey, setSelectedKey] = useState(
		location.pathname
	);

	useEffect(() => {
		setSelectedKey(location.pathname);
	}, [location]);

	return (
		<ConfigProvider
			theme={{
				components: {
					Menu: {
						itemHoverBg: "#003366", // Hover background
						itemHoverColor: "#fff", // Hover text color
						itemSelectedColor: "#fff",
						itemSelectedBg: "#004080",
						colorText: "#d9e8ff", // Default text color
					},
				},
			}}
		>
			<Header
				style={{
					position: "fixed",
					width: "100%",
					zIndex: 1000,
					top: 0,
					left: 0,
					padding: 0,
					background:
						"linear-gradient(135deg,rgb(10, 27, 113) 0%,rgb(10, 77, 46) 100%)",
					boxShadow: "0px 4px 10px rgba(0, 0, 0, 0.2)",
					borderBottom: "1px solid #004080",
					fontFamily: "Poppins, sans-serif",
				}}
			>
				<div
					style={{
						maxWidth: 1200,
						margin: "0 auto",
						padding: "0 24px",
						display: "flex",
						alignItems: "center",
						justifyContent: "space-between",
					}}
				>
					{/* Logo */}
					<div
						className="logo"
						style={{
							fontSize: 22,
							fontWeight: 700,
							color: "#fff",
							marginRight: "32px",
							transition: "0.3s",
							":hover": {
								transform: "scale(1.05)",
							},
						}}
					>
						<Link
							to="/"
							style={{
								textDecoration: "none",
								color: "#fff",
							}}
						>
							SAS
						</Link>
					</div>

					{/* Navigation Menu */}
					<Menu
						mode="horizontal"
						selectedKeys={[selectedKey]}
						onClick={(e) => setSelectedKey(e.key)}
						style={{
							background: "transparent",
							borderBottom: "none",
							flex: 1,
							color: "#d9e8ff",
							".ant-menu-item": {
								transition: "all 0.3s",
								"&:hover": {
									fontWeight: 600,
								},
							},
						}}
					>
						<Menu.Item key="/" icon={<HomeOutlined />}>
							<Link
								to="/"
								style={{
									color: "inherit",
									textDecoration: "none",
								}}
							>
								Home
							</Link>
						</Menu.Item>

						<Menu.Item
							key="/employeeform"
							icon={<FormOutlined />}
						>
							<Link
								to="/employeeform"
								style={{
									color: "inherit",
									textDecoration: "none",
								}}
							>
								Generate
							</Link>
						</Menu.Item>

						<Menu.Item
							key="/shiftswap"
							icon={<SwapOutlined />}
						>
							<Link
								to="/shiftswap"
								style={{
									color: "inherit",
									textDecoration: "none",
								}}
							>
								Shift Swap
							</Link>
						</Menu.Item>

						<Menu.Item
							key="/addemployeerecords"
							icon={<UserAddOutlined />}
						>
							<Link
								to="/addemployeerecords"
								style={{
									color: "inherit",
									textDecoration: "none",
								}}
							>
								Add Employee
							</Link>
						</Menu.Item>

						<Menu.Item key="" icon={<EyeOutlined />}>
							<Link
								to=""
								style={{
									color: "inherit",
									textDecoration: "none",
								}}
							>
								View Report{" "}
							</Link>
						</Menu.Item>

						<Menu.Item
							key="/logout"
							icon={
								<LogoutOutlined
									style={{ fontSize: "14px" }}
								/>
							} // Set smaller icon size
							style={{
								color: "#fff",
								fontWeight: 500,
								marginLeft: "auto",
								fontSize: "12px", // Decrease font size
								display: "flex",
								alignItems: "center",
								justifyContent: "center",
								background: "transparent", // Remove background
							}}
						>
							<Link
								to="/login"
								style={{
									color: "inherit",
									textDecoration: "none",
									display: "flex",
									alignItems: "center",
								}}
							>
								Log Out
							</Link>
						</Menu.Item>
					</Menu>
				</div>
			</Header>
		</ConfigProvider>
	);
};

export default Navbar;
