### 1. Simple Web Stack

**Design:**
- 1 Server, Nginx Web Server, Application Server, MySQL Database
- www.foobar.com, pointed to IP (8.8.8.8)

**Explanation:**
- Server hosts the web infrastructure.
- Domain is a human-readable alias.
- www DNS record points to the server.
- Nginx serves and manages HTTP requests.
- Application Server processes dynamic content.
- MySQL stores and retrieves data.
- Communication via HTTP/HTTPS.

**Issues:**
1. Single Point of Failure
2. Downtime during Maintenance
3. Scalability Concerns

---

### 2. Distributed Web Infrastructure

**Design:**
- 2 Servers, HAproxy Load-Balancer, Application Files, MySQL Database

**Explanation:**
- Load-balancer for distribution.
- Multiple servers for redundancy.
- HAproxy for load balancing.
- MySQL for database functionality.
- Round-robin distribution.
- Active-Active setup.
- Master-Slave for data redundancy.
- Primary for writes, Replica for reads.

**Issues:**
1. Single Points of Failure
2. Security Issues
3. No Monitoring

---

### 3. Secured and Monitored Web Infrastructure

**Design:**
- 3 Firewalls, SSL Certificate, 3 Monitoring Clients

**Explanation:**
- Firewalls for security.
- SSL for encrypted traffic.
- Monitoring for insights.
- Sumo Logic or similar tool for data aggregation.
- HTTPS ensures secure communication.
- Monitoring tracks performance metrics.
- SSL termination at load balancer is an issue.
- Single MySQL server for writes is problematic.
- Uniform server components may pose issues.
