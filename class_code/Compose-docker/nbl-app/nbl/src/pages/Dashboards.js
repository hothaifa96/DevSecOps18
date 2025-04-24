import React from "react";
import {
  LineChart,
  Line,
  AreaChart,
  Area,
  BarChart,
  Bar,
  PieChart,
  Pie,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";
import BandwidthMeter from "../components/BandwidthMeter";
import DeviceUsageCard from "../components/DeviceUsageCard";
import AlertBox from "../components/AlertBox";
import "../styles/Dashboard.css";

const Dashboard = ({ networkData }) => {
  const { currentUsage, historicalData, topDevices, alerts } = networkData;

  return (
    <div className='dashboard'>
      <h1>Network Bandwidth Dashboard</h1>

      <div className='dashboard-summary'>
        <div className='summary-card'>
          <h3>Current Upload</h3>
          <BandwidthMeter
            value={currentUsage.upload}
            max={currentUsage.maxUpload}
          />
          <p>{(currentUsage.upload / 1024 / 1024).toFixed(2)} Mbps</p>
        </div>
        <div className='summary-card'>
          <h3>Current Download</h3>
          <BandwidthMeter
            value={currentUsage.download}
            max={currentUsage.maxDownload}
          />
          <p>{(currentUsage.download / 1024 / 1024).toFixed(2)} Mbps</p>
        </div>
        <div className='summary-card'>
          <h3>Daily Usage</h3>
          <p>{(currentUsage.dailyTotal / 1024 / 1024 / 1024).toFixed(2)} GB</p>
        </div>
        <div className='summary-card'>
          <h3>Monthly Usage</h3>
          <p>
            {(currentUsage.monthlyTotal / 1024 / 1024 / 1024).toFixed(2)} GB
          </p>
          <p className='limit-info'>
            of {currentUsage.monthlyLimit / 1024 / 1024 / 1024} GB limit
          </p>
        </div>
      </div>

      <div className='dashboard-charts'>
        <div className='chart-container'>
          <h3>Bandwidth Usage (Last 24 Hours)</h3>
          <ResponsiveContainer width='100%' height={300}>
            <AreaChart data={historicalData.hourly}>
              <CartesianGrid strokeDasharray='3 3' />
              <XAxis dataKey='time' />
              <YAxis />
              <Tooltip />
              <Legend />
              <Area
                type='monotone'
                dataKey='download'
                stroke='#8884d8'
                fill='#8884d8'
                name='Download'
              />
              <Area
                type='monotone'
                dataKey='upload'
                stroke='#82ca9d'
                fill='#82ca9d'
                name='Upload'
              />
            </AreaChart>
          </ResponsiveContainer>
        </div>

        <div className='chart-container'>
          <h3>Top Bandwidth Consumers</h3>
          <ResponsiveContainer width='100%' height={300}>
            <PieChart>
              <Pie
                data={topDevices}
                cx='50%'
                cy='50%'
                labelLine={false}
                label={({ name, percent }) =>
                  `${name}: ${(percent * 100).toFixed(0)}%`
                }
                outerRadius={100}
                fill='#8884d8'
                dataKey='usage'
              />
              <Tooltip
                formatter={(value) =>
                  `${(value / 1024 / 1024 / 1024).toFixed(2)} GB`
                }
              />
            </PieChart>
          </ResponsiveContainer>
        </div>
      </div>

      <div className='dashboard-devices'>
        <h3>Top Devices</h3>
        <div className='device-grid'>
          {topDevices.slice(0, 4).map((device, index) => (
            <DeviceUsageCard key={index} device={device} />
          ))}
        </div>
      </div>

      {alerts.length > 0 && (
        <div className='dashboard-alerts'>
          <h3>Alerts</h3>
          {alerts.map((alert, index) => (
            <AlertBox key={index} alert={alert} />
          ))}
        </div>
      )}
    </div>
  );
};

export default Dashboard;
