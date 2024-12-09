class UserInputError(Exception):
    pass


def validate_citation_form(content: dict):
    citation_type = content.get('type')
    author = content.get('author')
    title = content.get('title')
    year = content.get('year')

    valid_types = ['article', 'inproceeding', 'book']

    if citation_type not in valid_types:
        raise UserInputError("Please give a valid citation type")

    if not author or not title or not year:
        raise UserInputError("Please fill all necessary fields")

    try:
        year = int(year)
    except ValueError as exc:
        raise UserInputError("Year must be an integer") from exc

    if year < 1:
        raise UserInputError("Year must be a positive number")
