# Web Stack Debugging #1

This project focuses on debugging and resolving an issue with an Nginx installation that is not listening on port 80 in an Ubuntu container. The goal is to automate the fix using a Bash script.

## Requirements

- Nginx must be running and listening on port 80 of all the server's active IPv4 IPs.
- The Bash script should configure the server to meet the above requirements.
- The Bash script should be sweet and short.

## Debugging the Issue

To debug the issue and find out what's preventing Nginx from listening on port 80, follow these steps:

1. Start an Ubuntu container.
2. Install any necessary debugging tools.
3. Use the tools to diagnose the issue and identify the root cause.
4. Make the necessary changes to the Nginx configuration to enable it to listen on port 80.
5. Test the changes to ensure Nginx is now listening on port 80.

## Bash Script

To automate the fix for the Nginx issue, a Bash script has been provided. The script is designed to be concise and efficient, adhering to the following requirements:

- The script is 5 lines long or less.
- There is a new line at the end of the file.
- The script follows usual Bash script requirements.
- The script does not use the ';' operator.
- The script does not use the '&&' operator.
- The script does not use the 'wget' command.
- The script does not execute the previous answer file (the name of the previous script is not included in this one).
- The 'service' (init) command must correctly report that Nginx is not running.

## Usage

1. Copy the provided Bash script to your server.
2. Make the script executable, if necessary.
3. Run the script using the appropriate command (e.g., `bash script.sh`, `./script.sh`).

Please note that this README file provides an overview of the project and its requirements. For detailed instructions and code implementation, refer to the script itself.
