import sys

def parse_gnmap(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    ip_ports = []

    for line in lines:
        if line.startswith('Host:'):
            ip = line.split()[1]
            ports_data = line.split('Ports: ')[1] if 'Ports: ' in line else ''
            ports = [port.split('/')[0].strip() for port in ports_data.split(',') if '/' in port]
            for port in ports:
                ip_ports.append(f"{ip}:{port}")

    return ip_ports

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <gnmap_file>")
        sys.exit(1)
    
    gnmap_file = sys.argv[1]
    ip_port_list = parse_gnmap(gnmap_file)
    
    with open('formatted_output.txt', 'w') as f:
        for ip_port in ip_port_list:
            f.write(f"{ip_port}\n")
    
    print("Formatted output written to formatted_output.txt")

if __name__ == "__main__":
    main()
