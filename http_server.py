import http.server
import socketserver
import subprocess
import sys

def is_package_installed(package_name):
    try:
        __import__(package_name)
        return True
    except ImportError:
        return False

def install_package(package_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

required_packages = []

for package in required_packages:
    if not is_package_installed(package):
        print(f"The package '{package}' is not installed.")
        install = input(f"Would you like to install '{package}' now? (yes/no): ").strip().lower()
        if install == 'yes':
            print(f"Installing '{package}'...")
            install_package(package)
        else:
            print(f"You can continue without '{package}', but the script may not work as intended.")
            sys.exit(1)

port_input = input("Enter the port number to serve on (default is 8000): ")
if not port_input.isdigit():
    print("Invalid port number. Using default port 8000.")
    port = 8000
else:
    port = int(port_input)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", port), Handler) as httpd:
    print(f"Port of the server: {port} (http://localhost:{port})")
    httpd.serve_forever()