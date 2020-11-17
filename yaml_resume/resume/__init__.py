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
    """Class corresponding to a full resume.

    :param contact: Contact informations.
    :type contact: Contact
    :param profiles: Profile section of the resume.
    :type profiles: list[Profile]
    :param experiences: Experience section of the resume.
    :type experiences: list[Experience]
    :param education: Education section of the resume.
    :type education: list[Degree]
    :param skills: Skills section of the resume.
    :type skills: list[Skill]
    :param languages: Languages section of the resume.
    :type languages: list[Language]
    :param projects: Projects section of the resume.
    :type projects: list[Project]
    :param hobbies: Hobbies section of the resume.
    :type hobbies: list[Hobby]

    """

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

    @staticmethod
    def ask():
        """Interactively create a Resume object.

        :returns: A Resume object from provided answers.

        """
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
        if click.confirm("Do you want to add a Projects section?", default=False):
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

    @staticmethod
    def load(data):
        """Load dictionary and returns a Resume object.

        :param data: A dictionary loaded from a yaml file.
        :type data: dict[]
        :returns: A Resume object.

        """
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
