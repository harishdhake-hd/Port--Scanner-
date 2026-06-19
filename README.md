# Network Port Scanner

A simple Python-based Network Port Scanner that scans a target host and identifies open ports. This project demonstrates the fundamentals of network reconnaissance and socket programming in Python.

## Features

* Scan a target IP address or hostname
* Detect open TCP ports
* Fast and lightweight implementation
* Beginner-friendly code structure
* Useful for learning basic cybersecurity concepts

## Technologies Used

* Python 3
* Socket Programming

## Project Structure

```
port_scanner.py
README.md
```

## How It Works

The scanner attempts to establish a connection to specified ports on a target system. If the connection succeeds, the port is considered open; otherwise, it is closed or filtered.

## Usage

Run the script:

```bash
python3 port_scanner.py
```

Enter the target IP address or hostname when prompted.

## Example Output

```
Scanning target: 192.168.1.1

Port 22: OPEN
Port 80: OPEN
Port 443: OPEN

Scan complete.
```

## Learning Objectives

* Understanding TCP/IP networking
* Using Python sockets
* Performing basic network reconnaissance
* Developing cybersecurity tools

## Future Improvements

* Multi-threaded scanning
* Service detection
* Banner grabbing
* UDP scanning
* Export results to CSV or JSON

## Author

Harish Dhake

BCA student Modern College Pune
 
