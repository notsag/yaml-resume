import yaml
from yaml_resume.contact import Contact


class Resume(yaml.YAMLObject):
    """Resume object"""
    yaml_tag = u'Resume'

    def __init__(self):
        self.contact = Contact()
