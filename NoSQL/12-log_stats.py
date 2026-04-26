#!/usr/bin/env python3
"""
Provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient 
from typing import List, Dict, Optional


def count(collection, options: Dict[str, str] = {}) -> int:
    """
    Take a mongoDB collection, filter data and count it

    Args:
        collection: MongoDB collection
        options (Dict[str, str]): options to filter
    """
    return collection.count_documents(options)


if __name__ == '__main__':
    client = MongoClient(host="localhost", port=27017)
    collection = client.logs.nginx
    methods: List[str] = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("{:d} logs".format(count(collection)))
    print("Methods:")

    for method in methods:
        print("\tmethod {:s}: {:d}".format(
            method,
            count(collection, {"method": method})
        ))

    print("{:d} status check".format(
        count(collection, {"method": "GET", "path": "/status"})
    ))
