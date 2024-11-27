import unittest
from unittest.mock import ANY
from repositories.citation_repository import update_citation
from unittest.mock import patch, MagicMock


class TestUpdateCitation(unittest.TestCase):

    @patch('repositories.citation_repository.db.session')
    def test_update_citation(self, mock_session):

        mock_execute = mock_session.execute
        mock_commit = mock_session.commit

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
