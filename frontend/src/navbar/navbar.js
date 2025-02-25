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
					<Link to="/" style={{ textDecoration: "none" }}>
						Home
					</Link>
				</Menu.Item>
				<Menu.Item key="/employeeform">
					<Link
						to="/employeeform"
						style={{ textDecoration: "none" }}
					>
						Employee Form
					</Link>
				</Menu.Item>
				<Menu.Item key="/shiftswap">
					<Link
						to="/shiftswap"
						style={{ textDecoration: "none" }}
					>
						Swap
					</Link>
				</Menu.Item>
				<Menu.Item key="/addemployeerecords">
					<Link
						to="/addemployeerecords"
						style={{ textDecoration: "none" }}
					>
						Add Employee
					</Link>
				</Menu.Item>
				<div style={{ flexGrow: 1 }}></div>{" "}
				{/* Pushes Log Out to the left with space */}
				<Menu.Item
					key="/logout"
					style={{ marginRight: "10px" }}
				>
					<Link
						to="/logout"
						style={{ textDecoration: "none" }}
					>
						Log Out
					</Link>
				</Menu.Item>
			</Menu>
		</Header>
	);
};

export default Navbar;
