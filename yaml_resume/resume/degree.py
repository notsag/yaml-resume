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
                institution = click.prompt("Institution")
                degree = click.prompt("Degree")
                start_date = click.prompt("Start date")
                end_date = click.prompt("End date (optional)", default="")
                website = click.prompt("Website (optional)", default="")
                education.append(
                    Degree(institution, degree, start_date, end_date, website)
                )
                continue_adding = click.confirm("Add a new degree?")
            correct = click.confirm("Is this correct?")
        return education
