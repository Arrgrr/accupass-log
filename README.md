accupass-log
============
Used to log user error message

there are 3 models

## Log

user: FK

category: FK

message: log message, custom field

log_date: timestamp

## Category

title: define time

## User

name: user name
email: user email
userid: user id

# EC2 setting

###/etc/apache2/sites-enabled/

WSGIScriptAlias / /home/ubuntu/log.accupass.com/accupass-log/accupasslog/wsgi.py
WSGIPythonPath /home/ubuntu/log.accupass.com/accupass-log
<Directory /home/ubuntu/log.accupass.com/accupass-log/accupasslog>
    <Files wsgi.py>
        Order deny,allow
        Require all granted
    </Files>
</Directory>

<Directory /home/ubuntu/log.accupass.com/accupass-log/static>
    Require all granted
</Directory>

<Directory /home/ubuntu/log.accupass.com/accupass-log/media>
    Require all granted
</Directory>