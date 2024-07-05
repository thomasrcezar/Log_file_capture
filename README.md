Log File Capture
Overview
Log File Capture is a Python-based tool designed to streamline the process of collecting and archiving log files and configuration files for software applications. It provides a user-friendly graphical interface that allows users to specify time ranges, select relevant files, and package them into a single, organized zip archive.
Key Features

Time-based Log File Selection: Capture log files within a specified start and end time range.
Configuration File Inclusion: Automatically include relevant .ini configuration files.
User-friendly Interface: Built with Tkinter for ease of use across different platforms.
Flexible Time Input: Manually input times or capture current system time with a button click.
Custom Save Location: Choose where to save the final zip archive.
Description Inclusion: Add a custom description to each archive for easy identification.

Requirements

Python 3.6+
Tkinter (usually comes pre-installed with Python)

Installation

Clone this repository:
Copygit clone https://github.com/thomasrcezar/Log_file_capture.git

Navigate to the project directory:
Copycd Log_file_capture


Usage

Run the application:
Copypython log_capture_app.py

In the application window:

Set the start and end times for log capture
Enter the software name
Specify the paths for configuration files and log files
Click "Store" to begin the capture process


When prompted, enter a description for the captured data
Choose a location to save the zip archive

File Structure
The generated zip archive will contain:

A Logs folder with the captured log files
An Ini folder with the relevant configuration files
A description.txt file with the user-provided description

Contributing
Contributions to improve Log File Capture are welcome. Please feel free to submit pull requests or open issues to suggest improvements or report bugs.
License
This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

Thanks to all contributors who have helped to improve this tool.
Special thanks to the Python and Tkinter communities for their excellent documentation and resources.