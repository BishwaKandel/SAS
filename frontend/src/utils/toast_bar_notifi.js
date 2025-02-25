import React from "react";
import { Button, notification } from "antd";
import { SmileOutlined } from "@ant-design/icons";

const ToastBar = ({ message, description, type = "info" }) => {
  const openNotification = () => {
    notification[type]({
      message: message || "Default Title",
      description: description || "This is a default notification message.",
      icon: <SmileOutlined style={{ color: "#108ee9" }} />,
      placement: "topRight",
    });
  };

  return (
    <div style={{ padding: 20 }}>
      <Button type="primary" onClick={openNotification}>
        Show Toast
      </Button>
    </div>
  );
};

export default ToastBar;
