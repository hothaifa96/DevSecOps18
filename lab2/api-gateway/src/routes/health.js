const express = require('express');
const router = express.Router();
const userService = require('../services/userService');
const inventoryService = require('../services/inventoryService');

router.get('/', async (req, res) => {
  try {
    const health = {
      status: 'healthy',
      timestamp: new Date().toISOString(),
      version: '1.0.0',
      services: {}
    };

    // Check user service health
    try {
      await userService.healthCheck();
      health.services.userService = 'healthy';
    } catch (error) {
      health.services.userService = 'unhealthy';
      health.status = 'degraded';
    }

    // Check inventory service health
    try {
      await inventoryService.healthCheck();
      health.services.inventoryService = 'healthy';
    } catch (error) {
      health.services.inventoryService = 'unhealthy';
      health.status = 'degraded';
    }

    const statusCode = health.status === 'healthy' ? 200 : 503;
    res.status(statusCode).json(health);
  } catch (error) {
    res.status(500).json({
      status: 'unhealthy',
      error: error.message,
      timestamp: new Date().toISOString()
    });
  }
});

module.exports = router;