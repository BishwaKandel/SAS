import React, { useState } from "react";
import { Card, Row, Col, Typography, Button, Divider } from "antd";
import { UserOutlined, ClockCircleOutlined, MailOutlined, IdcardOutlined, DeleteOutlined, StarOutlined } from "@ant-design/icons";

const { Title, Text } = Typography;

const EmployeeView = () => {
    const [employees, setEmployees] = useState([
        { e_id: 1, e_name: "Alice Johnson", no_of_hours_worked: 0, designation: "Cashier", e_gmail: "alice.johnson@email.com", e_priority: 8 },
        { e_id: 2, e_name: "Bob Smith", no_of_hours_worked: 5, designation: "Manager", e_gmail: "bob.smith@email.com", e_priority: 10 },
        { e_id: 3, e_name: "Charlie Brown", no_of_hours_worked: 3, designation: "Assistant", e_gmail: "charlie.brown@email.com", e_priority: 6 },
        { e_id: 4, e_name: "Daisy Evans", no_of_hours_worked: 4, designation: "Clerk", e_gmail: "daisy.evans@email.com", e_priority: 7 },
        { e_id: 5, e_name: "Ethan Wright", no_of_hours_worked: 8, designation: "Supervisor", e_gmail: "ethan.wright@email.com", e_priority: 9 },
        { e_id: 6, e_name: "Fiona Green", no_of_hours_worked: 2, designation: "Receptionist", e_gmail: "fiona.green@email.com", e_priority: 5 },
        { e_id: 7, e_name: "George Hill", no_of_hours_worked: 7, designation: "Security", e_gmail: "george.hill@email.com", e_priority: 4 },
        { e_id: 8, e_name: "Hannah Scott", no_of_hours_worked: 6, designation: "Technician", e_gmail: "hannah.scott@email.com", e_priority: 7 },
        { e_id: 9, e_name: "Ian Clark", no_of_hours_worked: 9, designation: "Analyst", e_gmail: "ian.clark@email.com", e_priority: 8 },
        { e_id: 10, e_name: "Julia Adams", no_of_hours_worked: 1, designation: "Intern", e_gmail: "julia.adams@email.com", e_priority: 3 }
    ]);

    const handleDelete = (id) => {
        const updatedEmployees = employees.filter(emp => emp.e_id !== id);
        setEmployees(updatedEmployees);
    };

    return (
        <>
            <Title level={2}>Employee View</Title>
            {employees.map((emp) => (
                <Card key={emp.e_id} style={{ marginBottom: 4, borderRadius: 4 }}>
                    <Row align="middle" justify="space-between">
                        <Col>
                            <Text><UserOutlined style={{ marginRight: 8 }} /> {emp.e_name}</Text>
                        </Col>
                        <Col>
                            <Text><IdcardOutlined style={{ marginRight: 8 }} /> {emp.designation}</Text>
                        </Col>
                        <Col>
                            <Text><MailOutlined style={{ marginRight: 8 }} /> {emp.e_gmail}</Text>
                        </Col>
                        <Col>
                            <Text><ClockCircleOutlined style={{ marginRight: 8 }} /> {emp.no_of_hours_worked} hours</Text>
                        </Col>
                        <Col>
                            <Text><StarOutlined style={{ marginRight: 8 }} /> Priority: {emp.e_priority}</Text>
                        </Col>
                        <Col>
                            <Button danger icon={<DeleteOutlined />} onClick={() => handleDelete(emp.e_id)}>
                                Delete
                            </Button>
                        </Col>
                    </Row>
                    <Divider />
                </Card>
            ))}
        </>
    );
};

export default EmployeeView;
