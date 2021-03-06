# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import (
    HiddenField, SubmitField, BooleanField,
    StringField, PasswordField, SelectField,
    TextAreaField
)
from dribdat.user.models import User, Project
from wtforms.fields.html5 import DateTimeField
from wtforms.validators import AnyOf, required, length

from ..user.validators import UniqueValidator
from ..user import USER_ROLE, USER_STATUS, projectProgressList

class UserForm(FlaskForm):
    next = HiddenField()
    id = HiddenField('id')
    username = StringField(u'Username', [required(), length(max=80), UniqueValidator(User, 'username')])
    email = StringField(u'E-mail', [required(), length(max=80)])
    webpage_url = StringField(u'Online profile', [length(max=128)])
    password = PasswordField(u'New password', [length(max=128)])
    is_admin = BooleanField(u"Administrator", default=False)
    active = BooleanField(u"Active", default=True)
    submit = SubmitField(u'Save')

class EventForm(FlaskForm):
    next = HiddenField()
    name = StringField(u'Title', [required(), length(max=80)])
    starts_at = DateTimeField(u'Starts at', description="2020-09-25 09:00:00")
    ends_at = DateTimeField(u'Finishes at', description="2020-09-26 17:00:00")
    is_current = BooleanField(u'Current event shown on homepage', default=False)
    hostname = StringField(u'Hosted by', [length(max=80)])
    location = StringField(u'Located at', [length(max=255)])
    description = TextAreaField(u'Description', description=u'Markdown and HTML supported')
    resources = TextAreaField(u'Guide to datasets and other resources, event page', description=u'Markdown and HTML supported')
    boilerplate = TextAreaField(u'Getting started guide, top of new project page', description=u'Markdown and HTML supported')
    logo_url = StringField(u'Host logo link', [length(max=255)])
    webpage_url = StringField(u'Home page link', [length(max=255)])
    community_url = StringField(u'Community link', [length(max=255)])
    community_embed = TextAreaField(u'Community code, bottom of event and project page', description=u'HTML and embedded scripts supported')
    custom_css = TextAreaField(u'Custom CSS', description=u'External stylesheets: @import url(https://...);')
    submit = SubmitField(u'Save')

class ProjectForm(FlaskForm):
    next = HiddenField()
    id = HiddenField('id')
    user_id = SelectField(u'Owner (team user)', coerce=int)
    event_id = SelectField(u'Event', coerce=int)
    progress = SelectField(u'Progress', coerce=int, choices=projectProgressList())
    hashtag = StringField(u'Hashtag or channel', [length(max=255)])
    autotext_url = StringField(u'Sync', [length(max=255)])
    # is_autoupdate = BooleanField(u'Autoupdate project data')
    name = StringField(u'Title', [required(), length(max=80), UniqueValidator(Project, 'name')])
    category_id = SelectField(u'Category', coerce=int)
    summary = StringField(u'Short summary', [length(max=120)])
    longtext = TextAreaField(u'Description')
    autotext = TextAreaField(u'Readme content')
    webpage_url = StringField(u'Web page link', [length(max=255)])
    source_url = StringField(u'Source code link', [length(max=255)])
    contact_url = StringField(u'Contact link', [length(max=255)])
    image_url = StringField(u'Banner image link', [length(max=255)])
    logo_color = StringField(u'Custom color', [length(max=7)])
    logo_icon = StringField(u'Custom icon', [length(max=20)])
    submit = SubmitField(u'Save')

class CategoryForm(FlaskForm):
    next = HiddenField()
    name = StringField(u'Name', [required(), length(max=80)])
    description = TextAreaField(u'Description', description=u'Markdown and HTML supported')
    logo_color = StringField(u'Custom color', [length(max=7)])
    logo_icon = StringField(u'<a target="_blank" href="http://fontawesome.io/icons/#search">Custom icon</a>', [length(max=20)])
    event_id = SelectField(u'Specific to an event, or global if blank', coerce=int)
    submit = SubmitField(u'Save')
