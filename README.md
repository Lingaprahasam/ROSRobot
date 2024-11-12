# ROSRobot

## 1. SSH Setup
* Create ssh keys using Linux/Ubuntu client machine 
    * ***ssh-keygen***

* Install commercial OS (Ubuntu server) on pi, with remote login using SSH with username and password authentication

* Use ***ssh-copy-id*** 
command to transfer the ssh keys from client machine to Pi. It will ask password for authentication.
    * From Ubuntu
        * ***ssh-copy-id -i  username@ipaddress***

Now it is possible to ssh the pi from client machine without password authentication.

## From Windows
* Look for ssh keys id_rsa.pub under C:\Users\<user profile>\.ssh
* open id_rsa.pub file and copy the content
* ssh to pi using username and password powershell
* open file authorized_keys under ~/.ssh folder
     * ***sudo nano authorized_keys***
* paste and save the id_rsa.pub content, save and exit
* Now pi is accessible without username and password
