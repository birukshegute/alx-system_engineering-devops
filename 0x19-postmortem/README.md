## 0x19. Postmortem

On May 6th, 2024 at 4:15 AM (EAT), the web page of a local supermarket, BuyMore was down due to a server nginx misconfiguration. Users were getting a 404 - Not Found error as the nginx server could not locate the requested page.

# Timeline:

4:15: 404 - page not found error for users trying to access the website.
4:20: System admins were notified and tried curling the web page. The Ip address responded to the curl request but the domain name didn’t.
4:22: System admins checked if the nginx server, the ufw firewall, and the sql database services were running appropriately. All the services were running.
4:24: System admins checked if the UFW firewall was blocking http and https ports. But UFW was configured properly without blocking port 80 and 443.
4:27: System admins checked if the nginx server configuration files exist and were configured properly. They found a mis-configuration in /etc/nginx/sites-available/default.
4:30: After reconfiguring the configuration file, and restarting the nginx service, the website was operational.

# Root Cause and resolution:

The root cause the problem was human error. In a routine system check, a programmer misspelled the uri address in the “location / {“ of the /etc/nginx/sites-available/default config file. AFter the misspelling was corrected, the problem was resolved and the server was working properly.
