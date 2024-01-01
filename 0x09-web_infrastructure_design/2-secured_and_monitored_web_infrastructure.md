## The Model
https://imgur.com/a/Bs05231

## Additional element for this task:

SSL Cerificate: SSL, more commonly called TLS, is a protocol for encrypting Internet traffic and verifying server identity. Any website with an HTTPS web address uses SSL/TLS. SSL certificates are what enable websites to use HTTPS, which is more secure than HTTP. An SSL certificate is a data file hosted in a website's origin server. SSL certificates make SSL/TLS encryption possible, and they contain the website's public key and the website's identity, along with related information.

Firewall: is a network security device that monitors incoming and outgoing network traffic and decides whether to allow or block specific traffic based on a defined set of security rules.

Sumo logic Monitoring Service: helps server admin gain visibility into the health, performance, and behavior of databases with KPIs like failed logins, slow queries, connections or deadlocks.

## Monitoring is used for:

Understanding database health and performance from the context of user transactions and overall application performance puts a new light on the ability to observe the system’s internal state.

## How does the monitoring tool collecting data?

The monitoring tool observes the servers and provides key metrics about the servers' operations to the administrators. It automatically tests the accessibility of the servers, measures response time, and alerts for errors such as corrupt/missing files, security vulnerabilities/violations, and many other issues.

## Issues are with this infrastructure

Terminating SSL at the load balancer level is an issue: There is no encryption between load balancer and other servers, making gthe server vurnerable.

Having only one MySQL server capable of accepting writes is an issue: as it makes it a SPOF. The service will struggle to add new information to server when said Server is down, affecting scalability.

Having servers with all the same components (database, web server and application server) might be a problem: would make the components contend for resources on the server like CPU, Memory, I/O, etc., which can lead to poor performance and also make it difficult to locate the source of the problem.
