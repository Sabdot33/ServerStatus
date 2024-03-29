import requests
import subprocess
import os

def getServiceStatus(service_name="smbd.service"):

    # Run systemctl command and capture output
    command = ["systemctl", "status", service_name]
    with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
        output, _ = process.communicate(timeout=5)  # Set a timeout to avoid hanging
        if output is None:  # Check for None output
            return ""
        lines = output.decode("utf-8").splitlines()
      
        # Join lines with newline characters for return value
        return "\n".join(lines[:9])  # Return first 9 lines with newlines
    

if __name__ == "__main__":
    service_name = input("Enter a service:  ")
    service_status = getServiceStatus(service_name)
    print(f"{service_name} status: {service_status}")
