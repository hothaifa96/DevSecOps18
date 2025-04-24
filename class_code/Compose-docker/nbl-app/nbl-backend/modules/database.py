import psycopg2
import os
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Database connection details from environment variables
DB_HOST = os.environ.get('DB_HOST', 'postgres')
DB_USER = os.environ.get('DB_USER', 'netbl_user')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'netbl_password')
DB_NAME = os.environ.get('DB_NAME', 'netbl_db')
DB_PORT = os.environ.get('DB_PORT', '5432')

def get_db_connection():
    """Get a connection to the PostgreSQL database"""
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )
    return conn

# SQL script for database initialization
INIT_SQL = """
-- Create tables for the Network Bandwidth Logger application

-- Devices table to track all devices on the network
CREATE TABLE IF NOT EXISTS devices (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    mac_address VARCHAR(17) UNIQUE NOT NULL,
    ip_address VARCHAR(15),
    device_type VARCHAR(50),
    first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Bandwidth data table to store usage metrics
CREATE TABLE IF NOT EXISTS bandwidth_data (
    id SERIAL PRIMARY KEY,
    device_id INTEGER REFERENCES devices(id),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    download_bytes BIGINT NOT NULL,
    upload_bytes BIGINT NOT NULL,
    session_duration INTEGER -- in seconds
);

-- Daily aggregates for faster reporting
CREATE TABLE IF NOT EXISTS daily_usage (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    device_id INTEGER REFERENCES devices(id),
    total_download BIGINT NOT NULL,
    total_upload BIGINT NOT NULL,
    UNIQUE (date, device_id)
);

-- Monthly aggregates for faster reporting
CREATE TABLE IF NOT EXISTS monthly_usage (
    id SERIAL PRIMARY KEY,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    device_id INTEGER REFERENCES devices(id),
    total_download BIGINT NOT NULL,
    total_upload BIGINT NOT NULL,
    UNIQUE (year, month, device_id)
);

-- Alerts table for tracking network anomalies
CREATE TABLE IF NOT EXISTS alerts (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    alert_type VARCHAR(50) NOT NULL,
    severity VARCHAR(20) NOT NULL,
    message TEXT NOT NULL,
    device_id INTEGER REFERENCES devices(id),
    acknowledged BOOLEAN DEFAULT FALSE
);

-- Insert some sample devices
INSERT INTO devices (name, mac_address, ip_address, device_type) VALUES
('Gaming PC', '00:1A:2B:3C:4D:5E', '192.168.1.100', 'computer'),
('Smart TV', '11:2A:3B:4C:5D:6E', '192.168.1.101', 'entertainment'),
('iPhone', '22:3A:4B:5C:6D:7E', '192.168.1.102', 'mobile'),
('Work Laptop', '33:4A:5B:6C:7D:8E', '192.168.1.103', 'computer'),
('IoT Hub', '44:5A:6B:7C:8D:9E', '192.168.1.104', 'iot')
ON CONFLICT (mac_address) DO NOTHING;

-- Function to generate random data for testing
CREATE OR REPLACE FUNCTION generate_sample_data() RETURNS void AS $$
DECLARE
    device_rec RECORD;
    current_date TIMESTAMP := NOW() - INTERVAL '30 days';
    end_date TIMESTAMP := NOW();
    current_time TIMESTAMP;
    download_amount BIGINT;
    upload_amount BIGINT;
BEGIN
    -- For each device
    FOR device_rec IN SELECT id FROM devices LOOP
        current_time := current_date;
        
        -- Generate data for the last 30 days
        WHILE current_time < end_date LOOP
            -- Random download and upload amounts between 10MB and 1GB
            download_amount := floor(random() * 990000000 + 10000000);
            upload_amount := floor(random() * 290000000 + 10000000);
            
            -- Insert hourly record
            INSERT INTO bandwidth_data (device_id, timestamp, download_bytes, upload_bytes, session_duration)
            VALUES (device_rec.id, current_time, download_amount, upload_amount, floor(random() * 3600));
            
            current_time := current_time + INTERVAL '1 hour';
        END LOOP;
    END LOOP;
    
    -- Aggregate daily data
    INSERT INTO daily_usage (date, device_id, total_download, total_upload)
    SELECT 
        DATE(timestamp),
        device_id,
        SUM(download_bytes),
        SUM(upload_bytes)
    FROM bandwidth_data
    GROUP BY DATE(timestamp), device_id
    ON CONFLICT (date, device_id) DO UPDATE
    SET total_download = EXCLUDED.total_download,
        total_upload = EXCLUDED.total_upload;
        
    -- Aggregate monthly data
    INSERT INTO monthly_usage (year, month, device_id, total_download, total_upload)
    SELECT 
        EXTRACT(YEAR FROM timestamp),
        EXTRACT(MONTH FROM timestamp),
        device_id,
        SUM(download_bytes),
        SUM(upload_bytes)
    FROM bandwidth_data
    GROUP BY EXTRACT(YEAR FROM timestamp), EXTRACT(MONTH FROM timestamp), device_id
    ON CONFLICT (year, month, device_id) DO UPDATE
    SET total_download = EXCLUDED.total_download,
        total_upload = EXCLUDED.total_upload;
END;
$$ LANGUAGE plpgsql;
"""

def init_db():
    """Initialize the database with tables and sample data"""
    try:
        # First create a connection to make sure the server is available
        conn = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        
        # Check if database exists, if not create it
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (DB_NAME,))
        if cursor.fetchone() is None:
            cursor.execute(f"CREATE DATABASE {DB_NAME}")
        
        cursor.close()
        conn.close()
        
        # Now connect to the specific database and initialize tables
        conn = get_db_connection()
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        
        # Execute the initialization SQL script
        cursor.execute(INIT_SQL)
        
        # Check if we already have data in the bandwidth_data table
        cursor.execute("SELECT COUNT(*) FROM bandwidth_data")
        count = cursor.fetchone()[0]
        
        # Only generate sample data if we don't have any
        if count == 0:
            cursor.execute("SELECT generate_sample_data();")
            print("Sample data generated successfully!")
        else:
            print(f"Database already contains {count} bandwidth records, skipping sample data generation.")
        
        cursor.close()
        conn.close()
        
        return True
    except Exception as e:
        print(f"Error in init_db: {e}")
        raise