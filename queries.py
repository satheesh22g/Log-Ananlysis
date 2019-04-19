#! /usr/bin/env python3

import psycopg2
from datetime import datetime


def get_query_result(query):
    # To Connect database
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    db.close()
    return rows


# function for query 1
def top_3_articles():

    query1 = """
        select articles.title, count(title)
        as top_views
        from articles,log
        where log.path LIKE concat('%',articles.slug) and status='200 OK'
        group by articles.title
        order by top_views
        desc limit 3;
    """

    # print query 1 result
    results = get_query_result(query1)

    count = 1
    for i in results:
        print(str(count) + '. ' + i[0] + ' --- ' + str(i[1]) + " views")
        count += 1


# function for query 2
def top_authors():

    # Build Query String
    query2 = """
        select authors.name,count(title)
        as views
        from articles,authors,log
        where log.path LIKE concat('%',articles.slug) and status='200 OK' and
         authors.id = articles.author
          group by authors.name
        order by views
        desc limit 3;

    """

# print query 2 result
    results = get_query_result(query2)

    count = 1
    for i in results:
        print(str(count) + '. ' + i[0] + ' --- ' + str(i[1]) + " views")
        count += 1


# function for query 3
def days_with_errors():
    query3 = """
        select * from (select requests.tdate,
        cast(round((errors.total_errors * 100.00)/requests.total_requests,2)
         as numeric) as error_perc
        from (select count(*) as total_requests,
        date(log.time) as tdate
        from log group by tdate) as requests
        join (select count(*) as total_errors,
        date(log.time) as tdate
        from log where log.status = '404 NOT FOUND' group by tdate) as errors
        on requests.tdate=errors.tdate) as result
        where error_perc > 1;

    """

    # print query 3 result
    results = get_query_result(query3)
    for i in results:
        print(i[0].strftime('%B %d, %Y') + " --- " +
              str(round(i[1], 2)) + "%" + " errors")


# print all three query results.
print('\nThe most popular three articles of all time')
top_3_articles()
print('\nThe most popular article authors of all time')
top_authors()
print('\nDays with more than 1% of requests lead to errors:')
days_with_errors()
