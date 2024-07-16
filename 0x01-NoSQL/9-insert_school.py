#!/usr/bin/env python3
"""insert a doc"""


def insert_school(mongo_collection, **kwargs):
    """inserting a doc in collection"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
