from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from datetime import datetime, timedelta
import random
from modules.database import get_db_connection, init_db
from modules.bandwidth_monitor import get_current_bandwidth
from modules.device_tracker import get_connected_devices
from modules.network_utils import format_bytes

app = Flask(__name__)
CORS(app)

# Initialize the database when the app starts
with app.app_context():
    try:
        init_db()
        print("Database initialized successfully!")
    except Exception as e:
        print(f"Error initializing database: {e}")

@app.route('/api/stats/summary', methods=['GET'])
def get_summary():
    """Get a summary of network stats for the dashboard"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Get current bandwidth usage
        current_bandwidth = get_current_bandwidth()
        
        # Get daily and monthly totals
        cursor.execute("""
            SELECT SUM(total_download) + SUM(total_upload) as daily_total
            FROM daily_usage 
            WHERE date = CURRENT_DATE
        """)
        daily_total = cursor.fetchone()[0] or 0
        
        cursor.execute("""
            SELECT SUM(total_download) + SUM(total_upload) as monthly_total
            FROM monthly_usage 
            WHERE year = EXTRACT(YEAR FROM CURRENT_DATE)
            AND month = EXTRACT(MONTH FROM CURRENT_DATE)
        """)
        monthly_total = cursor.fetchone()[0] or 0
        
        # Get historical hourly data for the last 24 hours
        cursor.execute("""
            SELECT 
                date_trunc('hour', timestamp) as hour,
                SUM(download_bytes) as download,
                SUM(upload_bytes) as upload
            FROM bandwidth_data
            WHERE timestamp > NOW() - INTERVAL '24 hours'
            GROUP BY hour
            ORDER BY hour
        """)
        hourly_data = []
        for row in cursor.fetchall():
            hourly_data.append({
                'time': row[0].strftime('%H:%M'),
                'download': row[1],
                'upload': row[2]
            })
            
        # Get top devices by usage
        cursor.execute("""
            SELECT 
                d.id, 
                d.name, 
                d.mac_address, 
                d.ip_address,
                d.device_type,
                SUM(bd.download_bytes) + SUM(bd.upload_bytes) as total_usage
            FROM devices d
            JOIN bandwidth_data bd ON d.id = bd.device_id
            WHERE bd.timestamp > NOW() - INTERVAL '7 days'
            GROUP BY d.id
            ORDER BY total_usage DESC
            LIMIT 5
        """)
        top_devices = []
        for row in cursor.fetchall():
            top_devices.append({
                'id': row[0],
                'name': row[1],
                'mac': row[2],
                'ip': row[3],
                'type': row[4],
                'usage': row[5]
            })
        
        # Get recent alerts
        cursor.execute("""
            SELECT id, timestamp, alert_type, severity, message, device_id
            FROM alerts
            WHERE acknowledged = FALSE
            ORDER BY timestamp DESC
            LIMIT 5
        """)
        alerts = []
        for row in cursor.fetchall():
            alerts.append({
                'id': row[0],
                'timestamp': row[1].isoformat(),
                'type': row[2],
                'severity': row[3],
                'message': row[4],
                'device_id': row[5]
            })
        
        cursor.close()
        conn.close()
        
        # If the database doesn't have enough data yet, supplement with mock data
        if not hourly_data:
            now = datetime.now()
            for i in range(24):
                time_point = now - timedelta(hours=23-i)
                hourly_data.append({
                    'time': time_point.strftime('%H:%M'),
                    'download': random.randint(1000000, 15000000),
                    'upload': random.randint(500000, 5000000)
                })
                
        if not top_devices:
            top_devices = [
                {'id': 1, 'name': 'Gaming PC', 'mac': '00:1A:2B:3C:4D:5E', 'ip': '192.168.1.100', 'type': 'computer', 'usage': random.randint(10000000000, 50000000000)},
                {'id': 2, 'name': 'Smart TV', 'mac': '11:2A:3B:4C:5D:6E', 'ip': '192.168.1.101', 'type': 'entertainment', 'usage': random.randint(20000000000, 80000000000)},
                {'id': 3, 'name': 'iPhone', 'mac': '22:3A:4B:5C:6D:7E', 'ip': '192.168.1.102', 'type': 'mobile', 'usage': random.randint(5000000000, 20000000000)},
                {'id': 4, 'name': 'Work Laptop', 'mac': '33:4A:5B:6C:7D:8E', 'ip': '192.168.1.103', 'type': 'computer', 'usage': random.randint(8000000000, 30000000000)},
                {'id': 5, 'name': 'IoT Hub', 'mac': '44:5A:6B:7C:8D:9E', 'ip': '192.168.1.104', 'type': 'iot', 'usage': random.randint(1000000000, 5000000000)}
            ]
            
        return jsonify({
            'currentUsage': {
                'upload': current_bandwidth['upload'],
                'download': current_bandwidth['download'],
                'maxUpload': 10000000,  # 10 Mbps
                'maxDownload': 50000000,  # 50 Mbps
                'dailyTotal': daily_total,
                'monthlyTotal': monthly_total,
                'monthlyLimit': 500000000000  # 500 GB
            },
            'historicalData': {
                'hourly': hourly_data
            },
            'topDevices': top_devices,
            'alerts': alerts
        })
        
    except Exception as e:
        print(f"Error in get_summary: {e}")
        # Provide mock data if we can't get real data
        return jsonify({
            'currentUsage': {
                'upload': random.randint(500000, 5000000),
                'download': random.randint(1000000, 20000000),
                'maxUpload': 10000000,
                'maxDownload': 50000000,
                'dailyTotal': random.randint(1000000000, 10000000000),
                'monthlyTotal': random.randint(50000000000, 200000000000),
                'monthlyLimit': 500000000000
            },
            'historicalData': {
                'hourly': [
                    {'time': f"{hour:02d}:00", 'download': random.randint(1000000, 15000000), 'upload': random.randint(500000, 5000000)} 
                    for hour in range(24)
                ]
            },
            'topDevices': [
                {'id': 1, 'name': 'Gaming PC', 'mac': '00:1A:2B:3C:4D:5E', 'ip': '192.168.1.100', 'type': 'computer', 'usage': random.randint(10000000000, 50000000000)},
                {'id': 2, 'name': 'Smart TV', 'mac': '11:2A:3B:4C:5D:6E', 'ip': '192.168.1.101', 'type': 'entertainment', 'usage': random.randint(20000000000, 80000000000)},
                {'id': 3, 'name': 'iPhone', 'mac': '22:3A:4B:5C:6D:7E', 'ip': '192.168.1.102', 'type': 'mobile', 'usage': random.randint(5000000000, 20000000000)},
                {'id': 4, 'name': 'Work Laptop', 'mac': '33:4A:5B:6C:7D:8E', 'ip': '192.168.1.103', 'type': 'computer', 'usage': random.randint(8000000000, 30000000000)},
                {'id': 5, 'name': 'IoT Hub', 'mac': '44:5A:6B:7C:8D:9E', 'ip': '192.168.1.104', 'type': 'iot', 'usage': random.randint(1000000000, 5000000000)}
            ],
            'alerts': [
                {
                    'id': 1,
                    'timestamp': datetime.now().isoformat(),
                    'type': 'usage',
                    'severity': 'warning',
                    'message': 'Monthly usage at 75% of limit',
                    'device_id': None
                }
            ] if random.random() > 0.7 else []
        })

@app.route('/api/devices', methods=['GET'])
def get_devices():
    """Get a list of all devices on the network"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                d.id, 
                d.name, 
                d.mac_address, 
                d.ip_address, 
                d.device_type, 
                d.first_seen, 
                d.last_seen,
                SUM(m.total_download) as month_download,
                SUM(m.total_upload) as month_upload
            FROM devices d
            LEFT JOIN monthly_usage m ON d.id = m.device_id
                AND m.year = EXTRACT(YEAR FROM CURRENT_DATE)
                AND m.month = EXTRACT(MONTH FROM CURRENT_DATE)
            GROUP BY d.id
            ORDER BY d.name
        """)
        
        devices = []
        for row in cursor.fetchall():
            devices.append({
                'id': row[0],
                'name': row[1],
                'mac': row[2],
                'ip': row[3],
                'type': row[4],
                'first_seen': row[5].isoformat() if row[5] else None,
                'last_seen': row[6].isoformat() if row[6] else None,
                'month_download': row[7] or 0,
                'month_upload': row[8] or 0
            })
            
        cursor.close()
        conn.close()
        return jsonify(devices)
        
    except Exception as e:
        print(f"Error in get_devices: {e}")
        # Return mock data if database query fails
        return jsonify([
            {'id': 1, 'name': 'Gaming PC', 'mac': '00:1A:2B:3C:4D:5E', 'ip': '192.168.1.100', 'type': 'computer', 
             'first_seen': (datetime.now() - timedelta(days=30)).isoformat(), 'last_seen': datetime.now().isoformat(),
             'month_download': 80000000000, 'month_upload': 20000000000},
            {'id': 2, 'name': 'Smart TV', 'mac': '11:2A:3B:4C:5D:6E', 'ip': '192.168.1.101', 'type': 'entertainment', 
             'first_seen': (datetime.now() - timedelta(days=60)).isoformat(), 'last_seen': datetime.now().isoformat(),
             'month_download': 120000000000, 'month_upload': 5000000000},
            {'id': 3, 'name': 'iPhone', 'mac': '22:3A:4B:5C:6D:7E', 'ip': '192.168.1.102', 'type': 'mobile', 
             'first_seen': (datetime.now() - timedelta(days=45)).isoformat(), 'last_seen': datetime.now().isoformat(),
             'month_download': 30000000000, 'month_upload': 10000000000},
            {'id': 4, 'name': 'Work Laptop', 'mac': '33:4A:5B:6C:7D:8E', 'ip': '192.168.1.103', 'type': 'computer', 
             'first_seen': (datetime.now() - timedelta(days=90)).isoformat(), 'last_seen': datetime.now().isoformat(),
             'month_download': 50000000000, 'month_upload': 15000000000},
            {'id': 5, 'name': 'IoT Hub', 'mac': '44:5A:6B:7C:8D:9E', 'ip': '192.168.1.104', 'type': 'iot', 
             'first_seen': (datetime.now() - timedelta(days=120)).isoformat(), 'last_seen': datetime.now().isoformat(),
             'month_download': 5000000000, 'month_upload': 2000000000}
        ])

@app.route('/api/devices/<int:device_id>', methods=['GET'])
def get_device_details(device_id):
    """Get detailed information about a specific device"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Get device info
        cursor.execute("""
            SELECT id, name, mac_address, ip_address, device_type, first_seen, last_seen
            FROM devices
            WHERE id = %s
        """, (device_id,))
        
        device = cursor.fetchone()
        if not device:
            return jsonify({'error': 'Device not found'}), 404
            
        device_info = {
            'id': device[0],
            'name': device[1],
            'mac': device[2],
            'ip': device[3],
            'type': device[4],
            'first_seen': device[5].isoformat() if device[5] else None,
            'last_seen': device[6].isoformat() if device[6] else None
        }
        
        # Get daily usage for the past 30 days
        cursor.execute("""
            SELECT date, total_download, total_upload
            FROM daily_usage
            WHERE device_id = %s AND date >= CURRENT_DATE - INTERVAL '30 days'
            ORDER BY date
        """, (device_id,))
        
        daily_usage = []
        for row in cursor.fetchall():
            daily_usage.append({
                'date': row[0].strftime('%Y-%m-%d'),
                'download': row[1],
                'upload': row[2],
                'total': row[1] + row[2]
            })
            
        # Get any alerts for this device
        cursor.execute("""
            SELECT id, timestamp, alert_type, severity, message
            FROM alerts
            WHERE device_id = %s
            ORDER BY timestamp DESC
            LIMIT 10
        """, (device_id,))
        
        alerts = []
        for row in cursor.fetchall():
            alerts.append({
                'id': row[0],
                'timestamp': row[1].isoformat(),
                'type': row[2],
                'severity': row[3],
                'message': row[4]
            })
            
        cursor.close()
        conn.close()
        
        return jsonify({
            'device': device_info,
            'usage': daily_usage,
            'alerts': alerts
        })
        
    except Exception as e:
        print(f"Error in get_device_details: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/reports/usage/<period>', methods=['GET'])
def get_usage_report(period):
    """Get usage report for a specific period (daily, weekly, monthly)"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        if period == 'daily':
            # Last 24 hours by hour
            cursor.execute("""
                SELECT 
                    date_trunc('hour', timestamp) as hour,
                    SUM(download_bytes) as download,
                    SUM(upload_bytes) as upload
                FROM bandwidth_data
                WHERE timestamp > NOW() - INTERVAL '24 hours'
                GROUP BY hour
                ORDER BY hour
            """)
            
            report_data = []
            for row in cursor.fetchall():
                report_data.append({
                    'date': row[0].strftime('%H:%M'),
                    'download': row[1],
                    'upload': row[2],
                    'total': row[1] + row[2]
                })
                
        elif period == 'weekly':
            # Last 7 days by day
            cursor.execute("""
                SELECT 
                    date,
                    SUM(total_download) as download,
                    SUM(total_upload) as upload
                FROM daily_usage
                WHERE date >= CURRENT_DATE - INTERVAL '7 days'
                GROUP BY date
                ORDER BY date
            """)
            
            report_data = []
            for row in cursor.fetchall():
                report_data.append({
                    'date': row[0].strftime('%a'),  # Day name (Mon, Tue, etc.)
                    'download': row[1],
                    'upload': row[2],
                    'total': row[1] + row[2]
                })
                
        elif period == 'monthly':
            # Last 30 days by day
            cursor.execute("""
                SELECT 
                    date,
                    SUM(total_download) as download,
                    SUM(total_upload) as upload
                FROM daily_usage
                WHERE date >= CURRENT_DATE - INTERVAL '30 days'
                GROUP BY date
                ORDER BY date
            """)
            
            report_data = []
            for row in cursor.fetchall():
                report_data.append({
                    'date': row[0].strftime('%d'),  # Day of month
                    'download': row[1],
                    'upload': row[2],
                    'total': row[1] + row[2]
                })
                
        else:
            cursor.close()
            conn.close()
            return jsonify({'error': 'Invalid period. Use daily, weekly, or monthly'}), 400
            
        cursor.close()
        conn.close()
        
        # If no data, generate mock data
        if not report_data:
            data_points = 0
            date_format = ""
            now = datetime.now()
            
            if period == 'daily':
                data_points = 24  # Last 24 hours
                date_format = '%H:%M'
                start_date = now - timedelta(hours=24)
                interval = timedelta(hours=1)
            elif period == 'weekly':
                data_points = 7  # Last 7 days
                date_format = '%a'
                start_date = now - timedelta(days=7)
                interval = timedelta(days=1)
            elif period == 'monthly':
                data_points = 30  # Last 30 days
                date_format = '%d'
                start_date = now - timedelta(days=30)
                interval = timedelta(days=1)
                
            report_data = []
            current_date = start_date
            
            for i in range(data_points):
                download = random.randint(500000000, 5000000000)  # 500MB-5GB
                upload = random.randint(100000000, 1000000000)    # 100MB-1GB
                
                report_data.append({
                    'date': current_date.strftime(date_format),
                    'download': download,
                    'upload': upload,
                    'total': download + upload
                })
                current_date += interval
            
        return jsonify({
            'period': period,
            'data': report_data
        })
        
    except Exception as e:
        print(f"Error in get_usage_report: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint for the API"""
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')