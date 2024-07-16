#!/usr/bin/env python3
"""all docs"""


def list_all(mongo_collection):
    """Listing all doc in collection"""
    if mongo_collection.find_one() is None:
        return []
    result = mongo_collection.find()
    return result
