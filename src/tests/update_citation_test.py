import unittest
from unittest.mock import ANY
from unittest.mock import patch
from repositories.citation_repository import update_citation

class PartialDictMatcher:
    def __init__(self, expected):
        self.expected = expected

    def __eq__(self, other):
        return all(other.get(key) == value for key, value in self.expected.items())

    def __repr__(self):
        return f"PartialDictMatcher({self.expected})"

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
            PartialDictMatcher({
                "type": "article",
                "author": "auth",
                "title": "titl",
                "year": "2024",
                "booktitle": "boog",
                "id": 1
            })
        )
