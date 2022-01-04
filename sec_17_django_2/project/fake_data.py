import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()

import random
from app.models import User
from faker import Faker

f = Faker()

def populate(N=5):
    for u in range(N):
        fn = f.first_name()
        ln = f.last_name()
        e = f"{fn[0]}{ln}@{f.email().split('@')[-1]}".lower()

        user = User.objects.get_or_create(first_name=fn,
            last_name=ln,
            email=e)[0]

        user.save()

if __name__ == "__main__":
    print("populatin script ran")
    populate(50)
    print("population complete")