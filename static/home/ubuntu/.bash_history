sudo apt-get update
sudo apt-get install python-pip
sudo apt-get install python-dev
sudo apt-get install nginx
sudo apt-get install git
sudo apt-get update
sudo pip install virtualenv
git clone https://github.com/zer8ne/bentome.git
cd bentome
virtualenv venv
source venv/bin/activate
pip install django
pip install bcrypt
pip install django-extensions
pip install --upgrade stripe
pip list
pip install gunicorn
ls
cd bentome
sudo vim settings.py
cd ..
python manage.py collectstatic #say yes
gunicorn --bind 0.0.0.0:8000 bentome.wsgi:application
deactivate
sudo vim /etc/systemd/system/gunicorn.service
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo vim /etc/nginx/sites-available/bentome
sudo ln -s /etc/nginx/sites-available/bentome /etc/nginx/sites-enabled
sudo nginx -t
sudo rm /etc/nginx/sites-enabled/default
sudo service nginx restart
cd bentome
source venv/bin/activate
ls
cd apps/home/templates/home
ls
vi dashboard.html
cd ~
ls
cd bentome
gitinit
git init
git push origin master
restart
ls
cd bentome
ls
cd apps
ls
cd home
ls
vim dashboard.html
cd templates/home
ls
vim dashboard.html
cd ..
ls
cd ..
ls
cd media
ls
cd ..
ls
cd bentome
ls
vim settings.py
cd ..
ls
cd bentome
vim settings.py
python manage.py collectstatic #say yes
cd ..
python manage.py collectstatic #say yes
ls
source venv/bin/activate
python manage.py collectstatic #say yes
python manage.py collectmedia #say yes
deactivate
ls
cd bentome
ls
vi urls.py
vim settings.py
vi urls.py
cd ..
ls
cd media
ls
cd ..
ls-al
ls -al
cd media
cd ..
cd bentome
vim settings.py
vim urls.py
vim settings.py
cd ..
ls
vim /etc/nginx/nginx.conf
cd ..
cd /etc
ls
cd nginx
ls
vim nginx.conf
sudo vim nginx.conf
nginx -s reload
cd ..
cd bentome
ls
cd ~
ls
cd bentome
git init
git add .
git commit -m "menu added for 3.20-3.24"
git push origin frontend
git branch
git push origin master
git pull origin master
git push origin master
ls
cd bentome
ls
cd apps
ls
cd home
cd templates
ls
cd home
ls
vim dashboard.html
ls
cd bentome
ls
cd apps
ls
cd home
ls
cd ..
ls
cd ..
ls
cd apps
ls
cd home
ls
cd templates
ls
cd home
ls
cd index.html
sudo vim index.html
cd ..
ls
cd ..
ls
vim urls.py
cd ..
cd apps
ls
cd home
vim urls.py
cd ..
ls
cd users
vim urls.py
cd ..
cd home
vim urls.py
cd ..
ls
cd bentome
ls
vim settings.py
cd ..
ls
cd bentome
ls
cd bentome
ls
cd apps
ls
cd ..
cd bentome
ls
vim urls.py
cd ..
git init
git push -u origin master
git remote add origin https://www.github.com/zer8ne/bentome.git
git push -u origin master
git remote
git add .
ls
cd bentome
ls
cd bentome
ls
cd media
ls
rm -rf *
ls
cd ..
ls
cd apps
cd bentome
ls
cd home
ls
cd static/home/images
ls
rm -rf *
ls
cd ..
ls
cd ..
ls
cd ..
ls
cd home
ls
atom . --disable-gpu
curl -o /usr/local/bin/rmate https://raw.githubusercontent.com/aurora/rmate/master/rmate
cd ~
curl -o /usr/local/bin/rmate https://raw.githubusercontent.com/aurora/rmate/master/rmate
sudo wget -O /usr/local/bin/rmate https://raw.github.com/aurora/rmate/master/rmate
sudo chmod a+x /usr/local/bin/rmate
rmate test.txt
ls
cd bentome
ls
cd apps
ls
cd adminbento
ls
cd urls.py
vim urls.py
ls
vim views.py
