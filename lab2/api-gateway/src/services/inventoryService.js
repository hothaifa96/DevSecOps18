const httpClient = require('../utils/httpClient');

const INVENTORY_SERVICE_URL = process.env.INVENTORY_SERVICE_URL || 'http://localhost:5003';

const inventoryService = {
  async getInventory() {
    try {
      const response = await httpClient.get(`${INVENTORY_SERVICE_URL}/inventory`);
      return response.data;
    } catch (error) {
      console.error('Inventory service error:', error.message);
      throw error;
    }
  },

  async createInventoryItem(itemData) {
    try {
      const response = await httpClient.post(`${INVENTORY_SERVICE_URL}/inventory`, itemData);
      return response.data;
    } catch (error) {
      console.error('Inventory service error:', error.message);
      throw error;
    }
  },

  async getInventoryItemById(id) {
    try {
      const response = await httpClient.get(`${INVENTORY_SERVICE_URL}/inventory/${id}`);
      return response.data;
    } catch (error) {
      if (error.response && error.response.status === 404) {
        return null;
      }
      console.error('Inventory service error:', error.message);
      throw error;
    }
  },

  async updateInventoryItem(id, itemData) {
    try {
      const response = await httpClient.put(`${INVENTORY_SERVICE_URL}/inventory/${id}`, itemData);
      return response.data;
    } catch (error) {
      if (error.response && error.response.status === 404) {
        return null;
      }
      console.error('Inventory service error:', error.message);
      throw error;
    }
  },

  async deleteInventoryItem(id) {
    try {
      await httpClient.delete(`${INVENTORY_SERVICE_URL}/inventory/${id}`);
      return true;
    } catch (error) {
      if (error.response && error.response.status === 404) {
        return false;
      }
      console.error('Inventory service error:', error.message);
      throw error;
    }
  },

  async healthCheck() {
    try {
      await httpClient.get(`${INVENTORY_SERVICE_URL}/actuator/health`);
      return true;
    } catch (error) {
      throw new Error('Inventory service is not healthy');
    }
  }
};

module.exports = inventoryService;