# Logs Analysis Project
### by Satheesh Gajula
This is a project for Udacity's [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

## Project Description:
Your task is to create a reporting tool that prints out reports (in plain text) 
based on the data in the database. This reporting tool is a Python program 
using the psycopg2 module to connect to the database.
***The database includes three tables:***
1.The authors table includes information about the authors of articles.
2.The articles table includes the articles themselves.
3.The log table includes one entry for each time a user has accessed the site.

#### Questions to Answer:
1. **What are the most popular three articles of all time?**
2. **Who are the most popular article authors of all time?** 
3. **On which days did more than 1% of requests lead to errors?**

### Project contents
* queries.py - main file to run this Logs Analysis Reporting tool
* README.md - instructions to install this reporting tool
* output.txt - output file that will shown on the command prompt
* newsdata.sql - database file

### Technologies:
1. Python
2. Vagrant
3. VirtualBox

### Installation:
1. Install [Vagrant](https://www.vagrantup.com/)
2. Install [VirtualBox](https://www.virtualbox.org/)
3. Install [Python3](https://www.python.org/downloads/)
4. Download database file from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
   Upzip the file and copy into a folder called log_analysis

### How to Run Project

Download the project zip file to you computer and unzip the file then place inside `vagrant/logs-analysis`.

  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  
  ```
    $ vagrant up
  ```
  2. Then Log into this using command:
  
  ```
    $ vagrant ssh
 ```
  3. download database from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

  4. Unzip this file after downloading it. The file inside is called newsdata.sql.

  5. Copy the newsdata.sql file and place inside `vagrant/logs-analysis`.

  6. In terminal Change directory to `vagrant/logs-analysis` and look around with ls.

  7. Load the data in local database using the command:

  ```
    $ psql -d news -f newsdata.sql
  ```
   8. Run queries.py using:
  ```
    $ python queries.py
  ```
Note: queries will take sometime to execute

### Output
```

The most popular three articles of all time
1. Candidate is jerk, alleges rival --- 338647 views
2. Bears love berries, alleges bear --- 253801 views
3. Bad things gone, say good people --- 170098 views

The most popular article authors of all time
1. Ursula La Multa --- 507594 views
2. Rudolf von Treppenwitz --- 423457 views
3. Anonymous Contributor --- 170098 views

Days with more than 1% of requests lead to errors:
July 17, 2016 --- 2.26% errors
```
### Useful Resources
* [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
* [PostgreSQL 9.5 Documentation](https://www.postgresql.org/docs/9.5/static/index.html)
* [Vagrant](https://www.vagrantup.com/downloads)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
# Logs Analysis Project
### by Satheesh Gajula
This is a project for Udacity's [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

## Project Description:
Your task is to create a reporting tool that prints out reports (in plain text) 
based on the data in the database. This reporting tool is a Python program 
using the psycopg2 module to connect to the database.
***The database includes three tables:***
1.The authors table includes information about the authors of articles.
2.The articles table includes the articles themselves.
3.The log table includes one entry for each time a user has accessed the site.

#### Questions to Answer:
1. **What are the most popular three articles of all time?**
2. **Who are the most popular article authors of all time?** 
3. **On which days did more than 1% of requests lead to errors?**

### Project contents
* queries.py - main file to run this Logs Analysis Reporting tool
* README.md - instructions to install this reporting tool
* output.txt - output file that will shown on the command prompt
* newsdata.sql - database file

### Technologies:
1. Python
2. Vagrant
3. VirtualBox

### Installation:
1. Install [Vagrant](https://www.vagrantup.com/)
2. Install [VirtualBox](https://www.virtualbox.org/)
3. Install [Python3](https://www.python.org/downloads/)
4. Download database file from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
   Upzip the file and copy into a folder called log_analysis

### How to Run Project

Download the project zip file to you computer and unzip the file then place inside `vagrant/logs-analysis`.

  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  
  ```
    $ vagrant up
  ```
  2. Then Log into this using command:
  
  ```
    $ vagrant ssh
 ```
  3. download database from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

  4. Unzip this file after downloading it. The file inside is called newsdata.sql.

  5. Copy the newsdata.sql file and place inside `vagrant/logs-analysis`.

  6. In terminal Change directory to `vagrant/logs-analysis` and look around with ls.

  7. Load the data in local database using the command:

  ```
    $ psql -d news -f newsdata.sql
  ```
   8. Run queries.py using:
  ```
    $ python queries.py
  ```
Note: queries will take sometime to execute

### Output
```

The most popular three articles of all time
1. Candidate is jerk, alleges rival --- 338647 views
2. Bears love berries, alleges bear --- 253801 views
3. Bad things gone, say good people --- 170098 views

The most popular article authors of all time
1. Ursula La Multa --- 507594 views
2. Rudolf von Treppenwitz --- 423457 views
3. Anonymous Contributor --- 170098 views

Days with more than 1% of requests lead to errors:
July 17, 2016 --- 2.26% errors
```
### Useful Resources
* [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
* [PostgreSQL 9.5 Documentation](https://www.postgresql.org/docs/9.5/static/index.html)
* [Vagrant](https://www.vagrantup.com/downloads)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
# Log-ananlysis
# Log-ananlysis
