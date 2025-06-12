## Port Scanner

# Overview:
portscanner.py is a lightweight and effective Python 3 tool used to scan a target IP address for open TCP ports within a specified range. It helps identify network services that are currently accessible, which is vital for reconnaissance and vulnerability assessment in penetration testing.

# How to use:

    Run the script: Execute portscanner.py and run it using Python 3.
    Input the IP address: When prompted, enter the IP address you want to scan.
    Input the port range: Enter the start and end ports for the scan.
    View results: The script will display the open ports found in the specified range.

# Important Notes:

Make sure you have permission to scan the target IP address, as unauthorized scanning can be considered illegal or malicious activity.

The script uses threading to speed up the scanning process, but be cautious with the number of threads, as scanning too many ports too quickly can lead to being blocked by firewalls or intrusion detection systems.

