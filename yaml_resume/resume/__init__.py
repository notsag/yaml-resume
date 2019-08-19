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

    def load(data):
        """Load dictionary and returns a Resume object"""
        contact = Contact.load(data.get("contact"))
        profiles = []
        for profile in data.get("profiles"):
            profiles.append(Profile.load(profile))
        experiences = []
        for ex in data.get("experiences"):
            experiences.append(Experience.load(ex))
        education = []
        for degree in data.get("education"):
            education.append(Degree.load(degree))
        skills = []
        for skill in data.get("skills"):
            skills.append(Skill.load(skill))
        languages = []
        for lang in data.get("languages"):
            languages.append(Language.load(lang))
        projects = []
        for project in data.get("projects"):
            projects.append(Project.load(project))
        hobbies = []
        for hobby in data.get("hobbies"):
            hobbies.append(Hobby.load(hobby))
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
