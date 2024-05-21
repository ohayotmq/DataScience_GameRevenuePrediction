import React, { useState } from "react";
import { Button, Form, Input, Select, Space, Table } from "antd";
import "./Form.css";
import predictSales from "../service/predict_1";

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

function FormDoanhSo() {
  const [form] = Form.useForm();
  const [tableData, setTableData] = useState([]);
  const [showTable, setShowTable] = useState(false);

  const onFinish = async (values) => {
    console.log(values);

    const salesData = {
      NA_sales: parseFloat(values.NARevenue),
      EU_sales: parseFloat(values.EURevenue),
      JP_sales: parseFloat(values.JPRevenue),
      otherSales: 0,
      releaseMonth: 1,
      releaseYear: 2022,
    };

    try {
      const predictedSales = await predictSales(salesData);

      // Thêm dữ liệu và kết quả dự đoán vào bảng
      setTableData((prevData) => [
        ...prevData,
        { ...values, "Predicted sales": predictedSales },
      ]);
      setShowTable(true);
    } catch (error) {
      console.error("Error predicting sales:", error);
    }

    form.resetFields();
  };

  const columns = [
    {
      title: "Game",
      dataIndex: "Game",
      key: "Game",
    },
    {
      title: "Genre",
      dataIndex: "genre",
      key: "genre",
    },
    {
      title: "NA Revenue",
      dataIndex: "NARevenue",
      key: "NARevenue",
    },
    {
      title: "JP Revenue",
      dataIndex: "JPRevenue",
      key: "JPRevenue",
    },
    {
      title: "EU Revenue",
      dataIndex: "EURevenue",
      key: "EURevenue",
    },
    {
      title: "Predicted sales",
      dataIndex: "Predicted sales",
      key: "Predicted sales",
      render: (text) => <span className="predicted-sales">{text}</span>,
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
        }}
      >
        <Form.Item
          name="Game"
          label="Game"
          rules={[
            {
              required: true,
            },
          ]}
        >
          <Input />
        </Form.Item>
        <Form.Item
          name="genre"
          label="Genre"
          rules={[
            {
              required: true,
            },
          ]}
        >
          <Select
            placeholder="Select a option and change input text above"
            allowClear
          >
            <Option value="RPG">RPG</Option>
            <Option value="Sports">Sports</Option>
            <Option value="Adventure">Adventure</Option>
            <Option value="Action">Action</Option>
            <Option value="Strategy">Strategy</Option>
            <Option value="Fighting">Fighting</Option>
            <Option value="other">other</Option>
          </Select>
        </Form.Item>
        <Form.Item
          name="NARevenue"
          label="NA Revenue"
          rules={[
            {
              required: true,
            },
          ]}
        >
          <Input />
        </Form.Item>
        <Form.Item
          name="JPRevenue"
          label="JP Revenue"
          rules={[
            {
              required: true,
            },
          ]}
        >
          <Input />
        </Form.Item>
        <Form.Item
          name="EURevenue"
          label="EU Revenue"
          rules={[
            {
              required: true,
            },
          ]}
        >
          <Input />
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
