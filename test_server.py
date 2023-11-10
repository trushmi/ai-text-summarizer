import unittest
import server

class TestSummarize(unittest.TestCase):
    def test_summarize(self):
        text = "This is a sample input text for summarization."

        data = {'text': text}

        with server.app.test_client() as client:
            response = client.post('/', json=data)

        self.assertIn('summary', response.json)

    def test_empty_text(self):
        text = ""

        data = {'text': text}

        with server.app.test_client() as client:
            response = client.post('/', json=data)

        self.assertIn('error', response.json)

    def test_summary_length(self):
        text = "This is a sample input text for summarization."

        data = {'text': text}

        with server.app.test_client() as client:
            response = client.post('/', json=data)

        summary = response.json['summary']
        max_length = 120
        min_length = 40
        self.assertGreaterEqual(len(summary), min_length)
        self.assertLessEqual(len(summary), max_length)

if __name__ == '__main__':
    unittest.main()