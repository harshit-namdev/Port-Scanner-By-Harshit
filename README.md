# Colorful Port Scanner 🌐🎨

This project is a simple yet powerful **Port Scanner** built with Python. Its standout feature is the colorful output, which makes it visually appealing and easy to understand for users. 🎉 The scanner is designed to check whether specified ports on a target are open or closed, providing color-coded results for quick analysis.

## Features ✨
- **Colorful Output**: Open ports are displayed in red, closed ports in yellow, and the process information is highlighted in blue and magenta.
- **Supports Multiple Targets**: You can scan multiple IP addresses simultaneously by separating them with commas.
- **Simple and User-friendly**: The tool is beginner-friendly and easy to use with a clean and intuitive interface.
  
## Usage 🚀
To use the tool, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/colorful-port-scanner.git
    cd colorful-port-scanner
    ```

2. **Install Dependencies**:
    Install the necessary Python packages:
    ```bash
    pip install -r requirements.txt
    ```
    The project requires the `termcolor` package for colorful output.

3. **Run the Tool**:
    Start scanning by providing the target IP address and number of ports:
    ```bash
    python port_scanner.py
    ```

4. **Example Output**:
    ```text
    [#] Enter your target/s IP address/s (use "," to differentiate between them): 192.168.1.1
    192.168.1.1
    [#] Enter the Number of ports you want to scan: 100
    100
    [+] Scanning Single Target
    Starting Scan For : 192.168.1.1
    [*] Port 22 is open
    [*] Port 80 is closed
    ```

## Installation Requirements 🛠️
- Python 3.x
- `termcolor` package for colored outputs:
    ```bash
    pip install termcolor
    ```

## Contributing 🤝
Contributions are welcome! Feel free to open issues or submit pull requests. 😊

## License 📜
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author 👨‍💻
- **Your Name** – Developer and Cybersecurity Enthusiast
