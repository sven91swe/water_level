#!bin/bash
#sudo apt install apache2 php -y
#sudo apt install mariadb-server php-mysql -y
#sudo service apache2 restart

sudo rm -r /var/www
sudo mkdir /var/www
cd ../python_code
sudo ln -s `pwd` /var/www/html
cd -

# Assuming that repo water_level is in the pi user home folder
sudo chmod o+x /home/ /home/pi/ /home/pi/water_level/ /home/pi/water_level/php_code