import yaml
import click


class Skill(yaml.YAMLObject):
    """Class corresponding to a skill.

    :param name: The name of the skill.
    :type name: str
    :param level: The level for this skill (0-100).
    :type leve: int

    """

    yaml_tag = u"Skill"

    def __init__(self, name, level):
        self.name = name
        self.level = level

    @staticmethod
    def ask():
        """Interactively create the skills section of a resume.

        :returns: A list of Skill objects.

        """
        skills = []
        continue_adding = True
        correct = False
        while not correct:
            while continue_adding:
                name = click.prompt("Name")
                level = click.prompt(
                    "Level (0-100)",
                    value_proc=lambda x: x if int(x) > 0 and int(x) <= 100 else 0,
                )
                skills.append(Skill(name, int(level)))
                continue_adding = click.confirm("Add a new skill?")
            correct = click.confirm("Is this correct?")
        return skills

    @staticmethod
    def load(data):
        """Load dictionary and returns an Skill object

        :param data: A dictionnary loaded from a yaml file.
        :type data: dict[]
        :returns: A Skill object.

        """
        return Skill(data.get("name"), data.get("level"))
