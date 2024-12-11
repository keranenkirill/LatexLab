import unittest
from entities.citation import Citation

class TestCitation(unittest.TestCase):
    def setUp(self):
        self.citation = Citation(
            id="test_id",
            type="article",
            author="Tester",
            title="Testing test",
            year=2024,
            booktitle="Testing Book",
            journal="Journal of Python Testing",
            volume="42",
            pages="123-456",
            publisher="Test Publisher"
        )

    def test_str_method(self):
        output_str = str(self.citation)
        self.assertIn("ID: test_id", output_str)
        self.assertIn("Type: article", output_str)
        self.assertIn("Author: Tester", output_str)
        self.assertIn("Title: Testing test", output_str)
        self.assertIn("Year: 2024", output_str)
        self.assertIn("Booktitle: Testing Book", output_str)
        self.assertIn("Journal: Journal of Python Testing", output_str)
        self.assertIn("Volume: 42", output_str)
        self.assertIn("Pages: 123-456", output_str)
        self.assertIn("Publisher: Test Publisher", output_str)

    def test_to_dict(self):
        expected = {
            'type': "article",
            'author': "Tester",
            'title': "Testing test",
            'year': 2024,
            'booktitle': "Testing Book",
            'journal': "Journal of Python Testing",
            'volume': "42",
            'pages': "123-456",
            'publisher': "Test Publisher"
        }
        self.assertEqual(self.citation.to_dict(), expected)
