import React, { useState } from 'react';
import { Select, Button, Divider } from 'antd';
import Chart from 'chart.js/auto';

const { Option } = Select;

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

const Comparison = () => {
  const [game1, setGame1] = useState('');
  const [game2, setGame2] = useState('');
  const [chart, setChart] = useState(null);
  const [comparisonData, setComparisonData] = useState(null);

  const handleCompare = () => {
    if (game1 === '' || game2 === '') {
      alert('Please select two games to compare.');
      return;
    }

    const game1Data = data.find((game) => game.game === game1);
    const game2Data = data.find((game) => game.game === game2);

    const ctx = document.getElementById('comparisonChart').getContext('2d');

    if (chart !== null) {
      chart.destroy();
    }

    const newChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Score', 'NA Revenue', 'JP Revenue', 'EU Revenue', 'Total Revenue'],
        datasets: [
          {
            label: game1,
            backgroundColor: 'rgba(75,192,192,0.4)',
            borderColor: 'rgba(75,192,192,1)',
            borderWidth: 1,
            hoverBackgroundColor: 'rgba(75,192,192,0.6)',
            hoverBorderColor: 'rgba(75,192,192,1)',
            data: [
              game1Data.score,
              game1Data.naRevenue,
              game1Data.jpRevenue,
              game1Data.euRevenue,
              game1Data.totalRevenue,
            ],
          },
          {
            label: game2,
            backgroundColor: 'rgba(255,99,132,0.4)',
            borderColor: 'rgba(255,99,132,1)',
            borderWidth: 1,
            hoverBackgroundColor: 'rgba(255,99,132,0.6)',
            hoverBorderColor: 'rgba(255,99,132,1)',
            data: [
              game2Data.score,
              game2Data.naRevenue,
              game2Data.jpRevenue,
              game2Data.euRevenue,
              game2Data.totalRevenue,
            ],
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    });

    const comparison = {
      score: `${Math.round((game1Data.score / game2Data.score) * 100)}%`,
      naRevenue: `${Math.round((game1Data.naRevenue / game2Data.naRevenue) * 100)}%`,
      jpRevenue: `${Math.round((game1Data.jpRevenue / game2Data.jpRevenue) * 100)}%`,
      euRevenue: `${Math.round((game1Data.euRevenue / game2Data.euRevenue) * 100)}%`,
      totalRevenue: `${Math.round((game1Data.totalRevenue / game2Data.totalRevenue) * 100)}%`,
    };

    setComparisonData(comparison);
    setChart(newChart);
  };

  const handleSwap = () => {
    setGame1(game2);
    setGame2(game1);
  };

  return (
    <div className="flex flex-col items-center">
      <div className="flex mt-4">
        <Select className="w-40" onChange={(value) => setGame1(value)} value={game1}>
          {data.map((game) => (
            <Option key={game.key} value={game.game}>
              {game.game}
            </Option>
          ))}
        </Select>
        <Select className="w-40 ml-4" onChange={(value) => setGame2(value)} value={game2}>
          {data.map((game) => (
            <Option key={game.key} value={game.game}>
              {game.game}
            </Option>
          ))}
        </Select>
        <Button className="ml-4" type="primary" onClick={handleCompare}>
          Compare
        </Button>
        <Button className="ml-4" onClick={handleSwap}>
          Swap
        </Button>
      </div>
      <Divider className="w-80 mt-4" />
      {comparisonData && (
        <table className="table-auto border-collapse w-full mt-4">
          <thead>
            <tr className="bg-gray-200">
              <th className="border px-4 py-2">Parameter</th>
              <th className="border px-4 py-2">{game1}</th>
              <th className="border px-4 py-2">{game2}</th>
            </tr>
          </thead>
          <tbody>
            {Object.keys(comparisonData).map((key) => (
              <tr key={key} className="border">
                <td className="border px-4 py-2">{key}</td>
                <td className="border px-4 py-2">{comparisonData[key]}</td>
                <td className="border px-4 py-2">100%</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
      <canvas id="comparisonChart" className="w-full mt-4" style={{ maxHeight: '400px' }}></canvas>
    </div>
  );
};

export default Comparison;
