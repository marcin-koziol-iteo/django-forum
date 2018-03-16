from .models import Section, Topic, Comment
from django.contrib.auth.models import User

def find_sections(search):
    return Section.objects.filter(name__contains=search)

def topics_by_section_name(name):
    return Topic.objects.filter(section__name=name)

def topic_by_title(title, section_name):
    if Topic.objects.filter(title=title, section__name=section_name):
        return Topic.objects.filter(title=title, section__name=section_name)[0]

def section_by_name(name):
    if Section.objects.filter(name=name):
        return Section.objects.filter(name=name)[0]

def comments_for_topic(topic_name):
    return Comment.objects.filter(topic__title=topic_name)

def check_login(login):
    if len(User.objects.filter(username=login)) > 0:
        return True
    else:
        return False
    
def add_user(login, password, email):
    user = User.objects.create(username=login, password=password, email=email)
    user.set_password(password)
    user.save()