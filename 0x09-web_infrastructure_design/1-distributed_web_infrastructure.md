## The Model:
https://imgur.com/a/344f4jw

## Additional element for this task:

1) Another set of servers: added for the sake of dublicity. It will help share the burden of the previous set of servers if they are setup in that way. Also can be used as an alternative if there is a problem with the previous server, thus minimising down time.

2) Load Balancer: responsible for efficiently distributing incoming network traffic across a group of backend servers.

## Distribution algorithm for the HAProxy load balancer:

The HAProxy load balancer uses Round Robin algorithm. It works by using each server behind the load balancer in turns, according to their weights. It’s also probably the smoothest and most fair algorithm as the servers’ processing time stays equally distributed. As a dynamic algorithm, Round Robin allows server weights to be adjusted on the go.

## Load Balancing cluster setup:

HAProxy provides high availability by employing multiple instances of HAProxy configured in an active-passive setup or a cluster. In this active-passive configuration, one HAProxy instance is the active load balancer, while another acts as a backup or standby. If the active instance fails, the passive instance takes over and continues handling the traffic. This arrangement ensures continuous service availability and minimizes downtime.
On the other hand, in active-active configuration, client machines connect to a load balancer that distributes their workloads across multiple active servers.

## A database Primary-Replica (Master-Slave) cluster:

This is one of the simplest forms of database replication. It involves a primary/master database server that accepts both read and write operations and one or more secondary/slave servers that replicate data from the primary server. Read operations can be distributed to the slave servers, offloading the read workload from the primary server.

## The difference between the Primary node and the Replica node:

The primary is the only member in the replica set that receives write operations. The DataBase applies write operations on the primary and then records the operations. Secondary members replicate this log and apply the operations to their data sets, but they don't perform write operations.

## The issues with this infrastructure:

SPOF: The primary MySQL server is a SPOF as the replica can't perform any write operation on the data. Also the Load balancer server is SPOF as the system will be interrupted without the load balancer.

## Security issues:

NO SSL: Since there is no SSL certificate in the system, the information exchange is not encrypted. Since the information exchanged isn't encrypted, hackers can access to valuable information that they shouldn't get.

No firewall: accepting every attempted connection into the network. We wouldn't have any way to detect incoming threats, which could leave ourservers vulnerable to malicious users without our knowledge.

No monitoring: We cannot control systems that we can't measure. Without the monitoring cleints in the servers, there is no way of knowing the performance of the servers. Therefore it will be hareder to optimise the performance of the system.
