import yaml
import click


class Experience(yaml.YAMLObject):
    """Experience object"""

    yaml_tag = u"Experience"

    def __init__(
        self, company, position, start_date, end_date, summary, tags, website
    ):
        self.company = company
        self.position = position
        self.start_date = start_date
        self.end_date = end_date
        self.summary = summary
        self.tags = tags
        self.website = website

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
                company = click.prompt("Company")
                position = click.prompt("Position")
                start_date = click.prompt("Start date")
                end_date = click.prompt("End date", default="")
                summary = ""
                buffer = False
                while buffer != "":
                    if buffer is not False:
                        summary += buffer + "\n"
                    buffer = click.prompt(
                        "Summary (empty line to finish)", default=""
                    )
                tags = click.prompt(
                    "Tags (use space between tags)", default=""
                ).split()
                website = click.prompt("Website (optional)")
                experiences.append(
                    Experience(
                        company,
                        position,
                        start_date,
                        end_date,
                        summary,
                        tags,
                        website,
                    )
                )
                continue_adding = click.confirm("Add a new experience?")
            correct = click.confirm("Is this correct?")
        return experiences
