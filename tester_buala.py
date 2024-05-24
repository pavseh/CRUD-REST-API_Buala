import unittest
import warnings
from api_buala import app

class TestAPITester(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()
        warnings.simplefilter("ignore", category=DeprecationWarning)


    def test_get_company(self):
        response = self.app.get("/company")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Ivern Buala" in response.data.decode())


    def test_get_company_id(self):
        response = self.app.get("/company/1")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Ivern Buala" in response.data.decode())


    def test_add_company(self):
        data = {"name": "Ivern Buala", "age": 21, "position": "Founder"}
        response = self.app.post("/company", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue("Ivern Buala" in response.data.decode())

    def test_update_company(self):
        data = {"name": "Lawrence Apalla", "age": 20, "position": "Co-Founder"}
        response = self.app.put("/company/1", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Lawrence Apalla" in response.data.decode())

    def test_delete_company(self):
        response = self.app.delete("/company/1")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("deleted successfully" in response.data.decode())


if __name__ == "__main__":
    unittest.main()