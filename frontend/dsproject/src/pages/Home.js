import React, { useEffect, useState } from 'react';
import { Table, Input } from 'antd';
import { SearchOutlined } from '@ant-design/icons';
import scrapedData from '../service/scrapedData';

const { Column } = Table;
const { Search } = Input;

const Home = () => {
  const [searchText, setSearchText] = useState('');
  const [resRows, setResRows] = useState() 
  const [pagination, setPagination] = useState({
    current: 1,
    pageSize: 10,
    total: 0,
  })
  async function fetchData(searchText, page){
    const respond = await scrapedData.get(searchText,page)
    console.log(respond);
    setResRows(respond.results.map((row)=>{return{
      key: row.Title+row.Console,
      game: row.Title,
    console: row.Console,
    publisher: row.Publisher,
    releaseDate: row['Release Year']+'-'+row['Release Month'],
    // last: '2023-02-01',
    // score: 100,
    naRevenue: row['NA Sales (m)'],
    jpRevenue: row['JP Sales (m)'],
    euRevenue: row['EU Sales (m)'],
    totalRevenue: row['Total Sales (m)'],
    }}))
    setPagination({...pagination, total: respond.count,current:page})
  }
  const handleSearch = async (value) => {
    setSearchText(value);
    fetchData(value, 1)
  };

  const sorterDate = (a, b) => {
    const dateA = new Date(a);
    const dateB = new Date(b);
    return dateA - dateB;
  };
  
  useEffect(()=>{
    fetchData('',1)},[])

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
      <Table dataSource={resRows} rowKey="key" pagination={pagination} onChange={(pagi)=>{
        fetchData(searchText,pagi.current)
      }}>
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
        {/* <Column
          title="Last Update"
          dataIndex="last"
          key="last"
          sorter={(a, b) => sorterDate(a.last, b.last)}
        /> */}
        {/* <Column
          title="Score"
          dataIndex="score"
          key="score"
          sorter={(a, b) => a.score - b.score}
        /> */}
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
