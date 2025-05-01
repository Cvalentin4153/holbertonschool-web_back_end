#!/usr/bin/env python3

import pymongo
from typing import List

def schools_by_topic(mongo_collection, topic: str) -> List[dict]:
    return mongo_collection.find({"topic": topic})
