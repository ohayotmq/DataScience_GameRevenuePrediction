import React, { useState } from 'react';
import { Table, Input } from 'antd';
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

  const handleSearch = (value) => {
    setSearchText(value);
  };

  const filteredData = data.filter(
    (item) =>
      item.game.toLowerCase().includes(searchText.toLowerCase()) ||
      item.publisher.toLowerCase().includes(searchText.toLowerCase())
  );
  const sorterDate = (a, b) => {
    const dateA = new Date(a);
    const dateB = new Date(b);
    return dateA - dateB;
  };
  

  return (
    <div>
      <Search
        placeholder="Search"
        allowClear
        enterButton
        value={searchText}
        onChange={(e) => setSearchText(e.target.value)}
        onSearch={handleSearch}
      />
      <Table dataSource={filteredData} rowKey="key">
        <Column
          title="Game"
          dataIndex="game"
          key="game"
        />
        <Column
          title="Console"
          dataIndex="console"
          key="console"
          filters={[
            { text: 'All', value: 'All' },
            { text: 'PC', value: 'PC' },
            { text: 'PS4', value: 'PS4' },
            { text: 'XBOX', value: 'XBOX' },
            { text: 'NINTENDO', value: 'NINTENDO' },
          ]}
          onFilter={(value, record) => record.console.indexOf(value) === 0}
        />
        <Column
          title="Publisher"
          dataIndex="publisher"
          key="publisher"
        />
        <Column
          title="Release Date"
          dataIndex="releaseDate"
          key="releaseDate"
          sorter={(a, b) => sorterDate(a.releaseDate, b.releaseDate)}
        />
        <Column
          title="Last Update"
          dataIndex="last"
          key="last"
          sorter={(a, b) => sorterDate(a.last, b.last)}
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
