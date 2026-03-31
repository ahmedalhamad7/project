import sqlite3
from datetime import datetime, timedelta


def seed_database():
    """Seed the database with sample data."""
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()

    # Check if data already exists
    cursor.execute('SELECT COUNT(*) FROM sites')
    if cursor.fetchone()[0] > 0:
        print("Database already seeded. Skipping...")
        conn.close()
        return

    # Sample sites
    sites = [
        ('Tower Alpha', 'New York', 'Northeast', 'tower'),
        ('Data Center 1', 'Chicago', 'Midwest', 'data_center'),
        ('Switch Hub A', 'Los Angeles', 'West', 'switch'),
        ('Router Node 1', 'Miami', 'Southeast', 'router'),
        ('Tower Beta', 'Seattle', 'Northwest', 'tower'),
        ('Data Center 2', 'Dallas', 'South', 'data_center'),
    ]

    cursor.executemany('''
        INSERT INTO sites (name, location, region, site_type) 
        VALUES (?, ?, ?, ?)
    ''', sites)

    # Sample incidents
    incidents = [
        ('Network Outage', 'Complete network failure at site', 'critical', 'open', 1),
        ('Power Fluctuation', 'Intermittent power issues detected', 'high', 'in_progress', 2),
        ('Cooling System Alert', 'Temperature above normal range', 'medium', 'open', 2),
        ('Fiber Cut', 'Fiber optic cable damaged', 'critical', 'resolved', 3),
        ('Router Malfunction', 'Router experiencing packet loss', 'high', 'in_progress', 4),
        ('Scheduled Maintenance', 'Routine maintenance required', 'low', 'open', 5),
    ]

    cursor.executemany('''
        INSERT INTO incidents (title, description, severity, status, site_id) 
        VALUES (?, ?, ?, ?, ?)
    ''', incidents)

    # Sample updates
    updates = [
        ('Initial assessment complete. Dispatching technician.', 'John Smith', 1),
        ('Backup power engaged. Investigating root cause.', 'Jane Doe', 2),
        ('HVAC team notified. Monitoring temperature.', 'Mike Johnson', 3),
        ('Cable repair completed. Service restored.', 'Sarah Williams', 4),
        ('Firmware update in progress.', 'Tom Brown', 5),
        ('Maintenance scheduled for next week.', 'Emily Davis', 6),
    ]

    cursor.executemany('''
        INSERT INTO updates (update_text, updated_by, incident_id) 
        VALUES (?, ?, ?)
    ''', updates)

    conn.commit()
    conn.close()
    print("Database seeded successfully!")


def clear_database():
    """Clear all data from the database."""
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM updates')
    cursor.execute('DELETE FROM incidents')
    cursor.execute('DELETE FROM sites')

    # Reset auto-increment counters
    cursor.execute("DELETE FROM sqlite_sequence WHERE name IN ('sites', 'incidents', 'updates')")

    conn.commit()
    conn.close()
    print("Database cleared successfully!")


if __name__ == '__main__':
    seed_database()
