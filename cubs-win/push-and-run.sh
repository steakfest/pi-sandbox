#!/bin/bash

scp * pi@rpi-3b-001:/home/pi/

echo "Running cubs-win.py"
# ssh pi@rpi-3b-001 sudo python3 /home/pi/cubs-win.py

echo "Shutting Down"
# ssh pi@rpi-3b-001 sudo python3 /home/pi/stop.py

