import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')
django.setup()
from question.models import Personality, Activity, Growth, Other
SECRET_KEY = 'dosqb3vsyy5+lwuek9(hjr(@)o0vmzl7gbnhdr24*-h42c-y8$'

# f = open('question.csv', 'r', encoding='UTF8')
# info = []
# 
# rdr = csv.reader(f)
# for row in rdr:
#     field, question = row
#     tuple = (field, question)
#     info.append(tuple)
# f.close()
activity_name = ['major', 'intern', 'class', 'circles', 'competition', 'development',
                 'overseas', 'school', 'volunteer', 'english', 'others', 'major_intelligence']
growth_name = ['environment', 'family', 'others', 'test']

personality_name = ['activate', 'extrovert', 'friendship',
                    'leadership', 'planned', 'sincere', 'random', 'ei', 'jp', 'sn', 'tf']
other_name = ['random']


for filename in activity_name:
    f = open("Q/activity/" + filename + ".txt", 'rt', encoding='UTF8')
    info = []
    while True:
        line = f.readline()
        if not line: break
        info.append(line)
    f.close()

    instances = []
    for question in info:
        instances.append(Activity(title=filename, question=question))

    Activity.objects.bulk_create(instances)

for filename in growth_name:
    f = open("Q/growth/" + filename + ".txt", 'rt', encoding='UTF8')
    info = []
    while True:
        line = f.readline()
        if not line: break
        info.append(line)
    f.close()

    instances = []
    for question in info:
        instances.append(Growth(title=filename, question=question))

    Growth.objects.bulk_create(instances)

for filename in personality_name:
    f = open("Q/personality/" + filename + ".txt", 'rt', encoding='UTF8')
    info = []
    while True:
        line = f.readline()
        if not line: break
        info.append(line)
    f.close()

    instances = []
    for question in info:
        instances.append(Personality(title=filename, question=question))

    Personality.objects.bulk_create(instances)

for filename in other_name:
    f = open("Q/other/" + filename + ".txt", 'rt', encoding='UTF8')
    info = []
    while True:
        line = f.readline()
        if not line: break
        info.append(line)
    f.close()

    instances = []
    for question in info:
        instances.append(Other(title=filename, question=question))

    Other.objects.bulk_create(instances)