const inventoryService = require('../services/inventoryService');

const inventoryController = {
  async getInventory(req, res) {
    try {
      const inventory = await inventoryService.getInventory();
      res.json(inventory);
    } catch (error) {
      console.error('Error fetching inventory:', error);
      res.status(500).json({ error: 'Failed to fetch inventory' });
    }
  },

  async createInventoryItem(req, res) {
    try {
      const item = await inventoryService.createInventoryItem(req.body);
      res.status(201).json(item);
    } catch (error) {
      console.error('Error creating inventory item:', error);
      res.status(500).json({ error: 'Failed to create inventory item' });
    }
  },

  async getInventoryItemById(req, res) {
    try {
      const item = await inventoryService.getInventoryItemById(req.params.id);
      if (!item) {
        return res.status(404).json({ error: 'Inventory item not found' });
      }
      res.json(item);
    } catch (error) {
      console.error('Error fetching inventory item:', error);
      res.status(500).json({ error: 'Failed to fetch inventory item' });
    }
  },

  async updateInventoryItem(req, res) {
    try {
      const item = await inventoryService.updateInventoryItem(req.params.id, req.body);
      if (!item) {
        return res.status(404).json({ error: 'Inventory item not found' });
      }
      res.json(item);
    } catch (error) {
      console.error('Error updating inventory item:', error);
      res.status(500).json({ error: 'Failed to update inventory item' });
    }
  },

  async deleteInventoryItem(req, res) {
    try {
      const success = await inventoryService.deleteInventoryItem(req.params.id);
      if (!success) {
        return res.status(404).json({ error: 'Inventory item not found' });
      }
      res.status(204).send();
    } catch (error) {
      console.error('Error deleting inventory item:', error);
      res.status(500).json({ error: 'Failed to delete inventory item' });
    }
  }
};

module.exports = inventoryController;