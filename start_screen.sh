#!/bin/bash

# Assumed path of repo
cd /home/pi/water_level

screen -S water -dm ./start_measure.sh
cd -
