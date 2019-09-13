sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/hello.conf /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/django.conf /etc/gunicorn.d/views.py
sudo /etc/init.d/gunicorn restart
