import yaml
import click


class Project(yaml.YAMLObject):
    """Project object"""
    yaml_tag = u'Project'

    def __init__(self, name, description, url):
        self.name = name
        self.description = description
        self.url = url

    def ask():
        """
        Prompt questions for projects section
        returns a list of Project objects
        """
        projects = []
        continue_adding = True
        correct = False
        while not correct:
            while continue_adding:
                name = click.prompt("What project did you work on?")
                description = click.prompt("Can you give a brief description?")
                url = click.prompt("What is the URL of the project?")
                projects.append(Project(name, description, url))
                continue_adding = click.confirm("Add a new project?")
            correct = click.confirm("Is this correct?")
        return projects
