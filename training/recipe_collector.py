from unittest
from training.website_iterator import WebsiteIterator
#from data_loader import training_storer

TEST_SPREADSHEET_ID = '1KQ2nFO9oeDLhHmKh9UTvNnhepKhMuTOyKmh7Nnxbj80'

class RecipeCollector:
    @staticmethod
    def collect_recipe(url, amount_of_rows):
        iterator = WebsiteIterator.get_iterator_for_website(url, amount_of_rows)

    # Iterates over the website and then execute multi insertion.
        cells_list = [], index = 0
        num_of_cells = 0
        result = iterator.next()
        while result is not StopIteration:
            cells_list[index].append(result)
            result = iterator.next()
            training_storer.insert_values(cells_list, target_spreadsheet=TEST_SPREADSHEET_ID)
        return added_cells_count

class TestIteratorAndStorer:
    def __init__(self):
        self.url = "https://www.thekitchencoach.co.il/%d7%9e%d7%92%d7%a0%d7%95%d7%9d-%d7%91%d7%99%d7%aa%d7%99/"

    def test_basic_extract_and_store(self):
        original_spreadsheet = training_storer.get_values(target_spreadsheet=TEST_SPREADSHEET_ID)
        added_cells_count = RecipeCollector.collect_recipe(self.url, 5) # Extracts and then insert.
        updated_spreadsheet = training_storer.get_values(target_spreadsheet=TEST_SPREADSHEET_ID)

        # It is not necessary to check everything - make sure that the first and last cells overlap is enough.
        assert len(updated_spreadsheet) == len(original_spreadsheet) + added_cells_count, "Spreadsheet length mismatch"
        assert original_spreadsheet[0] == updated_spreadsheet[0] and original_spreadsheet[original_spreadsheet.length-1] == updated_spreadsheet[original_spreadsheet.length-1], "First cells or last cells don't match"

        counter = 0
        iterator = WebsiteIterator.get_iterator_for_website(self.url)
        result = iterator.next()
        while result is not StopIteration:
            assert updated_spreadsheet[original_spreadsheet + counter] == result, "Spreadsheet content mismatch"