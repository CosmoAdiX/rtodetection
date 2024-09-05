import csv
import sqlite3

# Create a mock RTO database
def create_mock_rto_database():
    conn = sqlite3.connect('rto_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vehicles (
            registration_number TEXT PRIMARY KEY,
            owner_name TEXT,
            vehicle_type TEXT
        )
    ''')
    
    # Insert some mock data
    mock_data = [
        ('MU51YSU', 'Randi Car', 'Car'),
        ('KA02CD5678', 'Jane Smith', 'Motorcycle'),
        ('DL03EF9012', 'Bob Johnson', 'Truck')
    ]
    cursor.executemany('INSERT OR REPLACE INTO vehicles VALUES (?, ?, ?)', mock_data)
    conn.commit()
    conn.close()

# Function to read CSV file
def read_csv_file(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return list(csv_reader)

# Function to scan RTO database
def scan_rto_database(registration_numbers):
    conn = sqlite3.connect('rto_database.db')
    cursor = conn.cursor()
    
    results = []
    for reg_num in registration_numbers:
        cursor.execute('SELECT * FROM vehicles WHERE registration_number = ?', (reg_num,))
        result = cursor.fetchone()
        if result:
            results.append({
                'registration_number': result[0],
                'owner_name': result[1],
                'vehicle_type': result[2]
            })
        else:
            results.append({
                'registration_number': reg_num,
                'owner_name': 'Not found',
                'vehicle_type': 'Not found'
            })
    
    conn.close()
    return results

# Main function
def main():
    # Create mock database
    create_mock_rto_database()
    
    # Read CSV file
    csv_data = read_csv_file('test.csv')
    registration_numbers = [row['license_nmb'] for row in csv_data]
    
    # Scan RTO database
    results = scan_rto_database(registration_numbers)
    
    # Print results
    for result in results:
        print(f"Registration Number: {result['registration_number']}")
        print(f"Owner Name: {result['owner_name']}")
        print(f"Vehicle Type: {result['vehicle_type']}")
        print('-' * 30)

if __name__ == "__main__":
    main()