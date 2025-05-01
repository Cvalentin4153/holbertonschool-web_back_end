#!/usr/bin/env python3
"""
Module providing a function to list all documents in a MongoDB collection.
"""


import pymongo


def list_all(mongo_collection):
    """Lists all documents in a MongoDB collection.

    Args:
        mongo_collection: A pymongo collection object.

    Returns:
        A list containing all documents found in the collection,
        or an empty list if the collection is empty or does not exist.
    """
    cursor = mongo_collection.find()
    all_docs = list(cursor)
    return all_docs
