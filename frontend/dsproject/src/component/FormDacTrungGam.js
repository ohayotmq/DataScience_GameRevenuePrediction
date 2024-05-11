import React from 'react';
import { Button, Form, Input, Select, Space, DatePicker } from 'antd';
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

  const onFinish = values => {
    console.log(values);
  };
  const onReset = () => {
    form.resetFields();
  };

  return (
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
        noStyle
        shouldUpdate={(prevValues, currentValues) =>
          prevValues.gender !== currentValues.gender
        }>
        {({ getFieldValue }) =>
          getFieldValue('gender') === 'other' ? (
            <Form.Item
              name="customizeGender"
              label="Customize Gender"
              rules={[
                {
                  required: true,
                },
              ]}>
              <Input />
            </Form.Item>
          ) : null
        }
      </Form.Item>
      <Form.Item
        name="Release Date"
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
          <Button htmlType="button" onClick={onReset}>
            Reset
          </Button>
        </Space>
      </Form.Item>
    </Form>
  );
}
export default FormDacTrungGame;
