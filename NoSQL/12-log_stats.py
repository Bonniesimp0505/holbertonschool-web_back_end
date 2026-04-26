#!/usr/bin/env python3
"""
Provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient
from typing import List, Dict


def count(collection, options: Dict[str, str] = {}) -> int:
    """
    Take a mongoDB collection, filter data and count it
    """
    return collection.count_documents(options)


if __name__ == '__main__':
    client = MongoClient('mongodb://localhost:27017')
    collection = client.logs.nginx

    methods: List[str] = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{count(collection)} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {count(collection, {'method': method})}")
    print(f"{count(collection, {'method': 'GET', 'path': '/status'})} status check")
