import React, { useState } from "react";
import { Button, Form, Input, Select, Space, Table } from "antd";
import predictSales from "../service/predict_1";
import "./Form.css";

const { Option } = Select;
const layout = {
  labelCol: { span: 8 },
  wrapperCol: { span: 16 },
};
const tailLayout = {
  wrapperCol: { offset: 8, span: 16 },
};

function FormDoanhSo() {
  const [form] = Form.useForm();
  const [tableData, setTableData] = useState([]);
  const [showTable, setShowTable] = useState(false);

  const onFinish = async (values) => {
    try {
      const salesData = {
        NA_sales: values.NARevenue,
        EU_sales: values.EURevenue,
        JP_sales: values.JPRevenue,
        otherSales: values.otherSales || 0,
        releaseMonth: values.releaseMonth || new Date().getMonth() + 1,
        releaseYear: values.releaseYear || new Date().getFullYear(),
      };

      const predictions = await predictSales(salesData);

      const newData = {
        ...values,
        ...predictions,
      };

      setTableData((prevData) => [...prevData, newData]);
      setShowTable(true);
      form.resetFields();
    } catch (error) {
      console.error("Error predicting sales:", error);
    }
  };

  const columns = [
    { title: "Game", dataIndex: "Game", key: "Game" },
    // { title: "Genre", dataIndex: "genre", key: "genre" },
    { title: "NA Revenue", dataIndex: "NARevenue", key: "NARevenue" },
    { title: "JP Revenue", dataIndex: "JPRevenue", key: "JPRevenue" },
    { title: "EU Revenue", dataIndex: "EURevenue", key: "EURevenue" },
    { title: "Other Sales", dataIndex: "otherSales", key: "otherSales" },
    { title: "Release Month", dataIndex: "releaseMonth", key: "releaseMonth" },
    { title: "Release Year", dataIndex: "releaseYear", key: "releaseYear" },
    { title: "Decision Tree", dataIndex: "decisionTree", key: "decisionTree" },
    { title: "KNN", dataIndex: "knn", key: "knn" },
    { title: "Multi Linear", dataIndex: "multiLinear", key: "multiLinear" },
    { title: "Random Forest", dataIndex: "randomForest", key: "randomForest" },
    { title: "SVR Linear", dataIndex: "svrLinear", key: "svrLinear" },
    { title: "SVR Non Linear", dataIndex: "svrNonLinear", key: "svrNonLinear" },
  ];

  return (
    <>
      <Form
        {...layout}
        form={form}
        name="control-hooks"
        onFinish={onFinish}
        style={{ maxWidth: 800, minWidth: 600 }}
      >
        <Form.Item name="Game" label="Game" rules={[{ required: true }]}>
          <Input />
        </Form.Item>
        {/* <Form.Item name="genre" label="Genre" rules={[{ required: true }]}>
          <Select placeholder="Select a genre" allowClear>
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
            <Option value="other">Other</Option>
          </Select>
        </Form.Item> */}
        <Form.Item
          name="NARevenue"
          label="NA Revenue"
          rules={[{ required: true }]}
        >
          <Input />
        </Form.Item>
        <Form.Item
          name="JPRevenue"
          label="JP Revenue"
          rules={[{ required: true }]}
        >
          <Input />
        </Form.Item>
        <Form.Item
          name="EURevenue"
          label="EU Revenue"
          rules={[{ required: true }]}
        >
          <Input />
        </Form.Item>
        <Form.Item
          name="otherSales"
          label="Other Sales"
          rules={[{ required: true }]}
        >
          <Input />
        </Form.Item>
        <Form.Item
          name="releaseMonth"
          label="Release Month"
          rules={[{ required: true }]}
        >
          <Input type="number" min={1} max={12} />
        </Form.Item>
        <Form.Item
          name="releaseYear"
          label="Release Year"
          rules={[{ required: true }]}
        >
          <Input type="number" min={2000} max={new Date().getFullYear()} />
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

export default FormDoanhSo;
