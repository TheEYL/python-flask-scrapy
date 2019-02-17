## Setup instructions:

$ (sudo) virtualenv -p python3 /python-flask-scrappy  
To activate your virtualenv:  
$ source /python-flask-scrappy/bin/activate  
if having issues with `pkg-resources==0.0.0`, remove from requirements.txt (some ubuntu error with metadata)  
$ (sudo *not recommended*) pip3 install -r requirements.txt  
To run Flask:  
$ cd flask_web_app/  
$ python movie_manager.py  
go to port http://127.0.0.1:5000/  
You will see an error because postgres has not been installed yet  

#### To install postgres on Mac:  
$ cd ..  
Remove previous versions of PostgreSQL  
$brew uninstall --force postgresql  
Delete all Files of Postgres  
$ rm -rf /usr/local/var/postgres  
Install Postgres with Homebrew  
$ brew install postgres  
Install PostGIS with Homebrew  
$ brew install postgis  
Create the db and Movie table:  

installed Postgres desktop app  
initialized a new server  
went to postgres, auto opened terminal window with postgres initialized  
$ \d  
$ CREATE TABLE movies (id SERIAL PRIMARY KEY, title TEXT, url TEXT, image TEXT);   
$ \d  


#### After the db has been created, it is scrappy time!  
$ source /python-flask-scrappy/bin/activate  
Go into directory with scrappy cd scrapper/movieScraper/movieScraper  
$ scrapy crawl imdb_scrap  
