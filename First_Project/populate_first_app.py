import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'First_Project.settings')

import django
django.setup() #configures project settings

#fake pop script
import random
from First_App.models import AccessRocord, Webpage, Topic
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games'] #here we just created some topics

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t
#general format of get_or_create is a tuple
#that returns object and then sth that is created;
#first element is a refrence to the model instance that method creates;
#entry is created using parameters(random here).


def populate(N=5):
    for entry in range(N):
        top = add_topic() #get topic for the entry
        fake_url = fakegen.url() #create fake data for that entry
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        webpg = Webpage.objects.get_or_create(topic = top, url = fake_url, name = fake_name)[0]
        acc_rec = AccessRocord.objects.get_or_create(name = webpg, date = fake_date)[0]
#if there is a foreign key in the models, we cannot just pass in a string, we need to get an actual name, npr webpg


if __name__ == '__main__':
    print('Populating scripts')
    populate(20)
    print('Populating complete')
