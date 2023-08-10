from utils import text_extractor

class WebsiteIterator:
    def __init__(self, url, amount_of_rows):
        self.url = url
        self.content = text_extractor.get_all_text_from_url(url)
        self.amount_of_rows = amount_of_rows
        self.index = 0
        self.content_length = len(self.content)

    def next(self):
        lines = self.content.splitlines()
        end_index = self.index + self.amount_of_rows
        if end_index >= self.content_length:
            end_index = self.content_length - self.index
        if self.index >= self.content_length:
            raise StopIteration
        else:
            result = lines[self.index:end_index]
            self.index += self.amount_of_rows
            return result

    def get_iterator_for_website(url, amount_of_rows=5):
        return WebsiteIterator(url, amount_of_rows)