sudo ﻿ln -sf /home/box/web/etc/nginx.conf  /web/etc/nginx.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart


# /etc/nginx/sites-enabled/default