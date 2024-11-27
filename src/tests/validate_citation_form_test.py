import unittest

from entities.citation import Citation
from util import UserInputError, validate_citation_form


class TestCitationValidation(unittest.TestCase):
    def setUp(self):
        self.valid_article_citation = {
            "id": 1,
            "type": "article",
            "author": "testAuthor",
            "title": "testTitle",
            "year": 2002,
            "booktitle": "testBooktitle",
            "journal": "journalTest",
            "volume": "testVolume",
            "pages": "testPages",
            "publisher": "testPublisher"
        }

    def test_valid_citation_does_not_raise_error(self):
        validate_citation_form(self.valid_article_citation)

    def test_invalid_type_gives_error(self):
        self.valid_article_citation["type"] = "invalid_type"
        with self.assertRaises(UserInputError):
            validate_citation_form(self.valid_article_citation)

    def test_invalid_author_gives_error(self):
        self.valid_article_citation["author"] = None
        with self.assertRaises(UserInputError):
            validate_citation_form(self.valid_article_citation)

    def test_negative_year_gives_error(self):
        self.valid_article_citation["year"] = -5
        with self.assertRaises(UserInputError):
            validate_citation_form(self.valid_article_citation)

    def test_negative_year_gives_error(self):
        self.valid_article_citation["year"] = "test"
        with self.assertRaises(UserInputError):
            validate_citation_form(self.valid_article_citation)
