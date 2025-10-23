# Hardware assumptions
This was developed using a Raspberry Pi 5 (4GB variant, https://www.raspberrypi.com/products/raspberry-pi-5/)
and a Arduino Uno

Additional sensors, current and voltage converters were used but they have no software.

# Install Raspberry PI 5
First install Raspberry Pi OS per https://www.raspberrypi.com/software/

Then install git using 
```
sudo apt-get update
sudo apt-get install git
```

## Install web server
For this we will use a LAMP server per instructions here (https://projects.raspberrypi.org/en/projects/lamp-web-server-with-wordpress). Skipping the part with the Wordpress installation.

Run the script install_web.sh

After that go to ip address of the Raspberry Pi /info.php in a web browser to see that webserver is setup correctly.