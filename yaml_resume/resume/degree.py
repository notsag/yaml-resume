import yaml
import click


class Degree(yaml.YAMLObject):
    """Class corresponding to a line of the education section of a resume.

    :param institution: The name of the institution.
    :type institution: str
    :param degree: The name of the degree.
    :type degree: str
    :param start_date: The start date of the formation.
    :type start_date: str
    :param end_date: The end date of the formation.
    :type end_date: str
    :param website: The webstie of the institution.
    :type website: str

    """

    yaml_tag = u"Degree"

    def __init__(self, institution, degree, start_date, end_date, website):
        self.institution = institution
        self.degree = degree
        self.start_date = start_date
        self.end_date = end_date
        self.website = website

    @staticmethod
    def ask():
        """Interactively create the education section of a resume.

        :returns: A list of Degree objects

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

    @staticmethod
    def load(data):
        """Load dictionary and returns an Degree object.

        :param data: A dictionary loaded from a yaml file.
        :type data: dict[]
        :returns: A Degree object.

        """
        return Degree(
            data.get("institution"),
            data.get("degree"),
            data.get("start_date"),
            data.get("end_date"),
            data.get("website"),
        )
