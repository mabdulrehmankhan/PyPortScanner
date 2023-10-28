# PyPortScanner

**Author**: MUHAMMAD ABDUL REHMAN KHAN

PyPortScanner is a simple Python-based network tool designed to help network administrators and security professionals perform port scanning on a target host. This tool allows users to scan a list of specified ports on a given target host and provides information about the status of each port (open or closed). It also displays well-known port descriptions for reference, making it a useful tool for identifying potential vulnerabilities and discovering services running on the target system.

## Features

- Scans specified ports on a target host.
- Identifies open and closed ports.
- Displays well-known port descriptions for reference.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/mabdulrehmankhan/PyPortScanner.git
   ```

2. Change to the project directory:

   ```bash
   cd PyPortScanner
   ```

3. Run the PyPortScanner script:

   ```bash
   python PyPortScanner.py
   ```

## Usage

1. When you run the script, it will welcome you to the Port Scanner and display a list of well-known ports and their descriptions for reference.

2. Enter the target host (e.g., `google.com`).

3. Enter the target ports as a comma-separated list (e.g., `80, 20, 443`).

4. The script will start scanning the specified ports and display the results, including whether each port is open or closed.

## Example

Here's an example of running PyPortScanner:

```plaintext
WELCOME TO PORT SCANNER

Well-known ports and their descriptions:
20: FTP (File Transfer Protocol) - Data
21: FTP (File Transfer Protocol) - Control
...

Enter the target host (e.g. google.com): google.com
Enter the target ports (comma-separated) (e.g. 80, 20, 443): 80, 443, 8080

[+] Scan Result for: google.com

Scanning Port: 80
[+] 80/TCP open
Scanning Port: 443
[+] 443/TCP open
Scanning Port: 8080
[-] 8080/TCP closed
```

## License

This project is licensed under the FREE LICENSE. You can use it for educational purpose ONLY.

---

Feel free to customize this README with additional sections, images, or any other information you'd like to include.
