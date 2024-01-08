# Project Name

Web Server Configuration and Load Balancer Setup

## Description

This project aims to automate the configuration of web servers and set up a load balancer using Nginx and HAProxy. The goal is to double the number of web servers and distribute incoming traffic using a round-robin algorithm. Additionally, a custom HTTP response header, "X-Served-By," will be added to track which web server is handling the requests.

## Tasks

### Task 0: Double the number of webservers

In this task, the objective is to configure web-02 to be identical to web-01. A Bash script, "0-custom_http_response_header," will be used to automate the configuration process. The script will ensure that Nginx on both web-01 and web-02 includes a custom HTTP header, "X-Served-By," with the value set as the hostname of each respective server.

### Task 1: Install your load balancer

The focus of this task is to install and configure HAProxy on the lb-01 server. HAProxy will be set up to send traffic to web-01 and web-02 using a round-robin algorithm. It should also have an init script for easy management. The servers will be configured with the correct hostnames, [STUDENT_ID]-web-01 and [STUDENT_ID]-web-02, as per the provided tutorial.

### Task 2: Add a custom HTTP header with Puppet

In this advanced task, the objective is to use Puppet to automate the process of adding a custom HTTP header to the web servers. The header, "X-Served-By," should have the value set as the hostname of the Nginx server. The Puppet manifest file, "2-puppet_custom_http_response_header.pp," will be created to configure a new Ubuntu machine to meet these requirements.

## Installation and Usage

For detailed installation and usage instructions, please refer to the individual task files and follow the provided documentation.

## Credits

- Author: yandah1
