import os
import django 
from faker import Faker
import random 

#configure settings for project 
os.environ.setdefault('DJANGO_SETTINGS_NODULE', 'locallibrary.settings')

#load the Django projects's settings 
django.setup()

#importing the models
from catalog.models import Genre, Book, LibraryCopy, Author, Language

#Creating Faker instance 

fake = Faker()
Faker.seed(1) #to generate consistent sample data 