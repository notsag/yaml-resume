import yaml
import click
from .contact import Contact
from .profile import Profile
from .experience import Experience
from .degree import Degree
from .skill import Skill
from .language import Language
from .project import Project
from .hobby import Hobby


class Resume(yaml.YAMLObject):
    """Resume object"""

    yaml_tag = u"Resume"

    def __init__(
        self,
        contact,
        profiles,
        experiences,
        education,
        skills,
        languages,
        projects,
        hobbies,
    ):
        self.contact = contact
        self.profiles = profiles
        self.experiences = experiences
        self.education = education
        self.skills = skills
        self.languages = languages
        self.projects = projects
        self.hobbies = hobbies

    def ask():
        """Prompts questions and return Resume object"""
        print("## Contact Informations ##")
        contact = Contact.ask()
        print("## Profiles ##")
        profiles = Profile.ask()
        print("## Experiences ##")
        experiences = Experience.ask()
        print("## Education ##")
        education = Degree.ask()
        print("## Skills ##")
        skills = Skill.ask()
        print("## Languages ##")
        languages = Language.ask()
        if click.confirm(
            "Do you want to add a Projects section?", default=False
        ):
            print("## Projects ##")
            projects = Project.ask()
        print("## Hobbies ##")
        hobbies = Hobby.ask()
        return Resume(
            contact,
            profiles,
            experiences,
            education,
            skills,
            languages,
            projects,
            hobbies,
        )
