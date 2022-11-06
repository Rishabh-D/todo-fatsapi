from model import Todo
import pymongo #mongodb driver
from pymongo import MongoClient
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
mongo_uri = os.getenv('MONGO_URI')
mongo_db = os.getenv('MONGO_DB')
mongo_document = os.getenv('MONGO_DOCUMENT')
client = MongoClient(mongo_uri)
db = client.mongo_db
collection = db.mongo_document

def fetch_one_todo(title):
  document = collection.find_one({"title":title})
  return document

def fetch_all_todos():
  todos=[]
  cursor = collection.find({})
  for document in cursor:
    todos.append(Todo(**document))
  return todos

def create_todo(todo):
  document = todo
  result = collection.insert_one(document)
  return document

def update_todo_data(title, desc):
  print("in database")
  collection.update_one(
      {"title":title}, 
      {"$set":{
        "description": desc
        }
      }
    )
  print("collection.update ran")
  document = collection.find_one({"title":title})
  print("returning doc", document)
  return document

def remove_todo(title):
  collection.delete_one({"title":title})
  return True