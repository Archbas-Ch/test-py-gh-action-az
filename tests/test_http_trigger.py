import unittest
import azure.functions as func
from HttpTrigger import main


class TestHttpTrigger(unittest.TestCase):
    def test_http_trigger_with_name_in_params(self):
        # Construct a mock HTTP request.
        req = func.HttpRequest(
            method='GET',
            body=b'',
            url='/api/HttpTrigger',
            params={'name': 'Test'}
        )

        # Call the function.
        resp = main(req)

        # Check the output.
        self.assertEqual(
            resp.get_body(),
            b"Hello, Test. This HTTP triggered function executed successfully."
        )
        self.assertEqual(resp.status_code, 200)

    def test_http_trigger_with_name_in_body(self):
        # Construct a mock HTTP request.
        req = func.HttpRequest(
            method='POST',
            body=b'{"name": "Test"}',
            url='/api/HttpTrigger'
        )

        # Call the function.
        resp = main(req)

        # Check the output.
        self.assertEqual(
            resp.get_body(),
            b"Hello, Test. This HTTP triggered function executed successfully."
        )
        self.assertEqual(resp.status_code, 200)

    def test_http_trigger_without_name(self):
        # Construct a mock HTTP request.
        req = func.HttpRequest(
            method='GET',
            body=b'',
            url='/api/HttpTrigger'
        )

        # Call the function.
        resp = main(req)

        # Check the output.
        self.assertIn(
            b"This HTTP triggered function executed successfully",
            resp.get_body()
        )
        self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()
