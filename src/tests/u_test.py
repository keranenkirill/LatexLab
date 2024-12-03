import unittest
from unittest.mock import ANY, patch
from util import UserInputError, validate_citation_form
from repositories.citation_repository import del_citation, update_citation


class TestDeleteCitation(unittest.TestCase):

    @patch('repositories.citation_repository.db.session')
    def test_delete_citation(self, mock_session):
        mock_execute = mock_session.execute
        mock_commit = mock_session.commit

        citation_id = 1

        del_citation(citation_id)

        mock_execute.assert_called_once_with(
            ANY,
            {"id": citation_id}
        )

        mock_commit.assert_called_once()


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

    def test_str_as_year_gives_error(self):
        self.valid_article_citation["year"] = "test"
        with self.assertRaises(UserInputError):
            validate_citation_form(self.valid_article_citation)


class TestUpdateCitation(unittest.TestCase):

    @patch('repositories.citation_repository.db.session')
    def test_update_citation(self, mock_session):
        mock_execute = mock_session.execute

        citation_id = 1
        citation = {
            "type": "article",
            "author": "auth",
            "title": "titl",
            "year": "2024",
            "booktitle": "boog"
        }

        update_citation(citation_id, citation)

        mock_execute.assert_called_once_with(
            ANY,
            {
                "type": "article",
                "author": "auth",
                "title": "titl",
                "year": "2024",
                "booktitle": "boog",
                "id": 1
            }
        )
