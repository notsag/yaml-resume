import yaml
from .contact import Contact
from .profile import Profile
from .experience import Experience
from .skill import Skill


class Resume(yaml.YAMLObject):
    """Resume object"""
    yaml_tag = u'Resume'

    def __init__(self):
        print("## Contact Informations ##")
        self.contact = Contact.ask_contact()
        print("## Profiles ##")
        self.profiles = Profile.ask_profiles()
        print("## Experiences ##")
        self.experiences = Experience.ask_experiences()
        print("## Skills ##")
        self.skills = Skill.ask_skills()
