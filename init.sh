sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
source web/myvenv/bin/activate

sudo ln -sf /home/box/web/etc/hello.conf /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart

sudo ln -sf /home/box/web/etc/django.conf /etc/gunicorn.d/django.conf

sudo gunicorn -c /home/box/web/etc/hello.conf hello:wsgi_application
sudo gunicorn -c /home/box/web/etc/django.conf ask.wsgi:application
