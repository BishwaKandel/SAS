import React, { useState } from "react";
import { Layout, Menu } from "antd";
import { Link, useLocation } from "react-router-dom";

const { Header } = Layout;

const Navbar = () => {
	const location = useLocation();
	const [selectedKey, setSelectedKey] = useState(
		location.pathname
	);

	return (
		<Header
			style={{
				position: "fixed",
				width: "100vw",
				zIndex: 1000,
				top: 0,
				left: 0,
				padding: 0,
			}}
		>
			<Menu
				theme="dark"
				mode="horizontal"
				selectedKeys={[selectedKey]}
				onClick={(e) => setSelectedKey(e.key)}
				style={{
					display: "flex",
					alignItems: "center",
					justifyContent: "space-between",
					width: "100%",
				}}
			>
				<Menu.Item key="/">
					<Link to="/">Home</Link>
				</Menu.Item>
				<Menu.Item key="/employeeform">
					<Link to="/employeeform">Employee Form</Link>
				</Menu.Item>
				<Menu.Item key="/shiftswap">
					<Link to="/shiftswap">Swap</Link>
				</Menu.Item>
				<Menu.Item key="/addemployeerecorde">
					<Link to="/addemployeerecords">Add Employee</Link>
				</Menu.Item>
				<Menu.Item
					key="/logout"
					style={{ marginLeft: "auto" }}
				>
					Log Out
				</Menu.Item>
			</Menu>
		</Header>
	);
};

export default Navbar;
