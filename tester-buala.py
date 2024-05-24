import unittest
import warnings
from api import app

class APITester(unittest.TestCase):
    def setup(self):
        app.config["TESTING"] = True
        self.app = app.test_client()

        warnings.simplefilter("ignore", category=DeprecationWarning)


    def tester_get_company(self):
        
        response = self.app.get("/company")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Ivern Buala" in response.data.decode())

    def tester_get_company_id(self):

        response = self.app.get("/company/1")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Ivern Buala" in response.data.decode())