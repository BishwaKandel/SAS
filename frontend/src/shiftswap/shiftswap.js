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
  Select,
} from "antd";
import {
  SwapOutlined,
  IdcardOutlined,
  UserOutlined,
} from "@ant-design/icons";

const { Title, Text } = Typography;
const { Option } = Select;

const ShiftSwap = () => {
  const [form] = Form.useForm();
  const [swapAvailable, setSwapAvailable] = useState(false);
  const [resultMessage, setResultMessage] = useState("");

  const checkSwap = () => {
    const values = form.getFieldsValue();
    if (
      values.employee1Id &&
      values.employee2Id &&
      values.shiftName1 !== values.shiftName2 &&
      values.shiftDay1 !== values.shiftDay2
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
        alignItems: "center",
        height: "100vh",
        background: "#f0f2f5",
        padding: "20px",
      }}
    >
      <Card
        style={{
          width: 800,
          padding: "20px",
          borderRadius: "10px",
          boxShadow: "0px 4px 15px rgba(0, 0, 0, 0.2)",
          background: "#fff",
        }}
      >
        <Title level={3} style={{ textAlign: "center" }}>
          🔄 Shift Exchange Portal
        </Title>
        <Text type="secondary" style={{ display: "block", textAlign: "center", marginBottom: "20px" }}>
          Facilitate smooth shift transitions between team members
        </Text>

        <Form form={form} layout="vertical">
          <Row gutter={16} align="middle" justify="center">
            <Col span={10}>
              <Card title="👤 Employee 1" bordered>
                <Form.Item name="employee1Id" label="Staff ID" rules={[{ required: true }]}>
                  <Input prefix={<IdcardOutlined />} placeholder="E-1001" />
                </Form.Item>
                <Form.Item name="designation1" label="Designation" rules={[{ required: true }]}>
                  <Select placeholder="Select Designation">
                    <Option value="manager">Manager</Option>
                    <Option value="inventoryManager">Inventory Manager</Option>
                    <Option value="cleaningStaff">Cleaning Staff</Option>
                    <Option value="cashier">Cashier</Option>
                    <Option value="customerHelp">Customer Help</Option>
                    <Option value="security">Security</Option>
                  </Select>
                </Form.Item>
                <Form.Item name="shiftDay1" label="Shift Date" rules={[{ required: true }]}>
                  <DatePicker format="YYYY-MM-DD" style={{ width: "100%" }} />
                </Form.Item>
                <Form.Item name="shiftName1" label="Shift Name" rules={[{ required: true }]}>
                  <Select placeholder="Select Shift">
                    <Option value="morning">Morning</Option>
                    <Option value="day">Day</Option>
                    <Option value="evening">Evening</Option>
                    <Option value="night">Night</Option>
                  </Select>
                </Form.Item>
              </Card>
            </Col>
            
            <Col span={4} style={{ display: "flex", justifyContent: "center", alignItems: "center" }}>
              <SwapOutlined style={{ fontSize: "36px", color: "#1890ff" }} />
            </Col>
            
            <Col span={10}>
              <Card title="👤 Employee 2" bordered>
                <Form.Item name="employee2Id" label="Staff ID" rules={[{ required: true }]}>
                  <Input prefix={<IdcardOutlined />} placeholder="E-1002" />
                </Form.Item>
                <Form.Item name="designation2" label="Designation" rules={[{ required: true }]}>
                  <Select placeholder="Select Designation">
                    <Option value="manager">Manager</Option>
                    <Option value="inventoryManager">Inventory Manager</Option>
                    <Option value="cleaningStaff">Cleaning Staff</Option>
                    <Option value="cashier">Cashier</Option>
                    <Option value="customerHelp">Customer Help</Option>
                    <Option value="supervisor">Supervisor</Option>
                  </Select>
                </Form.Item>
                <Form.Item name="shiftDay2" label="Shift Date" rules={[{ required: true }]}>
                  <DatePicker format="YYYY-MM-DD" style={{ width: "100%" }} />
                </Form.Item>
                <Form.Item name="shiftName2" label="Shift Name" rules={[{ required: true }]}>
                  <Select placeholder="Select Shift">
                    <Option value="morning">Morning</Option>
                    <Option value="day">Day</Option>
                    <Option value="evening">Evening</Option>
                    <Option value="night">Night</Option>
                  </Select>
                </Form.Item>
              </Card>
            </Col>
          </Row>

          <div style={{ textAlign: "center", marginTop: "20px" }}>
            <Button type="primary" icon={<UserOutlined />} onClick={checkSwap}>
              Verify Swap Eligibility
            </Button>
            <Button type="default" style={{ marginLeft: "10px" }} icon={<SwapOutlined />} onClick={swapShifts}>
              Confirm Swap
            </Button>
          </div>

          {resultMessage && (
            <div style={{ textAlign: "center", marginTop: "15px", fontSize: "16px", fontWeight: "bold" }}>
              {swapAvailable ? `✅ ${resultMessage}` : `⚠️ ${resultMessage}`}
            </div>
          )}
        </Form>
      </Card>
    </div>
  );
};

export default ShiftSwap;