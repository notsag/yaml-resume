import yaml
from yaml_resume.contact import Contact
from yaml_resume.profile import Profile


class Resume(yaml.YAMLObject):
    """Resume object"""
    yaml_tag = u'Resume'

    def __init__(self):
        self.contact = Contact.ask_contact()
        self.profiles = Profile.ask_profiles()
