class UserInputError(Exception):
    pass


def validate_citation_form(content: dict):
    type = content.get('type')
    author = content.get('author')
    title = content.get('title')
    year = content.get('year')

    if 'article' not in type:
        raise UserInputError("Please give a valid citation type")

    if not author or not title or not year:
        raise UserInputError("Please fill all necessary fields")

    try:
        year = int(year)
    except ValueError:
        raise UserInputError("Year must be an integer")

    if year < 1:
        raise UserInputError("Year must be a positive number")
