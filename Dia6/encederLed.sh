#!/bin/bash
#source gpio
gpio mode 17 out
while true; do
echo 1 > /sys/class/gpio/gpio17/value
sleep 1.3
echo 0 > /sys/class/gpio/gpio17/value
sleep 1.3
done
