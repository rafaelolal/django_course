import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
from first_app.models import Topic, WebPage, AccessRecord
from faker import Faker

f = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()
        
        fake_url = f.url()
        fake_date = f.date()
        fake_name = f.company()

        page = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        record = AccessRecord.objects.get_or_create(name=page, date=fake_date)[0]

if __name__ == "__main__":
    print("populatin script ran")
    populate(20)
    print("population complete")