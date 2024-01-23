0x14. MySQL`
```markdown
# MySQL Primary-Replica Infrastructure Setup

## Table of Contents
1. [Install MySQL](#install-mysql)
2. [Let Us In!](#let-us-in)
3. [If Only You Could See What I've Seen with Your Eyes](#if-only-you-could-see-what-ive-seen-with-your-eyes)
4. [Quite an Experience to Live in Fear, Isn't It?](#quite-an-experience-to-live-in-fear-isnt-it)
5. [Setup a Primary-Replica Infrastructure Using MySQL](#setup-a-primary-replica-infrastructure-using-mysql)
6. [MySQL Backup](#mysql-backup)

---

## Install MySQL
**Mandatory**

First things first, let’s get MySQL installed on both your web-01 and web-02 servers.

- MySQL distribution must be 5.7.x
- Make sure that task #3 of your SSH project is completed for web-01 and web-02. The checker will connect to your servers to check MySQL status.
- Please make sure you have your README.md pushed to GitHub.

**Example:**

```bash
ubuntu@web-01:~$ mysql --version
mysql  Ver 14.14 Distrib 5.7.x, for Linux (x86_64) using  EditLine wrapper
ubuntu@web-01:~$
```

---

## Let Us In!
**Mandatory**

In order for us to verify that your servers are properly configured, we need you to create a user and password for both MySQL databases, allowing the checker access to them.

- Create a MySQL user named holberton_user on both web-01 and web-02 with the host name set to localhost and the password projectcorrection280hbtn.
- Ensure that holberton_user has permission to check the primary/replica status of your databases.
- Make sure that task #3 of your SSH project is completed for web-01 and web-02.

---

## If Only You Could See What I've Seen with Your Eyes
**Mandatory**

In order to set up replication, you’ll need to have a database with at least one table and one row in your primary MySQL server (web-01) to replicate from.

- Create a database named tyrell_corp.
- Within the tyrell_corp database create a table named nexus6 and add at least one entry to it.
- Ensure that holberton_user has SELECT permissions on your table so that we can check that the table exists and is not empty.

---

## Quite an Experience to Live in Fear, Isn't It?
**Mandatory**

Before you get started with your primary-replica synchronization, create a new user for the replica server on your primary MySQL server (web-01).

- Create a user named replica_user with the host name set to %.
- replica_user must have the appropriate permissions to replicate your primary MySQL server.
- holberton_user will need SELECT privileges on the mysql.user table to check that replica_user was created with the correct permissions.

---

## Setup a Primary-Replica Infrastructure Using MySQL
**Mandatory**

Having a replica member for your MySQL database has advantages such as redundancy and load distribution.

Requirements:
- MySQL primary must be hosted on web-01 - do not use the bind-address, just comment out this parameter.
- MySQL replica must be hosted on web-02.
- Setup replication for the MySQL database named tyrell_corp.
- Provide your MySQL primary configuration as an answer file (my.cnf or mysqld.cnf) with the name 4-mysql_configuration_primary.
- Provide your MySQL replica configuration as an answer file with the name 4-mysql_configuration_replica.

**Tips:**
- Once MySQL replication is set up, add a new record in your table via MySQL on web-01 and check if the record has been replicated in MySQL web-02. If you see it, it means your replication is working!
- Make sure that UFW is allowing connections on port 3306 (default MySQL port) otherwise replication will not work.

---

## MySQL Backup
**Mandatory**

What if the data center where both your primary and replica database servers are hosted is down because of a power outage or even worse: flooding, fire? Then all your data would be inaccessible or lost. That’s why you want to backup and store them in a different system in another physical location.

Write a Bash script that generates a MySQL dump and creates a compressed archive out of it.

Requirements:
- The MySQL dump must contain all your MySQL databases.
- The MySQL dump must be named backup.sql.
- The MySQL dump file has to be compressed to a tar.gz archive.
- This archive must have the following name format: day-month-year.tar.gz.
- The user to connect to the MySQL database must be root.
- The Bash script accepts one argument that is the password used to connect to the MySQL database.
```
