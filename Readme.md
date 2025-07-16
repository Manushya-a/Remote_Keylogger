# Smart Remote Keylogger

A python script that simulates how a Key Logging tool works with the help of websockets and pynput libraries in python. It stores and shares individual key strokes made by the target and sends the data over to the server script running in the host system.

## ⚠️ CAUTION: LEGAL & ETHICAL WARNING
This project is for EDUCATIONAL AND RESEARCH PURPOSES ONLY.

### 🚨 Important Disclaimers:

- Keyloggers can violate privacy laws (e.g., CFAA, GDPR, local regulations).

- Do not use this on any system without EXPLICIT PERMISSION.

- Unauthorized use may result in legal consequences.

### 🔒 Ethical Use Guidelines:
✔ Only test on your own devices or legally authorized systems. 

✔ Get written consent before deployment in any environment.

✔ Do not use for malicious purposes (e.g., stealing credentials).

### 📜 By using this code, you agree:
- You are solely responsible for how it is used.

*~~ The developer is not liable for misuse. ~~*

## Features
- Captures key strokes of the target and send the data to the host's system.
- Stores data on the host device segregated by individual IP addresses.
- `Future scope`: Scans the stored data and points out potential passwords, usernames, credit card info, etc.

## Prerequisites
- Python 3.7+

## Instalation
1. Clone the repository:
    ```bash
    git clone https://github.com/Manushya-a/Smart_Remote_Keylogger.git
    cd Smart_Remote_Keylogger
    ```
2. Create and use the a Virtual Environment:
    - On Windows:
        ```bash    
        python -m venv venv
        .\venv\Scripts\activate
        pip install -r requirements.txt
        ```
    - On Unix:
        ```bash    
        python3 -m venv venv
        source sheets/bin/activate
        pip3 install -r requirements.txt
        ```

## Configuration
- Replace `Your.I.P.Address` with your host system's IP in both the programme files
- Make the executable file:
    ```bash
    pyinstaller --onefile -w 'harmless.py'
    ```
- You can find the executable file (`harmless.exe`) inside the newly generated `dist` folder

## Usage
1. On the host system:
    ```bash
    python server.py # May have to use python3 if on Unix Environment
    ```
2. On the target system double click on the `harmless.exe` file 
3. Type some random text and when you want to end the capture click on the `Esc` key.
4. Check the script running the `server.py`

## Dependencies
Listed in `requirement.txt`

## Support

For questions or issues, please open an issue in the GitHub repository.

---

*This project was developed only for educational purposes and demonstrates WebSocket communication, async programming, and data processing in Python.*