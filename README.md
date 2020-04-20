

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
