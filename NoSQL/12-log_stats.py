#!/usr/bin/env python3
""" Script que proporciona estadísticas sobre logs de Nginx en MongoDB """
from pymongo import MongoClient


def log_stats():
    """ Procesa y muestra estadísticas de la colección nginx """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Total de documentos
    total_logs = nginx_collection.count_documents({})
    print("{} logs".format(total_logs))

    # Conteo por métodos
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    # Conteo específico para status check
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print("{} status check".format(status_check))


if __name__ == "__main__":
    log_stats()
