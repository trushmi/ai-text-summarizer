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

if __name__ == '__main__':
    unittest.main()