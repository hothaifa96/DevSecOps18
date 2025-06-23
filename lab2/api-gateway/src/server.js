const app = require('./src/app');
const PORT = process.env.PORT || 5001;

app.listen(PORT, '0.0.0.0', () => {
  console.log(`🎩 PeakyBlinders API Gateway is running on port ${PORT}`);
  console.log(`Environment: ${process.env.NODE_ENV || 'development'}`);
  console.log(`User Service URL: ${process.env.USER_SERVICE_URL || 'http://localhost:5002'}`);
  console.log(`Inventory Service URL: ${process.env.INVENTORY_SERVICE_URL || 'http://localhost:5003'}`);
});