0x0B. SSH

Table of Contents
Use a Private Key
Create an SSH Key Pair
Client Configuration File
Let Me In!
Use a Private Key

Task Description
Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.

Requirements
Only use ssh single-character flags.
You cannot use -l.
You do not need to handle the case of a private key protected by a passphrase.
Usage
bash
Copy code
./connect_to_server.sh
Create an SSH Key Pair
Task Description
Write a Bash script that creates an RSA key pair.

Requirements
Name of the created private key must be school.
Number of bits in the created key to be created: 4096.
The created key must be protected by the passphrase betty.
Usage
./create_ssh_key_pair.sh
Client Configuration File
Task Description
Your machine has an SSH configuration file for the local SSH client; let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

Requirements
Your SSH client configuration must be configured to use the private key ~/.ssh/school.
Your SSH client configuration must be configured to refuse to authenticate using a password.
Configuration Example
# ~/.ssh/config
Host my_server
    HostName your-server-ip
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
Let Me In!
Task Description
Now that you have successfully connected to your server, we would also like to join the party.

Add the SSH public key below to your server so that we can connect using the ubuntu user.

ssh-rsa [your-ssh-public-key] ubuntu@54.165.52.121ZZ
