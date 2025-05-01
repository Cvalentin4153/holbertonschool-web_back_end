#!/usr/bin/env python3
"""
Module providing a function to insert a new document in a MongoDB collection.
"""


import pymongo


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: Keyword arguments representing the fields and values
                  of the document to insert.

    Returns:
        The new _id of the inserted document.
    """
    doc = mongo_collection.insert(kwargs)
    return doc.inserted_id
