import csv
import re

def find_ip_addresses():
    ip_addresses = []
    pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

    with open(file_name, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            for item in row:
                ip_matches = re.findall(pattern, item)
                ip_addresses.extend(ip_matches)

    return ip_addresses

# Usage
file_name = 'Network_traffic.csv'
ip_list = find_ip_addresses(file_name)
print(ip_list)