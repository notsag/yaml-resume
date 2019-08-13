import yaml
import click


class Language(yaml.YAMLObject):
    """Language object"""

    yaml_tag = u"Language"

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def ask():
        """
        Prompt questions for languages section
        returns a list of Language objects
        """
        languages = []
        continue_adding = True
        correct = False
        while not correct:
            while continue_adding:
                name = click.prompt("What language do you want to add?")
                level = click.prompt("How well do you speak " + name + "?")
                languages.append(Language(name, level))
                continue_adding = click.confirm("Add a new language?")
            correct = click.confirm("Is this correct?")
        return languages
