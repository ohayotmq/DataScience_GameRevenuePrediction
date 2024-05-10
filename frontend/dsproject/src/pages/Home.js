import React, { useState } from 'react';
import { Table, Input, Space } from 'antd';
import { SearchOutlined } from '@ant-design/icons';

const { Column } = Table;
const { Search } = Input;

const data = [
  {
    key: '1',
    game: 'Game A',
    console: 'Console A',
    publisher: 'Publisher A',
    releaseDate: '2022-01-01',
    last: '2022-02-01',
    score: 90,
    naRevenue: 100,
    jpRevenue: 80,
    euRevenue: 120,
    totalRevenue: 300,
  },
  {
    key: '2',
    game: 'Game B',
    console: 'Console B',
    publisher: 'Publisher B',
    releaseDate: '2023-01-01',
    last: '2023-02-01',
    score: 100,
    naRevenue: 200,
    jpRevenue: 700,
    euRevenue: 70,
    totalRevenue: 400,
  },
];

const Home = () => {
  const [searchText, setSearchText] = useState('');
  const [searchedColumn, setSearchedColumn] = useState('');

  const getColumnSearchProps = (dataIndex) => ({
    filterDropdown: ({ setSelectedKeys, selectedKeys, confirm, clearFilters }) => (
      <div style={{ padding: 8 }}>
        <Input
          placeholder={`Search ${dataIndex}`}
          value={selectedKeys[0]}
          onChange={(e) => setSelectedKeys(e.target.value ? [e.target.value] : [])}
          onPressEnter={() => handleSearch(selectedKeys, confirm, dataIndex)}
          style={{ marginBottom: 8, display: 'block' }}
        />
        <Space>
          <button onClick={() => handleReset(clearFilters)} style={{ width: 90 }}>
            Reset
          </button>
          <button
            type="primary"
            onClick={() => handleSearch(selectedKeys, confirm, dataIndex)}
            icon={<SearchOutlined />}
            style={{ width: 90 }}
          >
            Search
          </button>
        </Space>
      </div>
    ),
    filterIcon: (filtered) => <SearchOutlined style={{ color: filtered ? '#1890ff' : undefined }} />,
    onFilter: (value, record) =>
      record[dataIndex].toString().toLowerCase().includes(value.toLowerCase()),
    onFilterDropdownVisibleChange: (visible) => {
      if (visible) {
        setTimeout(() => document.getElementById('search-input').select(), 100);
      }
    },
    render: (text) =>
      searchedColumn === dataIndex ? (
        <span style={{ backgroundColor: '#ffc069' }}>{text}</span>
      ) : (
        text
      ),
  });

  const handleSearch = (selectedKeys, confirm, dataIndex) => {
    confirm();
    setSearchText(selectedKeys[0]);
    setSearchedColumn(dataIndex);
  };

  const handleReset = (clearFilters) => {
    clearFilters();
    setSearchText('');
  };

  const handleTableSearch = (selectedKeys, confirm) => {
    confirm();
    setSearchText(selectedKeys[0]);
  };

  const handleTableReset = (clearFilters) => {
    clearFilters();
    setSearchText('');
  };

  const getColumnSearchPropsForAllColumns = () => ({
    filterDropdown: ({ setSelectedKeys, selectedKeys, confirm, clearFilters }) => (
      <div style={{ padding: 8 }}>
        <Input
          placeholder={`Search all columns`}
          value={selectedKeys[0]}
          onChange={(e) => setSelectedKeys(e.target.value ? [e.target.value] : [])}
          onPressEnter={() => handleTableSearch(selectedKeys, confirm)}
          style={{ marginBottom: 8, display: 'block' }}
        />
        <Space>
          <button onClick={() => handleTableReset(clearFilters)} style={{ width: 90 }}>
            Reset
          </button>
          <button
            type="primary"
            onClick={() => handleTableSearch(selectedKeys, confirm)}
            icon={<SearchOutlined />}
            style={{ width: 90 }}
          >
            Search
          </button>
        </Space>
      </div>
    ),
    filterIcon: (filtered) => <SearchOutlined style={{ color: filtered ? '#1890ff' : undefined }} />,
    onFilterDropdownVisibleChange: (visible) => {
      if (visible) {
        setTimeout(() => document.getElementById('search-input').select(), 100);
      }
    },
    render: (text) => (searchText ? <span>{text}</span> : text),
  });

  return (
    <div>
      <Search
        id="search-input"
        placeholder="Search"
        allowClear
        enterButton
        value={searchText}
        onChange={(e) => setSearchText(e.target.value)}
      />
      <Table dataSource={data} rowKey="key">
        <Column
          title="Game"
          dataIndex="game"
          key="game"
          {...getColumnSearchProps('game')}
        />
        <Column
          title="Console"
          dataIndex="console"
          key="console"
          {...getColumnSearchProps('console')}
        />
        <Column
          title="Publisher"
          dataIndex="publisher"
          key="publisher"
          {...getColumnSearchProps('publisher')}
        />
        <Column
          title="Release Date"
          dataIndex="releaseDate"
          key="releaseDate"
          {...getColumnSearchProps('releaseDate')}
        />
        <Column
          title="Last"
          dataIndex="last"
          key="last"
          {...getColumnSearchProps('last')}
        />
        <Column
          title="Score"
          dataIndex="score"
          key="score"
          sorter={(a, b) => a.score - b.score}
        />
        <Column
          title="NA Revenue"
          dataIndex="naRevenue"
          key="naRevenue"
          sorter={(a, b) => a.naRevenue - b.naRevenue}
        />
        <Column
          title="JP Revenue"
          dataIndex="jpRevenue"
          key="jpRevenue"
          sorter={(a, b) => a.jpRevenue - b.jpRevenue}
        />
        <Column
          title="EU Revenue"
          dataIndex="euRevenue"
          key="euRevenue"
          sorter={(a, b) => a.euRevenue - b.euRevenue}
        />
        <Column
          title="Revenue Prediction" 
          dataIndex="totalRevenue"
          key="totalRevenue"
          sorter={(a, b) => a.totalRevenue - b.totalRevenue}
          render={(text) => <span style={{ color: 'blue' }}>{text}</span>}
        />
      </Table>
    </div>
  );
};

export default Home;
