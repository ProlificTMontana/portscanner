import socket

import threading


def scan_port(ip, port):

    """Scan a single port on the given IP address."""

    try:

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

            sock.settimeout(1)  # Set a timeout for the connection attempt

            result = sock.connect_ex((ip, port))

            return result == 0  # Return True if the port is open

    except Exception as e:

        print(f"Error scanning port {port}: {e}")

        return False


def scan_ports(ip, start_port, end_port):

    """Scan a range of ports on the given IP address."""

    open_ports = []

    threads = []


    for port in range(start_port, end_port + 1):

        thread = threading.Thread(target=lambda p=port: open_ports.append(p) if scan_port(ip, p) else None)

        threads.append(thread)

        thread.start()


    for thread in threads:

        thread.join()  # Wait for all threads to complete


    return open_ports


def main():

    ip = input("Enter the IP address to scan: ")

    try:

        socket.inet_aton(ip)  # Validate the IP address format

    except socket.error:

        print("Invalid IP address format.")

        return


    try:

        start_port = int(input("Enter the start port: "))

        end_port = int(input("Enter the end port: "))

        if start_port < 0 or end_port > 65535 or start_port > end_port:

            raise ValueError("Port numbers must be between 0 and 65535 and start port must be less than or equal to end port.")

    except ValueError as e:

        print(f"Invalid port range: {e}")

        return


    print(f"Scanning {ip} from port {start_port} to {end_port}...")

    open_ports = scan_ports(ip, start_port, end_port)


    if open_ports:

        print("Open ports:")

        for port in open_ports:

            print(port)

    else:

        print("No open ports found.")


if __name__ == "__main__":

    main()
