import yaml
from yaml_resume import Resume
from yaml_resume.resume.contact import Location, Contact
from yaml_resume.resume.profile import Profile
from yaml_resume.resume.experience import Experience
from yaml_resume.resume.degree import Degree
from yaml_resume.resume.skill import Skill
from yaml_resume.resume.language import Language
from yaml_resume.resume.project import Project
from yaml_resume.resume.hobby import Hobby

data = yaml.load(open("sample.yml", "r"), yaml.SafeLoader)


def test_load_location():
    loc = data.get("contact").get("location")
    location = Location.load(loc)
    assert isinstance(location, Location)
    assert location.address == loc.get("address")
    assert location.city == loc.get("city")
    assert location.zip == loc.get("zip")
    assert location.state == loc.get("state")
    assert location.country == loc.get("country")


def test_load_contact():
    co = data.get("contact")
    contact = Contact.load(co)
    assert isinstance(contact, Contact)
    assert contact.name == co.get("name")
    assert contact.date_of_birth == co.get("date_of_birth")
    assert contact.job == co.get("job")
    assert contact.email == co.get("email")
    assert contact.phone == co.get("phone")


def test_load_profiles():
    profiles = data.get("profiles")
    for pro in profiles:
        profile = Profile.load(pro)
        assert isinstance(profile, Profile)
        assert profile.network == pro.get("network")
        assert profile.url == pro.get("url")


def test_load_experience():
    experiences = data.get("experiences")
    for ex in experiences:
        experience = Experience.load(ex)
        assert isinstance(experience, Experience)
        assert experience.company == ex.get("company")
        assert experience.position == ex.get("position")
        assert experience.start_date == ex.get("start_date")
        assert experience.end_date == ex.get("end_date")
        assert experience.summary == ex.get("summary")
        assert experience.tags == ex.get("tags")
        assert experience.website == ex.get("website")


def test_load_education():
    education = data.get("education")
    for deg in education:
        degree = Degree.load(deg)
        assert isinstance(degree, Degree)
        assert degree.institution == deg.get("institution")
        assert degree.degree == deg.get("degree")
        assert degree.start_date == deg.get("start_date")
        assert degree.end_date == deg.get("end_date")
        assert degree.website == deg.get("website")


def test_load_skills():
    skills = data.get("skills")
    for sk in skills:
        skill = Skill.load(sk)
        assert isinstance(skill, Skill)
        assert skill.name == sk.get("name")
        assert skill.level == sk.get("level")


def test_load_languages():
    languages = data.get("languages")
    for lang in languages:
        language = Language.load(lang)
        assert isinstance(language, Language)
        assert language.name == lang.get("name")
        assert language.level == lang.get("level")


def test_load_projects():
    projects = data.get("projects")
    for proj in projects:
        project = Project.load(proj)
        assert isinstance(project, Project)
        assert project.name == proj.get("name")
        assert project.description == proj.get("description")
        assert project.url == proj.get("url")


def test_load_hobbies():
    hobbies = data.get("hobbies")
    for hob in hobbies:
        hobby = Hobby.load(hob)
        assert isinstance(hobby, Hobby)
        assert hobby.name == hob.get("name")
        assert hobby.details == hob.get("details")


def test_load_resume():
    resume = Resume.load(data)
    assert isinstance(resume, Resume)
