#!/usr/bin/env python3
"""
Module providing a function to find schools by topic.
"""


import pymongo
from typing import List, Dict


def schools_by_topic(mongo_collection, topic: str) -> List[Dict]:
    """
    Returns the list of school documents having a specific topic.
    """
    return list(mongo_collection.find({"topic": topic}))
