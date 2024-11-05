# ROSRobot

1. ## SSH Setup
* Create ssh keys using Linux/Ubuntu client machine 
    * ***ssh-keygen***

* Install commercial OS (Ubuntu server) on pi, with remote login using SSH with username and password authentication

* Use ***ssh-copy-id*** 
command to transfer the ssh keys from client machine to Pi. It will ask password for authentication.
    * From Ubuntu
        * ***ssh-copy-id -i  username@ipaddress***

Now it is possible to ssh the pi from client machine without password authentication.
