#!/usr/bin/env python3
"""
Module providing a function to find schools by topic.
"""


import pymongo
from typing import List


def schools_by_topic(mongo_collection, topic: str) -> List[dict]:
    """Returns the list of school documents having a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic (str): The topic searched.

    Returns:
        List[dict]: A list of school documents that contain the specified topic
        in their 'topics' list.
    """

    return mongo_collection.find({"topic": topic})
