sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/hello.conf /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart
sudo gunicorn -c /home/box/web/etc/hello.conf hello:wsgi_app
sudo gunicorn -c /home/box/web/etc/django.conf ask.wsgi:app

