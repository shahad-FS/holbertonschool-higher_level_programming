#!/usr/bin/python3
"""Module contains API request"""
import requests
import csv


url = 'https://jsonplaceholder.typicode.com/posts'

def fetch_and_print_posts():
    """
    Functio send request to url and print response
    """
    request = requests.get(url)
    print(f"Status Code: {requests.status_codes}")
    if request.status_code == 200:
        data = request.json()

        for row in data:
            title = row['title']
            print(title)

def fetch_and_save_posts():
    """
    Function send request to url
    save response in csv file
    """
    data_list = []
    csv_file = 'posts.csv'
    request = requests.get(url)
    print(f"Status Code: {requests.status_codes}")
    if request.status_code == 200:
        data = request.json()
        for item in data:
            post = {
                'id': item['id'],
                'title': item['title'],
                'body': item['body']
            }
            data_list.append(post)

        with open(csv_file, 'w') as file:
            write = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            write.writeheader()
            write.writerows(data_list)

    else:
        print("Request was not successful.")
