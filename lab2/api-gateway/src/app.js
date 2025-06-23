const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');
const compression = require('compression');
const rateLimit = require('express-rate-limit');
require('dotenv').config();

const userRoutes = require('./routes/users');
const inventoryRoutes = require('./routes/inventory');
const healthRoutes = require('./routes/health');
const corsMiddleware = require('./middleware/cors');
const logger = require('./middleware/logger');

const app = express();

// Security middleware
app.use(helmet());

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
  message: 'Too many requests from this IP, please try again later.',
});
app.use(limiter);

// Compression
app.use(compression());

// CORS
app.use(corsMiddleware);

// Logging
app.use(morgan('combined'));
app.use(logger);

// Body parsing
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true, limit: '10mb' }));

// Routes
app.use('/health', healthRoutes);
app.use('/api/users', userRoutes);
app.use('/api/inventory', inventoryRoutes);

// Welcome route
app.get('/', (req, res) => {
  res.json({
    message: '🎩 Welcome to PeakyBlinders Software API Gateway',
    version: '1.0.0',
    services: {
      userService: process.env.USER_SERVICE_URL || 'http://localhost:5002',
      inventoryService: process.env.INVENTORY_SERVICE_URL || 'http://localhost:5003'
    }
  });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error('Error:', err);
  res.status(err.status || 500).json({
    error: err.message || 'Internal Server Error',
    timestamp: new Date().toISOString()
  });
});

// 404 handler
app.use('*', (req, res) => {
  res.status(404).json({
    message: 'Route not found',
    path: req.originalUrl
  });
});

module.exports = app;