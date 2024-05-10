// MainLayout.js

import React from 'react';
import { Layout, Menu } from 'antd';
import { MenuOutlined } from '@ant-design/icons';
import { Link, Outlet } from 'react-router-dom';

const { Header, Content } = Layout;

const MainLayout = () => {
  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Header className="bg-gray-800 p-0 flex justify-between">
        <div className="flex items-center">
          <div className="text-white mr-8">Logo</div>
          <Menu
            theme="dark"
            mode="horizontal"
            defaultSelectedKeys={['1']}
            className="border-none"
            style={{ lineHeight: '64px' }}
          >
            <Menu.Item key="1"><Link to="/">Home</Link></Menu.Item>
            <Menu.Item key="2"><Link to="/gameprediction">Game Prediction</Link></Menu.Item>
            <Menu.Item key="3"><Link to="/analysis">Analysis</Link></Menu.Item>
            <Menu.Item key="4"><Link to="/gamecomparing">Game Comparing</Link></Menu.Item>
          </Menu>
        </div>
        <div className="text-white cursor-pointer">
          <MenuOutlined />
        </div>
      </Header>
      <Content>
        <div className="p-4">
          <Outlet />
        </div>
      </Content>
    </Layout>
  );
};

export default MainLayout;
