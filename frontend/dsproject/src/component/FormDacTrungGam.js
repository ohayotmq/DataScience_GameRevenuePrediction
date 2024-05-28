import React, { useState } from "react";
import { Button, Form, Input, Select, Space, Table } from "antd";
import predictDacTrungGame from "../service/predict_2";

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

  const onFinish = async (values) => {
    try {
      const salesData = {
        console: values.console,
        genre: values.genre,
        // publisher: values.publisher,
        NA_sales: values.NA_sales,
        EU_sales: values.EU_sales,
        JP_sales: values.JP_sales,
      };
      const predictions = await predictDacTrungGame(salesData);
      setTableData((prevData) => [...prevData, { ...values, ...predictions }]);
      setShowTable(true);
      form.resetFields();
    } catch (error) {
      console.error("Error predicting sales:", error);
    }
  };

  const columns = [
    {
      title: "Console",
      dataIndex: "console",
      key: "console",
    },
    {
      title: "Genre",
      dataIndex: "genre",
      key: "genre",
    },
    {
      title: "Publisher",
      dataIndex: "publisher",
      key: "publisher",
    },
    {
      title: "NA Sales",
      dataIndex: "NA_sales",
      key: "NA_sales",
    },
    {
      title: "EU Sales",
      dataIndex: "EU_sales",
      key: "EU_sales",
    },
    {
      title: "JP Sales",
      dataIndex: "JP_sales",
      key: "JP_sales",
    },
    // {
    //   title: "Decision Tree",
    //   dataIndex: "decisionTree",
    //   key: "decisionTree",
    // },
    // {
    //   title: "KNN",
    //   dataIndex: "knn",
    //   key: "knn",
    // },
    // {
    //   title: "Multi Linear",
    //   dataIndex: "multiLinear",
    //   key: "multiLinear",
    // },
    // {
    //   title: "Random Forest",
    //   dataIndex: "randomForest",
    //   key: "randomForest",
    // },
    // {
    //   title: "SVR Linear",
    //   dataIndex: "svrLinear",
    //   key: "svrLinear",
    // },
    // {
    //   title: "SVR Non Linear",
    //   dataIndex: "svrNonLinear",
    //   key: "svrNonLinear",
    // },

    
    { title: "Multi Linear", dataIndex: "multiLinear", key: "multiLinear" },
    { title: "Polynomial Linear", dataIndex: "polynomial", key: "polynomial" },
    { title: "KNN", dataIndex: "knn", key: "knn" },
    { title: "Decision Tree", dataIndex: "decisionTree", key: "decisionTree" },
    { title: "Random Forest", dataIndex: "randomForest", key: "randomForest" },
    { title: "SVR Linear", dataIndex: "svrLinear", key: "svrLinear" },
    { title: "SVR Non Linear", dataIndex: "svrNonLinear", key: "svrNonLinear" },
    { title: "XGB", dataIndex: "xgb", key: "xgb" },
  ];

  const consoles = [
    "PS",
    "X360",
    "PS3",
    "DS",
    "Wii",
    "PS2",
    "GBA",
    "PC",
    "PS4",
    "GBC",
    "PSV",
    "PSP",
    "XB",
    "3DS",
    "SNES",
    "GC",
    "XOne",
    "SAT",
    "NS",
    "GB",
    "DC",
    "WiiU",
    "N64",
    "PSN",
    "PCE",
    "GEN",
    "3DO",
    "NES",
    "2600",
    "XBL",
    "NG",
    "WW",
    "SCD",
    "Mob",
    "GG",
    "VC",
    "WS",
    "PCFX",
    "OSX",
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
        <Form.Item
          name="console"
          label="Console"
          rules={[
            {
              required: true,
              message: "Please select a console",
            },
          ]}
        >
          <Select placeholder="Select a console" allowClear>
            {consoles.map((console) => (
              <Option key={console} value={console}>
                {console}
              </Option>
            ))}
          </Select>
        </Form.Item>
        <Form.Item name="genre" label="Genre" rules={[{ required: true }]}>
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
        </Form.Item>
        <Form.Item
          name="publisher"
          label="Publisher"
          rules={[
            {
              required: true,
              message: "Please enter the publisher",
            },
          ]}
        >
          <Input />
        </Form.Item>
        <Form.Item
          name="NA_sales"
          label="NA Sales"
          rules={[
            {
              required: true,
              message: "Please enter NA Sales",
            },
          ]}
        >
          <Input />
        </Form.Item>
        <Form.Item
          name="EU_sales"
          label="EU Sales"
          rules={[
            {
              required: true,
              message: "Please enter EU Sales",
            },
          ]}
        >
          <Input />
        </Form.Item>
        <Form.Item
          name="JP_sales"
          label="JP Sales"
          rules={[
            {
              required: true,
              message: "Please enter JP Sales",
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

export default FormDacTrungGame;
