import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'userbase.settings')

import django
django.setup()

import random
from exercise.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        f_name = fakegen.name().split(' ')[0]
        f_lname = fakegen.name().split(' ')[1]
        f_mail = fakegen.email()
        usr = User.objects.get_or_create(fname=f_name,
                                        lname=f_lname, email=f_mail)[0]


if __name__ == '__main__':
    print('Population script!')
    populate(200)
    print('Complete!')
