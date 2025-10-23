#!/bin/bash

username="dataBaseUser"
password="dataBasePassword"
database="waterlevel"

printf "db_user = \"%s\" \ndb_password = \"%s\" \ndb_name = \"%s\"" $username $password $database > ../python_code/database.py

printf "<?php \n\$db_user = \"%s\";\n\$db_password = \"%s\";\n\$db_name = \"%s\";\n?>" $username $password $database > ../php_code/database.php


sudo mysql -e "CREATE DATABASE IF NOT EXISTS $database"
sudo mysql -e "GRANT ALL ON $database.* TO '$username'@'localhost' IDENTIFIED BY '$password';"

mysql --user=$username --password=$password $database -e "CREATE TABLE data (id int NOT NULL AUTO_INCREMENT, value int, time datetime, PRIMARY KEY (id));"
