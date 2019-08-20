from cerberus import Validator
from . import schema
import yaml


def validate(resume):
    """Use cerberus.Validator to check file against schema.

    :param resume: The path of the resume to validate
    :type resume: str.
    :returns: Tuple -- return code, errors

    """
    v = Validator(schema.resume)
    document = yaml.load(open(resume, "r"), Loader=yaml.FullLoader)
    return (v.validate(document), v.errors)
