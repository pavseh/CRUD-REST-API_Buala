import unittest
import warnings
from api import app

class TestAPITester(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()

        warnings.simplefilter("ignore", category=DeprecationWarning)


    def tester_get_company(self):
        response = self.app.get("/ivernstudios")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Ivern Buala" in response.data.decode())


    def tester_get_company_id(self):
        response = self.app.get("/ivernstudios/1")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Ivern Buala" in response.data.decode())


    def tester_add_company(self):
        data = {"name": "Ivern Buala", "age": 21, "position": "Founder"}
        response = self.app.post("/ivernstudios", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue("Ivern Buala" in response.data.decode())

    def tester_update_company(self):
        data = {"name": "Lawrence Apalla", "age": 20, "position": "Co-Founder"}
        response = self.app.put("/ivernstudios/1", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Lawrence Apalla" in response.data.decode())

    def tester_delete_company(self):
        response = self.app.delete("/ivernstudios/1")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("deleted successfully" in response.data.decode())


if __name__ == "__tester__":
    unittest.main()