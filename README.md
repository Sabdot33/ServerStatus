# ServerStatus

## Important Note:

* This application has only been tested on Ubuntu-based operating systems.
* The project is under development and not intended for public distribution. It serves as a personal learning project.

## Project Overview

ServerStatus is a web application designed to deliver real-time monitoring and status updates for servers. It empowers users to view the current health of their servers and track performance metrics

The objective is to simplify server monitoring, enabling proactive management and swift responses to potential downtimes or performance degradations.

This specific version focuses on monitoring Jellyfin, XRDP, and Samba, but it can be readily customized to suit individual requirements. Feel free to explore the codebase, make improvements, and experiment with it.

## Dependencies

The required dependencies are listed in the `requirements.txt` file. Here's a general overview:

- Flask (web framework)
- Waitress (production server)
- requests (making HTTP requests)

## Running the Application

1. **Set up a Python virtual environment:**
   - This isolates project dependencies and avoids conflicts. Refer to Python's documentation for virtual environment creation.

2. **Activate the virtual environment.**
   - Run `python3 -m venv {Name}` to do so 

4. **Install dependencies:**
   - Within the activated virtual environment, run `pip install -r requirements.txt` to install the necessary libraries.

5. **Run the application:**
   - Execute `main.py` to start the web application.

**Additional Considerations**

- **Security:** Since this project is not intended for public use, security hasn't been thoroughly implemented. I advise not running it in untrusted environments or being *extremely* careful.
- **Configuration:** To configure what services or apps the focus should be on, simply edit `Jellyfin.py`, `Samba.py` or `Xrdp.py`.
- **Future Development:** If you plan to share the project in the future, consider adding a roadmap or outlining potential enhancements.
