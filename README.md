# Simple Python HTTP Server

This is a simple HTTP server implemented in Python using the socket module. The server listens for incoming requests from clients and responds to these requests by serving HTML files.

## Features

- **Basic HTTP Server**: Implements a basic HTTP server using TCP/IP sockets.
- **Handling Requests**: Processes incoming HTTP requests from clients to serve requested files.
- **Response Handling**: Generates appropriate HTTP responses based on the requested file's availability.
- **Error Handling**: Provides a custom 404 Not Found page if the requested file is not available.

## File Structure
- **server.py**: Contains the Python code for the HTTP server.
- **html/**: Directory containing HTML files to be served by the server.
- **hyperlink.html**: Sample HTML file that can be accessed by default.
- **tidak_ketemu.html**: Custom HTML file for 404 Not Found error.

## Requirements
- **Python 3.x**

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/dapraws/WebServer-Python.git
2. Navigate to the project directory:
   ```bash
   cd WebServer-Python
3. Run the server:
   ```bash
   webServer.py
