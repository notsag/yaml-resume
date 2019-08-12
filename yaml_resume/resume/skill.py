import yaml
import click


class Skill(yaml.YAMLObject):
    """Skill object"""
    yaml_tag = u'Skill'

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def ask_skills():
        """
        Prompt questions for skills section
        returns a list of Skill objects
        """
        skills = []
        continue_adding = True
        correct = False
        while not correct:
            while continue_adding:
                name = click.prompt("What skill do you want to add?")
                level = click.prompt("What level do you have? (0-100)")
                skills.append(Skill(name, int(level)))
                continue_adding = click.confirm("Add a new skill?")
            correct = click.confirm("Is this correct?")
        return skills
