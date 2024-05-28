import React, { useState } from "react";
import { Button, Form, Input, Select, Space, Table, message } from "antd";
import predictGoiYKhuVuc from "../service/predict_3";

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

function FormGoiYKhuVuc() {
  const [form] = Form.useForm();
  const [tableData, setTableData] = useState([]);
  const [showTable, setShowTable] = useState(false);

  const onFinish = async (values) => {
    try {
      const predictions = await predictGoiYKhuVuc(
        values.genre,
        values?.region,
        values?.console
      );
      const newData = {
        ...values,
        region_max: predictions.region_max,
        console_max: predictions.console_max,
        revenue_max: predictions.revenue_max,
      };
      console.log("New data:", newData);

      setTableData((prevData) => [...prevData, newData]);
      setShowTable(true);
      form.resetFields();
    } catch (error) {
      message.error("Error predicting sales. Please try again later.");
      console.error("Error predicting sales:", error);
    }
  };

  const columns = [
    {
      title: "Genre",
      dataIndex: "genre",
      key: "genre",
    },
    {
      title: "Region",
      dataIndex: "region",
      key: "region",
    },
    {
      title: "Console",
      dataIndex: "console",
      key: "console",
    },
    {
      title: "Region Max",
      dataIndex: "region_max",
      key: "region_max",
    },
    {
      title: "Console Max",
      dataIndex: "console_max",
      key: "console_max",
    },
    {
      title: "Revenue Max",
      dataIndex: "revenue_max",
      key: "revenue_max",
    },
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

  const regions = ["JP", "NA", "Other", "PAL"];

  return (
    <>
      <Form
        {...layout}
        form={form}
        name="control-hooks"
        onFinish={onFinish}
        style={{ maxWidth: 800, minWidth: 600 }}
      >
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
        <Form.Item name="region" label="Region">
          <Select placeholder="Select a region">
            {regions.map((region) => (
              <Option key={region} value={region}>
                {region}
              </Option>
            ))}
          </Select>
        </Form.Item>

        <Form.Item name="console" label="Console">
          <Select placeholder="Select a console">
            {consoles.map((console) => (
              <Option key={console} value={console}>
                {console}
              </Option>
            ))}
          </Select>
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

export default FormGoiYKhuVuc;
