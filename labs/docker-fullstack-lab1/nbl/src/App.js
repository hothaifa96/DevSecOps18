import React, { useState, useEffect } from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link,
  useParams,
  useLocation,
} from "react-router-dom";
import {
  LineChart,
  Line,
  AreaChart,
  Area,
  PieChart,
  Pie,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";
import axios from "axios";
import './App.css'

function App() {
  return (
    <Router>
      <div className='app'>
        <Navbar />
        <main className='content'>
          <Routes>
            <Route path='/' element={<Dashboard />} />
            <Route path='/devices' element={<DeviceList />} />
            <Route path='/devices/:deviceId' element={<DeviceDetails />} />
            <Route path='/reports' element={<Reports />} />
          </Routes>
        </main>
        <footer className='footer'>
          <p>&copy; {new Date().getFullYear()} Network Bandwidth Logger</p>
        </footer>
      </div>
    </Router>
  );
}

// Navbar Component
function Navbar() {
  const location = useLocation();

  return (
    <nav className='navbar'>
      <div className='navbar-container'>
        <Link to='/' className='navbar-logo'>
          <span className='logo-icon'>📊</span>
          <span className='logo-text'>NetBL</span>
        </Link>

        <ul className='navbar-menu'>
          <li className='navbar-item'>
            <Link
              to='/'
              className={
                location.pathname === "/" ? "navbar-link active" : "navbar-link"
              }
            >
              Dashboard
            </Link>
          </li>
          <li className='navbar-item'>
            <Link
              to='/devices'
              className={
                location.pathname.includes("/devices")
                  ? "navbar-link active"
                  : "navbar-link"
              }
            >
              Devices
            </Link>
          </li>
          <li className='navbar-item'>
            <Link
              to='/reports'
              className={
                location.pathname === "/reports"
                  ? "navbar-link active"
                  : "navbar-link"
              }
            >
              Reports
            </Link>
          </li>
        </ul>
      </div>
    </nav>
  );
}

// Dashboard Page
function Dashboard() {
  const [networkData, setNetworkData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const API_URL =
          process.env.REACT_APP_API_URL || "http://localhost:5002/api";
        const response = await axios.get(`${API_URL}/stats/summary`);
        setNetworkData(response.data);
        setError(null);
      } catch (err) {
        console.error("Error fetching network data:", err);
        setError("Failed to load network data. Please try again later.");
      } finally {
        setLoading(false);
      }
    };

    fetchData();
    // Set up polling for real-time updates
    const interval = setInterval(fetchData, 30000); // Refresh every 30 seconds
    return () => clearInterval(interval);
  }, []);

  if (loading) {
    return <div className='loading'>Loading dashboard data...</div>;
  }

  if (error) {
    return <div className='error'>{error}</div>;
  }

  if (!networkData) {
    return <div className='error'>No network data available</div>;
  }

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
          <p>{formatBytes(currentUsage.upload)}/s</p>
        </div>
        <div className='summary-card'>
          <h3>Current Download</h3>
          <BandwidthMeter
            value={currentUsage.download}
            max={currentUsage.maxDownload}
          />
          <p>{formatBytes(currentUsage.download)}/s</p>
        </div>
        <div className='summary-card'>
          <h3>Daily Usage</h3>
          <p>{formatBytes(currentUsage.dailyTotal)}</p>
        </div>
        <div className='summary-card'>
          <h3>Monthly Usage</h3>
          <p>{formatBytes(currentUsage.monthlyTotal)}</p>
          <p className='limit-info'>
            of {formatBytes(currentUsage.monthlyLimit)} limit
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
              <YAxis tickFormatter={(value) => formatBytes(value)} />
              <Tooltip formatter={(value) => formatBytes(value)} />
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
                nameKey='name'
              />
              <Tooltip formatter={(value) => formatBytes(value)} />
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
}

