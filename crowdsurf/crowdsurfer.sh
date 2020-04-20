#!/bin/bash

echo " ██████╗██████╗  ██████╗ ██╗    ██╗██████╗ ███████╗██╗   ██╗██████╗ ███████╗"
echo "██╔════╝██╔══██╗██╔═══██╗██║    ██║██╔══██╗██╔════╝██║   ██║██╔══██╗██╔════╝"
echo "██║     ██████╔╝██║   ██║██║ █╗ ██║██║  ██║███████╗██║   ██║██████╔╝█████╗  "
echo "██║     ██╔══██╗██║   ██║██║███╗██║██║  ██║╚════██║██║   ██║██╔══██╗██╔══╝  "
echo "╚██████╗██║  ██║╚██████╔╝╚███╔███╔╝██████╔╝███████║╚██████╔╝██║  ██║██║     "
echo " ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝    "

ip a | grep -q "mon0"
if [[ $? != 0 ]]; then
	echo "Monitor Mode is not enabled!!!!... Exiting......"
	exit 1
fi

sudo rm /root/atos2020/crowdsurf/out/raw-01.csv 2>/dev/null # replace location from line 5
mkdir out 2>/dev/null
xterm -hold -e sudo airodump-ng mon0 -w /root/atos2020/crowdsurf/out/raw -o csv & #set location to store csv file

cp devicemacs.txt currentmac.txt


sleep 5;

function read {
	python - <<END

content = ""
bssid = []
station_MAC = []
i = 0
toWhich = 0
p = 0
devicenum = 0


with open('out/raw-01.csv', 'r') as airdump:
	content = airdump.read()


count = content.split("\n")

while i<len(count):
	carry = count[i].split(",")

	if carry[0] == "Station MAC":
		toWhich = 1;
	elif carry[0] == "\r" or carry[0] == "BSSID":
		pass
	else:
		if toWhich == 0:
			bssid.append(carry[0])
		else:
			station_MAC.append(carry[0])
	i = i+1

outputbssid = []
for x in bssid:
	if x not in outputbssid:
		outputbssid.append(x)

outputmac = []
for x in station_MAC:
	if x not in outputmac:
		outputmac.append(x)


print "\nDevices Nearby :"

v = len(outputmac)
while p < v:
	print outputmac[p]
	p = p + 1
	devicenum = devicenum + 1

devicenum = devicenum - 1
print "Number of devices Present : ", devicenum

with open('numberofdevices.txt', 'w') as numberofdevices:
	numberofdevices.write(str(devicenum))
	
with open('devicemacs.txt', 'a') as f:
	for item in outputmac:
		f.write('%s\n' %item)

END
}

counter=0
while [ $counter -le 2 ]
do
	read
	sudo cp numberofdevices.txt /var/www/html
	sleep 5;
	counter=$((counter+1))
done

if [ $counter -ge 2 ];then
	tn=$(cat numberofdevices.txt) 
	timestamp=$(date '+%Y-%m-%d %H:%M:%S') 
	echo $timestamp,$tn >> dataset.csv # Appends to timestamp and number of people into the dataset
	str=$'\n'
	for i in $(cat currentmac.txt 2>/dev/null)
	do
		machash=$(echo $i | md5sum | rev | cut -c 4- | rev) # converts the MACs into md5 hashes
		echo $machash,$timestamp >> macdb.csv # Appends to MAC database
	done
	cp macdb.csv /var/www/html
	cp dataset.csv /var/www/html
	echo "$str $str Final $str Time:$timestamp,$str Number of devices: $tn"  # Prints out the current status
	pkill -f xterm
fi
