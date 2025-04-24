import socket
import os
import platform
import subprocess
import re
import math

def format_bytes(bytes, precision=2):
    """
    Format bytes to human-readable format.
    
    Args:
        bytes: Number of bytes
        precision: Number of decimal places
        
    Returns:
        Formatted string (e.g., "1.23 MB")
    """
    if bytes == 0:
        return "0 B"
        
    size_names = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(bytes, 1024)))
    p = math.pow(1024, i)
    s = round(bytes / p, precision)
    
    return f"{s} {size_names[i]}"

def get_public_ip():
    """
    Get the public IP address of the current machine.
    In a real application, this would make an external API call.
    """
    try:
        # This would make an external API call in a real application
        # For this demo, we'll return a mock IP
        return "203.0.113.42"  # Example IP from TEST-NET-3 block
    except:
        return None

def ping(host):
    """
    Ping a host to check if it's reachable.
    
    Args:
        host: The hostname or IP address to ping
        
    Returns:
        A dictionary with ping results
    """
    try:
        # Determine the OS-specific ping command
        if platform.system().lower() == "windows":
            ping_cmd = ["ping", "-n", "4", host]
        else:
            ping_cmd = ["ping", "-c", "4", host]
            
        # Execute the ping command
        output = subprocess.check_output(ping_cmd).decode('utf-8')
        
        # Parse the output
        if platform.system().lower() == "windows":
            pattern = r"Minimum = (\d+)ms, Maximum = (\d+)ms, Average = (\d+)ms"
            match = re.search(pattern, output)
            if match:
                min_time, max_time, avg_time = map(int, match.groups())
            else:
                min_time = max_time = avg_time = None
        else:
            pattern = r"min/avg/max/mdev = ([\d.]+)/([\d.]+)/([\d.]+)/([\d.]+) ms"
            match = re.search(pattern, output)
            if match:
                min_time, avg_time, max_time, _ = map(float, match.groups())
            else:
                min_time = max_time = avg_time = None
                
        # Count the number of successful pings
        if platform.system().lower() == "windows":
            received = output.count("Reply from")
        else:
            match = re.search(r"(\d+) received", output)
            received = int(match.group(1)) if match else 0
            
        return {
            'host': host,
            'success': received > 0,
            'packets_sent': 4,
            'packets_received': received,
            'min_time': min_time,
            'max_time': max_time,
            'avg_time': avg_time
        }
    except:
        # If there's an error, assume the host is unreachable
        return {
            'host': host,
            'success': False,
            'packets_sent': 4,
            'packets_received': 0,
            'min_time': None,
            'max_time': None,
            'avg_time': None
        }

def traceroute(host):
    """
    Perform a traceroute to the specified host.
    
    Args:
        host: The hostname or IP address
        
    Returns:
        A list of hops
    """
    try:
        # Determine the OS-specific traceroute command
        if platform.system().lower() == "windows":
            cmd = ["tracert", host]
        else:
            cmd = ["traceroute", host]
            
        # Execute the command
        output = subprocess.check_output(cmd).decode('utf-8')
        
        # Parse the output
        hops = []
        lines = output.split('\n')
        
        # Skip the first line (header)
        for line in lines[1:]:
            # Parse the hop information
            # This is a simple implementation and may need to be adjusted
            if platform.system().lower() == "windows":
                match = re.search(r"^\s*(\d+)\s+(\d+)\s+ms\s+(\d+)\s+ms\s+(\d+)\s+ms\s+([\w\.-]+|\*)", line)
                if match:
                    hop_num, time1, time2, time3, host = match.groups()
                    hops.append({
                        'hop': int(hop_num),
                        'host': host,
                        'times': [int(time1), int(time2), int(time3)]
                    })
            else:
                match = re.search(r"^\s*(\d+)\s+([\w\.-]+|\*)\s+\(([\d\.]+)\)\s+(\d+\.\d+)\s+ms\s+(\d+\.\d+)\s+ms\s+(\d+\.\d+)\s+ms", line)
                if match:
                    hop_num, host_name, host_ip, time1, time2, time3 = match.groups()
                    hops.append({
                        'hop': int(hop_num),
                        'host': host_name,
                        'ip': host_ip,
                        'times': [float(time1), float(time2), float(time3)]
                    })
        
        return hops
    except:
        # If there's an error, return an empty list
        return []