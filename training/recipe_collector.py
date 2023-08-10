from unittest
from training.website_iterator import WebsiteIterator
#from data_loader import training_storer

class RecipeCollector:
    @staticmethod
    def collect_recipe(url, amount_of_rows):
        iterator = WebsiteIterator.get_iterator_for_website(url, amount_of_rows)

    # Iterates over the website and then execute multi insertion.
        cells_list = [], index = 0
        result = iterator.next()
        while result != StopIteration:
            cells_list[index].append(result)
            result = iterator.next()
            #training_storer.insert_values(cells_list)
class TestIteratorAndStorer:
    def __init__(self):
        self.url = "https://www.thekitchencoach.co.il/%d7%9e%d7%92%d7%a0%d7%95%d7%9d-%d7%91%d7%99%d7%aa%d7%99/"
        self.expected_response = "" #TODO: Add here the response
    def test_basic_extract_and_store(self):
        orignal_spreadsheet = training_storer.get_values() #Fetch the sheet (before the changes)
        RecipeCollector.collect_recipe(self.url, 5) # Extracts and then insert.
        updated_spreadsheet = training_storer.get_values() #Fetch the sheet again (after the changes made)
        #TODO: Check if it was append properly (according checking the original and the updated)