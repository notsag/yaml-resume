import yaml
import click


class Degree(yaml.YAMLObject):
    """Degree object"""

    yaml_tag = u"Degree"

    def __init__(self, institution, degree, start_date, end_date, website):
        self.institution = institution
        self.degree = degree
        self.start_date = start_date
        self.end_date = end_date
        self.website = website

    def ask():
        """
        Prompt questions for education section
        returns a list of Degree objects
        """
        education = []
        continue_adding = True
        correct = False
        while not correct:
            while continue_adding:
                institution = click.prompt(
                    "What is the name of the institution?"
                )
                degree = click.prompt("What your degree did you prepare?")
                start_date = click.prompt("When did you start?")
                end_date = click.prompt(
                    "When did you stop?", default=start_date
                )
                website = click.prompt(
                    "What is the website of the institution?"
                )
                education.append(
                    Degree(institution, degree, start_date, end_date, website)
                )
                continue_adding = click.confirm("Add a new degree?")
            correct = click.confirm("Is this correct?")
        return education
