import { PieChartOutlined } from '@ant-design/icons';
import { Pie } from 'react-chartjs-2';

const data = {
  labels: ['NA', 'JP', 'EU'],
  datasets: [
    {
      data: [100, 80, 120],
      backgroundColor: ['#FF4500', '#4169E1', '#32CD32'],
    },
  ],
};

const PieChartComponent = () => {
  const totalRevenue = data.datasets[0].data.reduce((total, value) => total + value, 0);
  const highestRegionIndex = data.datasets[0].data.indexOf(Math.max(...data.datasets[0].data));
  const highestRegion = data.labels[highestRegionIndex];

  const comment = {
    region: highestRegion,
    reason: `Vì khu vực ${highestRegion} có doanh thu cao nhất, chiếm ${(data.datasets[0].data[highestRegionIndex] / totalRevenue * 100).toFixed(2)}% tổng doanh thu.`,
  };

  return (
    <div className="flex justify-center items-center h-screen">
      <div className="w-full max-w-md bg-white shadow-md rounded-lg p-6">
        <div className="text-center">
          <h1 className="text-xl font-bold mb-4">Revenue by Regions:</h1>
          <PieChartOutlined style={{ fontSize: '48px', color: '#1890ff' }} />
        </div>
        <div className="mt-6">
          <Pie data={data} />
        </div>
        <div className="mt-6 text-center">
          <h2 className="text-lg font-semibold">Data Analysis:</h2>
          <p className="mt-2 text-sm">{`Khu vực có doanh thu cao nhất là ${comment.region}. ${comment.reason}`}</p>
        </div>
      </div>
    </div>
  );
};

export default PieChartComponent;
