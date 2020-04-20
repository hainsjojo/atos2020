#!/bin/bash
(crontab -l 2>/dev/null; echo "*/5 * * * * /root/atos2020/crowdsurf/crowdsurfer.sh") | crontab -
(crontab -l 2>/dev/null; echo "0 * * * * /root/atos2020/prophet/prophet.py") | crontab -
(crontab -l 2>/dev/null; echo "0 * * * * /root/atos2020/node_data/receive.sh") | crontab -
(crontab -l 2>/dev/null; echo "0 * * * * /root/atos2020/node_data/transfer.sh") | crontab -
