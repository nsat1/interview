import unittest
from unittest.mock import patch


class TestAnimalSearch(unittest.TestCase):

    @patch("requests.get")
    def test_get_animal_count(self, mock_get):

        mock_html = """
        <div class="mw-category-group">
            <ul>
                <li>Аист</li>
                <li>Барсук</li>
                <li>Белка</li>
            </ul>
        </div>
        """
        mock_get.return_value.text = mock_html

        expected_count = {"А": 1, "Б": 2}

if __name__ == '__main__':
    unittest.main()
