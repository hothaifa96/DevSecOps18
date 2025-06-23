const httpClient = require('../utils/httpClient');

const USER_SERVICE_URL = process.env.USER_SERVICE_URL || 'http://localhost:5002';

const userService = {
  async getUsers() {
    try {
      const response = await httpClient.get(`${USER_SERVICE_URL}/users`);
      return response.data;
    } catch (error) {
      console.error('User service error:', error.message);
      throw error;
    }
  },

  async createUser(userData) {
    try {
      const response = await httpClient.post(`${USER_SERVICE_URL}/users`, userData);
      return response.data;
    } catch (error) {
      console.error('User service error:', error.message);
      throw error;
    }
  },

  async getUserById(id) {
    try {
      const response = await httpClient.get(`${USER_SERVICE_URL}/users/${id}`);
      return response.data;
    } catch (error) {
      if (error.response && error.response.status === 404) {
        return null;
      }
      console.error('User service error:', error.message);
      throw error;
    }
  },

  async updateUser(id, userData) {
    try {
      const response = await httpClient.put(`${USER_SERVICE_URL}/users/${id}`, userData);
      return response.data;
    } catch (error) {
      if (error.response && error.response.status === 404) {
        return null;
      }
      console.error('User service error:', error.message);
      throw error;
    }
  },

  async deleteUser(id) {
    try {
      await httpClient.delete(`${USER_SERVICE_URL}/users/${id}`);
      return true;
    } catch (error) {
      if (error.response && error.response.status === 404) {
        return false;
      }
      console.error('User service error:', error.message);
      throw error;
    }
  },

  async healthCheck() {
    try {
      await httpClient.get(`${USER_SERVICE_URL}/health`);
      return true;
    } catch (error) {
      throw new Error('User service is not healthy');
    }
  }
};

module.exports = userService;