// Device List Page
function DeviceList() {
  const [devices, setDevices] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchDevices = async () => {
      try {
        setLoading(true);
        const API_URL =
          process.env.REACT_APP_API_URL || "http://localhost:5002/api";
        const response = await axios.get(`${API_URL}/devices`);
        setDevices(response.data);
        setError(null);
      } catch (err) {
        console.error("Error fetching devices:", err);
        setError("Failed to load devices. Please try again later.");
      } finally {
        setLoading(false);
      }
    };

    fetchDevices();
  }, []);

  if (loading) {
    return <div className='loading'>Loading devices...</div>;
  }

  if (error) {
    return <div className='error'>{error}</div>;
  }

  return (
    <div className='device-list'>
      <h1>Network Devices</h1>

      <div className='device-list-container'>
        <table className='device-table'>
          <thead>
            <tr>
              <th>Name</th>
              <th>IP Address</th>
              <th>Device Type</th>
              <th>Monthly Usage</th>
              <th>Last Seen</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {devices.map((device) => (
              <tr key={device.id}>
                <td>{device.name}</td>
                <td>{device.ip}</td>
                <td>
                  <span className={`device-type device-type-${device.type}`}>
                    {device.type}
                  </span>
                </td>
                <td>
                  {formatBytes(device.month_download + device.month_upload)}
                </td>
                <td>{formatDate(device.last_seen)}</td>
                <td>
                  <Link to={`/devices/${device.id}`} className='button'>
                    Details
                  </Link>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

// Device Details Page
function DeviceDetails() {
  const { deviceId } = useParams();
  const [deviceData, setDeviceData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchDeviceDetails = async () => {
      try {
        setLoading(true);
        const API_URL =
          process.env.REACT_APP_API_URL || "http://localhost:5002/api";
        const response = await axios.get(`${API_URL}/devices/${deviceId}`);
        setDeviceData(response.data);
        setError(null);
      } catch (err) {
        console.error("Error fetching device details:", err);
        setError("Failed to load device details. Please try again later.");
      } finally {
        setLoading(false);
      }
    };

    fetchDeviceDetails();
  }, [deviceId]);

  if (loading) {
    return <div className='loading'>Loading device details...</div>;
  }

  if (error) {
    return <div className='error'>{error}</div>;
  }

  if (!deviceData) {
    return <div className='error'>Device not found</div>;
  }

  const { device, usage, alerts } = deviceData;

  return (
    <div className='device-details'>
      <div className='device-header'>
        <h1>{device.name}</h1>
        <Link to='/devices' className='button button-secondary'>
          Back to Devices
        </Link>
      </div>

      <div className='device-info card'>
        <h2>Device Information</h2>
        <div className='info-grid'>
          <div className='info-item'>
            <span className='info-label'>MAC Address:</span>
            <span className='info-value'>{device.mac}</span>
          </div>
          <div className='info-item'>
            <span className='info-label'>IP Address:</span>
            <span className='info-value'>{device.ip}</span>
          </div>
          <div className='info-item'>
            <span className='info-label'>Device Type:</span>
            <span className='info-value'>{device.type}</span>
          </div>
          <div className='info-item'>
            <span className='info-label'>First Seen:</span>
            <span className='info-value'>{formatDate(device.first_seen)}</span>
          </div>
          <div className='info-item'>
            <span className='info-label'>Last Seen:</span>
            <span className='info-value'>{formatDate(device.last_seen)}</span>
          </div>
        </div>
      </div>

      <div className='device-usage card'>
        <h2>Usage History</h2>
        <ResponsiveContainer width='100%' height={300}>
          <BarChart data={usage}>
            <CartesianGrid strokeDasharray='3 3' />
            <XAxis dataKey='date' />
            <YAxis tickFormatter={(value) => formatBytes(value)} />
            <Tooltip formatter={(value) => formatBytes(value)} />
            <Legend />
            <Bar
              dataKey='download'
              stackId='a'
              fill='#8884d8'
              name='Download'
            />
            <Bar dataKey='upload' stackId='a' fill='#82ca9d' name='Upload' />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {alerts.length > 0 && (
        <div className='device-alerts card'>
          <h2>Device Alerts</h2>
          {alerts.map((alert, index) => (
            <AlertBox key={index} alert={alert} />
          ))}
        </div>
      )}
    </div>
  );
}

// Reports Page
function Reports() {
  const [period, setPeriod] = useState("daily");
  const [reportData, setReportData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchReportData = async () => {
      try {
        setLoading(true);
        const API_URL =
          process.env.REACT_APP_API_URL || "http://localhost:5002/api";
        const response = await axios.get(`${API_URL}/reports/usage/${period}`);
        setReportData(response.data);
        setError(null);
      } catch (err) {
        console.error("Error fetching report data:", err);
        setError("Failed to load report data. Please try again later.");
      } finally {
        setLoading(false);
      }
    };

    fetchReportData();
  }, [period]);

  const handlePeriodChange = (newPeriod) => {
    setPeriod(newPeriod);
  };

  if (loading) {
    return <div className='loading'>Loading report data...</div>;
  }

  if (error) {
    return <div className='error'>{error}</div>;
  }

  if (!reportData) {
    return <div className='error'>No report data available</div>;
  }

  return (
    <div className='reports'>
      <h1>Network Usage Reports</h1>

      <div className='period-selector'>
        <button
          className={period === "daily" ? "button active" : "button"}
          onClick={() => handlePeriodChange("daily")}
        >
          Daily
        </button>
        <button
          className={period === "weekly" ? "button active" : "button"}
          onClick={() => handlePeriodChange("weekly")}
        >
          Weekly
        </button>
        <button
          className={period === "monthly" ? "button active" : "button"}
          onClick={() => handlePeriodChange("monthly")}
        >
          Monthly
        </button>
      </div>

      <div className='report-chart card'>
        <h2>
          {period === "daily" && "Last 24 Hours"}
          {period === "weekly" && "Last 7 Days"}
          {period === "monthly" && "Last 30 Days"}
        </h2>
        <ResponsiveContainer width='100%' height={400}>
          <AreaChart data={reportData.data}>
            <CartesianGrid strokeDasharray='3 3' />
            <XAxis dataKey='date' />
            <YAxis tickFormatter={(value) => formatBytes(value)} />
            <Tooltip formatter={(value) => formatBytes(value)} />
            <Legend />
            <Area
              type='monotone'
              dataKey='download'
              stackId='1'
              stroke='#8884d8'
              fill='#8884d8'
              name='Download'
            />
            <Area
              type='monotone'
              dataKey='upload'
              stackId='1'
              stroke='#82ca9d'
              fill='#82ca9d'
              name='Upload'
            />
          </AreaChart>
        </ResponsiveContainer>
      </div>

      <div className='report-summary card'>
        <h2>Summary</h2>
        <div className='summary-grid'>
          <div className='summary-item'>
            <span className='summary-label'>Total Download:</span>
            <span className='summary-value'>
              {formatBytes(
                reportData.data.reduce((sum, item) => sum + item.download, 0)
              )}
            </span>
          </div>
          <div className='summary-item'>
            <span className='summary-label'>Total Upload:</span>
            <span className='summary-value'>
              {formatBytes(
                reportData.data.reduce((sum, item) => sum + item.upload, 0)
              )}
            </span>
          </div>
          <div className='summary-item'>
            <span className='summary-label'>Total Usage:</span>
            <span className='summary-value'>
              {formatBytes(
                reportData.data.reduce(
                  (sum, item) => sum + item.download + item.upload,
                  0
                )
              )}
            </span>
          </div>
          <div className='summary-item'>
            <span className='summary-label'>Average Daily Usage:</span>
            <span className='summary-value'>
              {formatBytes(
                reportData.data.reduce(
                  (sum, item) => sum + item.download + item.upload,
                  0
                ) / reportData.data.length
              )}
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}

// Helper Components
function BandwidthMeter({ value, max }) {
  const percentage = Math.min((value / max) * 100, 100);

  let color = "#2ecc71"; // Green
  if (percentage > 70) color = "#f39c12"; // Orange
  if (percentage > 90) color = "#e74c3c"; // Red

  return (
    <div className='bandwidth-meter'>
      <div className='meter-bar'>
        <div
          className='meter-fill'
          style={{
            width: `${percentage}%`,
            backgroundColor: color,
          }}
        ></div>
      </div>
      <div className='meter-text'>{percentage.toFixed(0)}%</div>
    </div>
  );
}

function DeviceUsageCard({ device }) {
  return (
    <div className='device-card'>
      <div className='device-icon'>
        {device.type === "computer" && "💻"}
        {device.type === "mobile" && "📱"}
        {device.type === "entertainment" && "📺"}
        {device.type === "iot" && "🔌"}
      </div>
      <div className='device-info'>
        <h4>{device.name}</h4>
        <p>{device.ip}</p>
      </div>
      <div className='device-usage'>
        <span className='usage-text'>{formatBytes(device.usage)}</span>
      </div>
      <Link to={`/devices/${device.id}`} className='device-link'>
        Details
      </Link>
    </div>
  );
}

function AlertBox({ alert }) {
  return (
    <div className={`alert-box alert-${alert.severity}`}>
      <div className='alert-icon'>
        {alert.severity === "critical" && "⚠️"}
        {alert.severity === "warning" && "⚠️"}
        {alert.severity === "info" && "ℹ️"}
      </div>
      <div className='alert-content'>
        <h4>
          {alert.type.charAt(0).toUpperCase() + alert.type.slice(1)} Alert
        </h4>
        <p>{alert.message}</p>
        <span className='alert-time'>{formatDate(alert.timestamp)}</span>
      </div>
    </div>
  );
}

// Utility Functions
function formatBytes(bytes, decimals = 2) {
  if (bytes === 0) return "0 Bytes";

  const k = 1024;
  const dm = decimals < 0 ? 0 : decimals;
  const sizes = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"];

  const i = Math.floor(Math.log(bytes) / Math.log(k));

  return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + " " + sizes[i];
}

function formatDate(dateString) {
  if (!dateString) return "N/A";

  const date = new Date(dateString);
  return new Intl.DateTimeFormat("en-US", {
    year: "numeric",
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  }).format(date);
}

export default App;
