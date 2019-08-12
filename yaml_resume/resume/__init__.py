import yaml
from .contact import Contact
from .profile import Profile
from .experience import Experience
from .skill import Skill
from .language import Language


class Resume(yaml.YAMLObject):
    """Resume object"""
    yaml_tag = u'Resume'

    def __init__(self):
        print("## Contact Informations ##")
        self.contact = Contact.ask()
        print("## Profiles ##")
        self.profiles = Profile.ask()
        print("## Experiences ##")
        self.experiences = Experience.ask()
        print("## Skills ##")
        self.skills = Skill.ask()
        print("## Languages ##")
        self.languages = Language.ask()
