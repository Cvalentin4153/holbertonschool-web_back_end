#!/usr/bin/env python3
"""
nginx_stats.py:
Connects to the 'logs' database, 'nginx' collection,
and prints out:
 - total number of logs
 - per-method counts for GET, POST, PUT, PATCH, DELETE
 - number of GET /status requests
"""

from pymongo import MongoClient


def main():
    # 1) Connect to MongoDB on localhost:27017
    client = MongoClient()

    # 2) Select the 'logs' database and 'nginx' collection
    db = client.logs
    nginx = db.nginx

    # 3) Total number of documents
    total = nginx.count_documents({})
    print(f"{total} logs")

    # 4) Methods breakdown
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # 5) Count of GET /status
    status_count = nginx.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_count} status check")


if __name__ == "__main__":
    main()
