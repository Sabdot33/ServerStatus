import subprocess

def check_jellyfin_service_status():
  """Checks the status of the smbd.service using systemctl."""
  # Run systemctl command and capture output
  command = ["sudo", "systemctl", "show", "-p", "ActiveState", "smbd.service"]
  output = subprocess.check_output(command).decode("utf-8").strip()

  # Extract the active state from the output
  Jellystate = output.split("=")[1]

  return Jellystate

if __name__ == "__main__":
  status = check_jellyfin_service_status()
  print(f"Samba service (smbd.service) status: {status}")
