import React, { useEffect, useState } from 'react';
import { Pie, Bar, Line } from 'react-chartjs-2';
import { Row, Col, Card } from 'antd';
import { PieChartOutlined, BarChartOutlined, LineChartOutlined } from '@ant-design/icons';
import scrapedData from '../service/scrapedData';

const AnalysisPage = () => {
  const [fetchedData, setFetchedData] = useState([]);

  useEffect(() => {
    async function fetchData() {
      try {
        const respond = await scrapedData.get('', 1);
        setFetchedData(respond.results);
      } catch (error) {
        console.error("Error fetching data: ", error);
      }
    }
    fetchData();
  }, []);

  const platformData = {
    labels: ['PC', 'PS4', 'XBOX', 'NINTENDO'],
    datasets: [
      {
        data: [
          fetchedData.filter(item => item.console === 'PC').length,
          fetchedData.filter(item => item.console === 'PS4').length,
          fetchedData.filter(item => item.console === 'XBOX').length,
          fetchedData.filter(item => item.console === 'NINTENDO').length,
        ],
        backgroundColor: ['#FF4500', '#4169E1', '#32CD32', '#FFD700'],
      },
    ],
  };

  const genreSalesData = {
    labels: ['Action', 'Adventure', 'RPG', 'Strategy'],
    datasets: [
      {
        label: 'Sales by Genre',
        backgroundColor: 'rgba(75,192,192,0.2)',
        borderColor: 'rgba(75,192,192,1)',
        borderWidth: 1,
        hoverBackgroundColor: 'rgba(75,192,192,0.4)',
        hoverBorderColor: 'rgba(75,192,192,1)',
        data: [
          fetchedData.filter(item => item.genre === 'Action').length,
          fetchedData.filter(item => item.genre === 'Adventure').length,
          fetchedData.filter(item => item.genre === 'RPG').length,
          fetchedData.filter(item => item.genre === 'Strategy').length,
        ],
      },
    ],
  };

  const years = ['2019', '2020', '2021', '2022'];
  const genreLabels = [...new Set(fetchedData.map(item => item.genre))];
  const yearlySalesData = {
    labels: years,
    datasets: genreLabels.map(genre => ({
      label: genre,
      fill: false,
      lineTension: 0.1,
      borderColor: '#' + (Math.random().toString(16) + '000000').substring(2,8),
      borderWidth: 2,
      data: years.map(year => fetchedData.filter(item => item.genre === genre && item.releaseYear === year).length),
    })),
  };

  return (
    <div className="container mt-4">
      <Row gutter={16}>
        <Col span={8}>
          <Card title="Revenue by Platform" bordered={false}>
            <Pie data={platformData} />
          </Card>
        </Col>
        <Col span={8}>
          <Card title="Sales by Genre" bordered={false}>
            <Bar data={genreSalesData} />
          </Card>
        </Col>
        <Col span={8}>
          <Card title="Sales by Year and Genre" bordered={false}>
            <Line data={yearlySalesData} />
          </Card>
        </Col>
      </Row>
    </div>
  );
};

export default AnalysisPage;
