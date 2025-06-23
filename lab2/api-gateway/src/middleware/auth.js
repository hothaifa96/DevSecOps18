const auth = (req, res, next) => {
    // Simple auth middleware for demonstration
    const token = req.header('Authorization');
    
    if (!token && process.env.NODE_ENV === 'production') {
      return res.status(401).json({ error: 'Access denied. No token provided.' });
    }
    
    // In production, verify JWT token here
    req.user = { id: 1, name: 'Demo User' };
    next();
  };
  
  module.exports = auth;