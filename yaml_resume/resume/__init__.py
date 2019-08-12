import yaml
from .contact import Contact
from .profile import Profile
from .experience import Experience
from .skill import Skill
from .language import Language
from .project import Project


class Resume(yaml.YAMLObject):
    """Resume object"""
    yaml_tag = u'Resume'

    def __init__(
                self,
                contact,
                profiles,
                experiences,
                skills,
                languages,
                projects
                ):
        self.contact = contact
        self.profiles = profiles
        self.experiences = experiences
        self.skills = skills
        self.languages = languages
        self.projects = projects

    def ask():
        print("## Contact Informations ##")
        contact = Contact.ask()
        print("## Profiles ##")
        profiles = Profile.ask()
        print("## Experiences ##")
        experiences = Experience.ask()
        print("## Skills ##")
        skills = Skill.ask()
        print("## Languages ##")
        languages = Language.ask()
        print("## Projects ##")
        projects = Project.ask()
        return Resume(
                contact,
                profiles,
                experiences,
                skills,
                languages,
                projects
                )
