import React, { useState } from 'react';
import { Button, Form, Input, Select, Space, DatePicker, Table } from 'antd';
import moment from 'moment';

const { Option } = Select;
const layout = {
  labelCol: {
    span: 8,
  },
  wrapperCol: {
    span: 16,
  },
};
const tailLayout = {
  wrapperCol: {
    offset: 8,
    span: 16,
  },
};

function FormDacTrungGame() {
  const [form] = Form.useForm();
  const [tableData, setTableData] = useState([]);
  const [showTable, setShowTable] = useState(false);

  const onFinish = values => {
    console.log(values);
    setTableData(prevData => [...prevData, values]);
    setShowTable(true);
    form.resetFields();
  };

  const formatDate = date => {
    return moment(date).format('MM/YYYY');
  };

  const columns = [
    {
      title: 'Game',
      dataIndex: 'Game',
      key: 'Game',
    },
    {
      title: 'Genre',
      dataIndex: 'genre',
      key: 'genre',
    },
    {
      title: 'Release Date',
      dataIndex: 'ReleaseDate',
      key: 'ReleaseDate',
      render: formatDate, // Sử dụng hàm formatDate để định dạng giá trị ngày tháng
    },
    {
      title: 'Predicted sales',
      dataIndex: 'Predicted sales',
      key: 'Predicted sales',
      render: (text, record) => <span className="predicted-sales">{text}</span>,
    },
    {
      title: 'Point evaluation',
      dataIndex: 'Point evaluation',
      key: 'Point evaluation',
      render: (text, record) => (
        <span className="point-evaluation">{text}</span>
      ),
    },
  ];

  return (
    <>
      <Form
        {...layout}
        form={form}
        name="control-hooks"
        onFinish={onFinish}
        style={{
          maxWidth: 600,
        }}>
        <Form.Item
          name="Game"
          label="Game"
          rules={[
            {
              required: true,
            },
          ]}>
          <Input />
        </Form.Item>
        <Form.Item
          name="genre"
          label="Genre"
          rules={[
            {
              required: true,
            },
          ]}>
          <Select
            placeholder="Select a option and change input text above"
            allowClear>
            <Option value="Adventure">Adventure</Option>
            <Option value="Action">Action</Option>
            <Option value="Action-Adventure">Action-Adventure</Option>
            <Option value="Board Game">Board Game</Option>
            <Option value="Education">Education</Option>
            <Option value="Fighting">Fighting</Option>
            <Option value="Misc">Misc</Option>
            <Option value="MMO">MMO</Option>
            <Option value="Music">Music</Option>
            <Option value="Party">Party</Option>
            <Option value="Platform">Platform</Option>
            <Option value="Puzzle">Puzzle</Option>
            <Option value="Racing">Racing</Option>
            <Option value="Role-Playing">Role-Playing</Option>
            <Option value="Sandbox">Sandbox</Option>
            <Option value="Shooter">Shooter</Option>
            <Option value="Simulation">Simulation</Option>
            <Option value="Sports">Sports</Option>
            <Option value="Strategy">Strategy</Option>
            <Option value="Visual Novel">Visual Novel</Option>
            <Option value="other">other</Option>
          </Select>
        </Form.Item>
        <Form.Item
          name="ReleaseDate"
          label="Release Date"
          rules={[
            {
              required: true,
            },
          ]}>
          <DatePicker picker="month" format="MM/YYYY" />
        </Form.Item>
        <Form.Item {...tailLayout}>
          <Space>
            <Button type="primary" htmlType="submit">
              Submit
            </Button>
            <Button htmlType="button" onClick={() => form.resetFields()}>
              Reset
            </Button>
          </Space>
        </Form.Item>
      </Form>
      {showTable && <Table columns={columns} dataSource={tableData} />}
    </>
  );
}

export default FormDacTrungGame;
