#!/bin/bash

echo "===========Installing============="
BAR='********************'
for i in {1..20}; do
        echo -ne "\r${BAR:0:$i}"
        sleep 0.5
done

#update upgrade Linux/Termux
        sudo apt upgrade -y && sudo apt update -y
#Install python2
        sudo apt get install python2 || sudo pkg install python2
#Install Package module
        pip install futures
        pip install mechanize
        pip install requests
        pip install bs4
chmod +x start.sh
./start.sh
