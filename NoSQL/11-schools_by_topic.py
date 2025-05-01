#!/usr/bin/env python3
"""
Module providing a function to find schools by topic.
"""


import pymongo
from typing import List, Dict


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school documents having a specific topic.
    """
    query = {"topic": topic}
    matching_schools = list(mongo_collection.find(query))
    return matching_schools
