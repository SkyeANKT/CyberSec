# Setting up the server

### VM Platform
Amazon EC2 <br>
<b>IP:</b> 18.143.138.152
### AMI image
Ubuntu 22:04
### Hostname:
<b>Provider:</b> No_IP <br>
<b>Hostname:</b> https://g3-tech.ddns.net

### Web Serve
<b>Apache2</b> 
```
sudo apt install apache2
```

### Database Sever
<b>MySQL</b>
```
sudo apt install mysql-server
```

### Scripting Language
<b>PHP</b>
```
sudo apt install php php-common php-curl php-mysql php-imagick php-mbstring php-xml php-zip
```

### SSL Certificate
<b>Provider:</b> Let's Encrypt <br>
<b>Type:</b> RSA
```
sudo snap install --classic certbot
sudo certbot --apache --key-type rsa
```

### Content Management System (CMS)
<b>WordPress</b>
```
sudo wget https://wordpress.org/latest.tar.gz
```

<br>
<br>
<br>
<br>
<br>

# Defense Method Use:
<b>DDoS</b> ----> iptables(Network Level) + mod_evasive(Application Level)

### Mod Evasive
[Reference: https://www.atlantic.net/vps-hosting/how-to-install-and-configure-modevasive-with-apache-on-ubuntu-18-04/]
- To install mod_evasive, enter a below command
```
sudo apt install libapache2-mod-evasive
```
- To config a mod evasive, enter a below command to access a config file.
```
sudo nano /etc/apache2/mods-available/evasive.conf
```
- Change only a number to 
```
<IfModule mod_evasive20.c>

        DOSHashTableSize        3097
        <!-- Hash table size 3097 -->
        
        DOSPageCount            5
        DOSPageInterval         3
        <!-- Access same page 5 times within 3 sec -->
        
        DOSSiteCount            5
        DOSSiteInterval         3
        <!-- Access same internal site 5 time within 3 sec -->
        
        DOSBlockingPeriod       300
        <!-- Block those who violate these rules for 300 sec (5 min) -->

        DOSEmailNotify          U6215224@gmail.com
        DOSSystemCommand        "su - someuser -c '/sbin/... %s ...'"
        DOSLogDir               "/var/log/apache2"
        DOSWhitelist            49.230.144.118 219.100.37.241 216.144.248.26
        
</IfModule>
```
Note: this only slow down the attacking and help prevent our server from cpu overload, but still able to slow down our server 

### Iptables

#### Blocked IP
- Replace IP-Address to block specific the malicious IP-Address
```
sudo iptables -A INPUT -s [IP-Address] -j DROP
```
This is the exmple of the IP Address that I've block
```
sudo iptables -A INPUT -s 180.183.10.158 -j DROP
sudo iptables -A INPUT -s 1.46.158.50 -j DROP
sudo iptables -A INPUT -s 180.183.8.203 -j DROP
sudo iptables -A INPUT -s 52.23.162.86 -j DROP
sudo iptables -A INPUT -s 52.65.155.151 -j DROP
sudo iptables -A INPUT -s 168.120.248.48 -j DROP
```
### Plugin >> Security by CleanTalk (Firewall+Malware Check) + W3 Total Cache (Cache)


## Login
- Change your current directory to the Key Pair location on your device
```
ssh -i "User01.pem" ubuntu@ec2-18-143-138-152.ap-southeast-1.compute.amazonaws.com
```


# Log file 
### Mornitoring
- use `-f` to monitor a real-time log
```
sudo tail -f /var/log/apache2/access.log
```
- use `-n ###` to monitor a log in ### line
```
sudo tail -n 500 /var/log/apache2/access.log
```
### Filter
```
| grep -Ev '49.230.144.118|CleanTalk|Cleantalk-Helper|UptimeRobot|internal dummy connection|180.183.8.203|180.183.8.203|52.23.162.86|1.46.158.50'
```
## Hide Sensitive Sever Information
- To hide a sensitive server information you need to access the configuration file locates as in below command:
```
sudo nano /etc/apache2/conf-enabled/security.conf
```
Once you access the file:

```
ServerTokens Prod
ServerSignature Off
FileETag None
```

1. you need to search for the line where it have the word `ServerToken` and add `ServerTokens Prod` to it below. 
2. Then search for `ServerSignature` then put `#` in front of `ServerSignature On` and delete `#` in front of `ServerSignature Off` away. 
3. Add the `FileETag None` to any where in the file

After you done config the file, `Ctrl+o` to save and press `enter` to confirm, then `Ctrl+x` to escape from that file

chmod 644 /path/to/wp-config.php