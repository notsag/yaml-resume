import yaml
from yaml_resume.contact import Contact
from yaml_resume.profile import Profile
from yaml_resume.experience import Experience


class Resume(yaml.YAMLObject):
    """Resume object"""
    yaml_tag = u'Resume'

    def __init__(self):
        self.contact = Contact.ask_contact()
        self.profiles = Profile.ask_profiles()
        self.experiences = Experience.ask_experiences()
