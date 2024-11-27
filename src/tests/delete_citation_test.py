import unittest
from unittest.mock import ANY
from unittest.mock import patch
from repositories.citation_repository import del_citation


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
