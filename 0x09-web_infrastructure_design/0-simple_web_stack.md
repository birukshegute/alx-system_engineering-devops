## The model:
https://imgur.com/a/v78jViN

## A Server:
A server is a computer or system that provides resources, data, services, or programs to other computers, known as clients, over a network.

## The role of the domain name:
The role of the domain is to make the ip address of a server human readable. In our example, the IPV4 adress 8.8.8.8 may cause users a problem as it is a long number and it may be difficult to remember it (most IP adresses are like that). But, the doamain name foobar.com is easier to remember and therefore it will make the website accessible. A communication exchange between the user browser and a DNS server will translate the domain name into the respective IP adress using the DNS A record.

## What type of DNS record www is in www.foobar.com?

It is a CNAME type DNS. 
A CNAME is a DNS record type that maps the subdomains or the alias names to the true Domain.

## The role of the web server:

A web server is a computer system capable of delivering web content to end users over the internet via a web browser. The end user processes a request via a web browser installed on a web server. The communication between a web server or browser and the end user takes place using Hypertext Transfer Protocol (HTTP). The primary role of a web server is to store, process, and deliver requested information or webpages to end users.

## The role of the application server:

Application servers are designed to provide applications with the fundamentals that they need to make them functional and efficient. Some of the services that are provided for applications are security, improved availability, supports complex database access, transaction support, and mail services.

## The role of Database:

A database is a collection of data and information that is stored in an organized manner for easy retrieval. The primary purpose of a database is to store, retrieve, and update information. A database can be used to store data related to any aspect of business operations.

## What is the server using to communicate with the user?

The server is using the TCP/IP protocol suite to communicate with the user computer. It happens using the http protocol over the Internet.

## Issues with this Infrastructure:

SPOF: The infrastracture has only one Web Server, one Application Server and one Database server, which means if one of them are down, the entire system is down.

Downtime when maintenance needed: Since there is no duplication in the server side, when there is a maintenance in the server side, there will be system interruption.

Cannot scale if too much incoming traffic: Since there are no multiple servers in the server side, and there is no load balancing because of that, if the server has too many requests, then it will be inefficient and slow.
