# Project: 0x12. Web stack debugging #2 README

This repository contains scripts and configurations to address specific tasks related to running software as another user and configuring Nginx for enhanced security.

## Task 0: Run Software as Another User

### Description

The `0-iamsomeoneelse` script is designed to execute the `whoami` command under a specified user. The motivation behind this task is to emphasize the importance of not running processes as the root user to enhance system security.

### Requirements

- Write a Bash script that accepts one argument.
- The script should run the `whoami` command under the user passed as an argument.
- Ensure the script works with different user arguments.

### Usage Example

```bash
root@ubuntu:~# whoami
root
root@ubuntu:~# ./0-iamsomeoneelse www-data
www-data
root@ubuntu:~# whoami
root
root@ubuntu:~#
```

## Task 1: Run Nginx as Nginx

### Description

This task focuses on improving the security of the Nginx web server by configuring it to run as the less privileged `nginx` user. Running services with minimal privileges helps mitigate potential security risks.

### Requirements

- Nginx must be running as the `nginx` user.
- Nginx must be listening on all active IPs on port 8080.
- The solution should not use `apt-get remove`.
- Write a Bash script to configure the container to meet the above requirements.

### Usage

1. Execute the provided Bash script to configure Nginx:

    ```bash
    ./configure-nginx.sh
    ```

### Notes

- Ensure that the script is executed with the necessary permissions.
- Make sure to test the Nginx configuration after running the script.

