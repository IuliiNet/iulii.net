#!/bin/sh
IPV6PREFIX="2001:470:7023:2"
IPV6=$IPV6PREFIX::$(cat /sys/class/net/eth0/address |awk -F: '{print $1$2":"$3$4":"$5$6}')
echo $IPV6
