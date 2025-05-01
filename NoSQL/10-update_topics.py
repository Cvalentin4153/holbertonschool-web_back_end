#!/usr/bin/env python3
"""
Module providing a function to update topics of a school document.
"""


import pymongo
from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]):
    """Changes all topics of a school document based on the name.

    Args:
        mongo_collection: The pymongo collection object.
        name (str): The school name to update.
        topics (List[str]): The list of topics approached in the school.
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
