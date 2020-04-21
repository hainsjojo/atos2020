## Description

Crowdsurf is an application that allows users to know the number of people in a particular area at a certain time. It involves a system of detecting the density of the crowd in a specific area using sensors and crunching this data with AI to predict future density of crowds. These sensors are expandable, and using collaborative AI, the data collected by them can be connected and realized into a bigger system covering a large area. All these sensors are continuously updating to give the present number of people to the users. The individual AIs send their collected data and predictions to every other AI (node) in the network directly without a server, making it decentralized. 

## Requirements

```
sudo apt-get install gcc g++ build-essential python-dev python3-dev pip3 apache2 aircrack-ng php7.3 git python3-pandas nc
```

```
pip3 install django
pip3 install fbprophet
```

Clone the repo as root.

```
cd ~
git clone https://github.com/hainsjojo/atos2020.git
```

*Make all the scripts executable*
```
cd ~
chmod +x atos2020/cronjob.sh 
chmod +x atos2020/crowdsurf/mon0.sh 
chmod +x atos2020/crowdsurf/crowdsurfer.sh 
chmod +x atos2020/prophet/prophet.py 
chmod +x atos2020/node_data/receive.sh 
chmod +x atos2020/node_data/transfer.sh
```

Make sure to enable Monitor mode before running the `cronjob.sh`.
```
cd atos2020/crowdsurf/
root@kali:~/atos2020/crowdsurf# ./mon0.sh
```

To append all scripts to crontab run

```
root@kali:~# cd atos2020/
root@kali:~/atos2020# ./cronjob.sh
```
