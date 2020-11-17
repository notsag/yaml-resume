import yaml
import click


class Experience(yaml.YAMLObject):
    """Class corresponding to an item of the experience section of a resume.

    :param company: The name of the company.
    :type company: str
    :param position: The job title.
    :type position: str
    :param start_date: The start date of the experience.
    :type start_date: str
    :param end_date: The end date of the experience.
    :type end_date: str
    :param summary: The description of the experience.
    :type summary: str
    :param tags: A list of tags corresponding to the experience.
    :type tags: list[str]
    :param website: The website of the company
    :type website: str

    """

    yaml_tag = u"Experience"

    def __init__(self, company, position, start_date, end_date, summary, tags, website):
        self.company = company
        self.position = position
        self.start_date = start_date
        self.end_date = end_date
        self.summary = summary
        self.tags = tags
        self.website = website

    @staticmethod
    def ask():
        """Interactively create the experience section of the resume.

        :returns: A list of Experience objects.

        """
        experiences = []
        continue_adding = True
        correct = False
        while not correct:
            while continue_adding:
                company = click.prompt("Company")
                position = click.prompt("Position")
                start_date = click.prompt("Start date")
                end_date = click.prompt("End date", default="")
                summary = ""
                buffer = False
                while buffer != "":
                    if buffer is not False:
                        summary += buffer + "\n"
                    buffer = click.prompt("Summary (empty line to finish)", default="")
                tags = click.prompt("Tags (use space between tags)", default="").split()
                website = click.prompt("Website (optional)")
                experiences.append(
                    Experience(
                        company, position, start_date, end_date, summary, tags, website
                    )
                )
                continue_adding = click.confirm("Add a new experience?")
            correct = click.confirm("Is this correct?")
        return experiences

    @staticmethod
    def load(data):
        """Load dictionary and returns an Experience object.

        :param data: A dictionary loaded from a yaml file.
        :type data: dict[]
        :returns: An Experience object.

        """
        return Experience(
            data.get("company"),
            data.get("position"),
            data.get("start_date"),
            data.get("end_date"),
            data.get("summary"),
            data.get("tags"),
            data.get("website"),
        )
