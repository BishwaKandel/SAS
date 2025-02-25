import React, { useState } from "react";
import { Form, Input, Button, Typography, InputNumber, Row, Col } from "antd";
import { UserOutlined, MailOutlined, IdcardOutlined, ClockCircleOutlined, SolutionOutlined, StarOutlined } from "@ant-design/icons";

const { Title } = Typography;

const AddEmployeeRecord = () => {
    const [employee, setEmployee] = useState({
        e_id: "",
        e_name: "",
        no_of_hours_worked: "",
        designation: "",
        e_gmail: "",
        e_priority: "",
    });

    const handleChange = (name, value) => {
        setEmployee({ ...employee, [name]: value });
    };

    const handleSubmit = () => {
        console.log("Employee Record Submitted:", employee);
    };

    return (
        <div style={{ width: "100vw", height: "100vh", display: "flex", justifyContent: "center", alignItems: "center", padding: "20px" }}>
            <div style={{ width: "90%" }}>
                <Title level={2} style={{ textAlign: "center", marginBottom: "20px" }}>Add Employee Record</Title>
                <Form layout="horizontal" onFinish={handleSubmit}>
                    <Row gutter={16}>
                        <Col span={8}>
                            <Form.Item label="ID" name="e_id" rules={[{ required: true, message: "Please enter ID" }]}> 
                                <InputNumber prefix={<IdcardOutlined />} style={{ width: "100%" }} onChange={(value) => handleChange("e_id", value)} />
                            </Form.Item>
                        </Col>
                        <Col span={8}>
                            <Form.Item label="Name" name="e_name" rules={[{ required: true, message: "Please enter name" }]}> 
                                <Input prefix={<UserOutlined />} onChange={(e) => handleChange("e_name", e.target.value)} />
                            </Form.Item>
                        </Col>
                        <Col span={8}>
                            <Form.Item label="Hours Worked" name="no_of_hours_worked" rules={[{ required: true, message: "Please enter hours worked" }]}> 
                                <InputNumber prefix={<ClockCircleOutlined />} style={{ width: "100%" }} onChange={(value) => handleChange("no_of_hours_worked", value)} />
                            </Form.Item>
                        </Col>
                    </Row>
                    <Row gutter={16}>
                        <Col span={8}>
                            <Form.Item label="Designation" name="designation" rules={[{ required: true, message: "Please enter designation" }]}> 
                                <Input prefix={<SolutionOutlined />} onChange={(e) => handleChange("designation", e.target.value)} />
                            </Form.Item>
                        </Col>
                        <Col span={8}>
                            <Form.Item label="Email" name="e_gmail" rules={[{ required: true, type: "email", message: "Please enter a valid email" }]}> 
                                <Input prefix={<MailOutlined />} onChange={(e) => handleChange("e_gmail", e.target.value)} />
                            </Form.Item>
                        </Col>
                        <Col span={8}>
                            <Form.Item label="Priority" name="e_priority" rules={[{ required: true, message: "Please enter priority" }]}> 
                                <InputNumber prefix={<StarOutlined />} style={{ width: "100%" }} onChange={(value) => handleChange("e_priority", value)} />
                            </Form.Item>
                        </Col>
                    </Row>
                    <Row justify="center">
                        <Button type="primary" htmlType="submit" size="large">Add Employee</Button>
                    </Row>
                </Form>
            </div>
        </div>
    );
};

export default AddEmployeeRecord;
