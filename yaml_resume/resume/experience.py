import yaml
import click


class Experience(yaml.YAMLObject):
    """Experience object"""
    yaml_tag = u'Experience'

    def __init__(self, company, position, startDate, endDate, summary, tags):
        self.company = company
        self.position = position
        self.startDate = startDate
        self.endDate = endDate
        self.summary = summary
        self.tags = tags

    def ask():
        """
        Prompt questions for experiences section
        returns a list of Experience objects
        """
        experiences = []
        continue_adding = True
        correct = False
        while not correct:
            while continue_adding:
                company = click.prompt("What is the name of the company?")
                position = click.prompt("What is/was your position?")
                startDate = click.prompt("When did you start working there?")
                endDate = click.prompt(
                    "When did you stop working there?", default=""
                    )
                summary = ""
                summary_adding = True
                while summary_adding:
                    summary = summary + click.prompt("Summary:") + "\n"
                    summary_adding = click.confirm(
                        "Continue summary?", default=True
                        )
                tags = click.prompt(
                    "Add tags? (1 word/1 tag)", default=""
                    ).split()
                experiences.append(
                     Experience(
                         company, position, startDate, endDate, summary, tags
                         )
                     )
                continue_adding = click.confirm("Add a new experience?")
            correct = click.confirm("Is this correct?")
        return experiences
