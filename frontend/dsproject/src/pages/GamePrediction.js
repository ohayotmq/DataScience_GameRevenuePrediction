import React, { useState } from "react";
import {
  DesktopOutlined,
  MenuFoldOutlined,
  MenuUnfoldOutlined,
  PieChartOutlined,
} from "@ant-design/icons";
import { Button, Menu } from "antd";
import FormDoanhSo from "../component/FormDoanhSo";
import FormDacTrungGame from "../component/FormDacTrungGam";

const { Item } = Menu;
const items = [
  {
    key: "1",
    icon: <PieChartOutlined />,
    label: "Dự đoán theo doanh số ",
  },
  {
    key: "2",
    icon: <DesktopOutlined />,
    label: "Dự đoán theo đặc trưng game",
  },
];
export default function GamePrediction() {
  const [collapsed, setCollapsed] = useState(false);
  const [selectedOption, setSelectedOption] = useState(items[0].key);
  const toggleCollapsed = () => {
    setCollapsed(!collapsed);
  };
  const handleMenuClick = (e) => {
    setSelectedOption(e.key);
  };

  const renderForm = () => {
    if (selectedOption === "1") {
      return <FormDoanhSo />;
    } else if (selectedOption === "2") {
      return <FormDacTrungGame />;
    }
    return null;
  };

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "row",
        alignItems: "flex-start",
        width: 300,
      }}
    >
      <Menu
        defaultSelectedKeys={["1"]}
        defaultOpenKeys={["sub1"]}
        mode="inline"
        theme="dark"
        inlineCollapsed={collapsed}
        onClick={handleMenuClick}
        style={{
          flex: "0 0 auto", // Không co giãn Menu khi thay đổi kích thước
        }}
      >
        {items.map((item) => (
          <Item key={item.key} icon={item.icon}>
            {item.label}
          </Item>
        ))}
      </Menu>
      <div
        style={{
          flex: "1", // Phần còn lại của layout sẽ được phần đóng
          marginLeft: 20, // Khoảng cách giữa Menu và Form
        }}
      >
        <Button
          type="primary"
          onClick={toggleCollapsed}
          style={{
            marginBottom: 16,
          }}
        >
          {collapsed ? <MenuUnfoldOutlined /> : <MenuFoldOutlined />}
        </Button>
        {renderForm()}
      </div>
    </div>
  );
}
