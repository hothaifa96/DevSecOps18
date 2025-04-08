import socket
import subprocess
import platform
import re
import random
from datetime import datetime, timedelta

def get_connected_devices():
    """
    In a real application, this would scan the network for connected devices.
    For this demo, we'll return mock data.
    """
    # Mock device data
    devices = [
        {'name': 'Gaming PC', 'mac': '00:1A:2B:3C:4D:5E', 'ip': '192.168.1.100', 'type': 'computer'},
        {'name': 'Smart TV', 'mac': '11:2A:3B:4C:5D:6E', 'ip': '192.168.1.101', 'type': 'entertainment'},
        {'name': 'iPhone', 'mac': '22:3A:4B:5C:6D:7E', 'ip': '192.168.1.102', 'type': 'mobile'},
        {'name': 'Work Laptop', 'mac': '33:4A:5B:6C:7D:8E', 'ip': '192.168.1.103', 'type': 'computer'},
        {'name': 'IoT Hub', 'mac': '44:5A:6B:7C:8D:9E', 'ip': '192.168.1.104', 'type': 'iot'},
    ]
    
    # Add randomly generated devices to simulate network changes
    if random.random() > 0.7:  # 30% chance to add a new device
        new_device_types = ['mobile', 'iot', 'computer', 'entertainment']
        new_device_type = random.choice(new_device_types)
        
        if new_device_type == 'mobile':
            names = ['Android Phone', 'iPad', 'Google Pixel']
        elif new_device_type == 'iot':
            names = ['Smart Speaker', 'Security Camera', 'Smart Thermostat']
        elif new_device_type == 'computer':
            names = ['Linux Server', 'MacBook', 'Desktop PC']
        else:
            names = ['Apple TV', 'Roku', 'Chromecast']
            
        new_device = {
            'name': random.choice(names),
            'mac': ':'.join(['%02x' % random.randint(0, 255) for _ in range(6)]),
            'ip': f'192.168.1.{random.randint(105, 254)}',
            'type': new_device_type
        }
        
        devices.append(new_device)
    
    return devices

def detect_device_type(mac_address):
    """
    Determine the type of device based on the MAC address.
    In a real application, this would use OUI (Organizationally Unique Identifier) lookup.
    For this demo, we'll return random device types.
    """
    device_types = ['computer', 'mobile', 'entertainment', 'iot']
    return random.choice(device_types)

def scan_network():
    """
    Scan the local network for devices.
    In a real application, this would use nmap or similar tools.
    """
    try:
        # Get local network information
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        
        # In a real application, we would scan the network here
        # For this demo, we just return mock data
        connected_devices = get_connected_devices()
        
        return connected_devices
    except Exception as e:
        print(f"Error scanning network: {e}")
        return []

def update_device_status(device_id, status):
    """
    Update the status of a device in the database.
    In a real application, this would update the database.
    
    Args:
        device_id: The ID of the device to update
        status: The new status (e.g., 'online', 'offline')
        
    Returns:
        True if successful, False otherwise
    """
    # In a real application, this would update the database
    return True

def get_device_data():
    """
    Get data about connected devices.
    In a real application, this would query the database and the network.
    """
    return get_connected_devices()