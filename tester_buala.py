import unittest
import warnings
from api_buala import app

class TestAPITester(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()
        warnings.simplefilter("ignore", category=DeprecationWarning)

    # Test 1
    def test_get_company(self):
        response = self.app.get("/company")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Ivern Buala" in response.data.decode())

    # Test 2
    def test_get_company_id(self):
        response = self.app.get("/company/1")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Ivern Buala" in response.data.decode())

    # Add
    def test_add_company(self):
        data = {"name": "Ivern Buala", "age": 21, "position": "Founder"}
        response = self.app.post("/company", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue("Ivern Buala" in response.data.decode())


    # Update
    def test_update_company(self):
        # Login to get the token
        login_response = self.app.post('/auth', json={'username': 'admin', 'password': 'password123'})
        self.assertEqual(login_response.status_code, 200)
        token = login_response.json['access_token']

        headers = {
            'Authorization': f'Bearer {token}'
        }

        data = {"name": "Lawrence Apalla", "age": 20, "position": "Co-Founder"}
        response = self.app.put("/company/1", json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Lawrence Apalla" in response.data.decode())

    # Delete
    def test_delete_company(self):
        # Login to get the token
        login_response = self.app.post('/auth', json={'username': 'admin', 'password': 'password123'})
        self.assertEqual(login_response.status_code, 200)
        token = login_response.json['access_token']

        headers = {
            'Authorization': f'Bearer {token}'
        }

        response = self.app.delete("/company/1", headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("deleted successfully" in response.data.decode())

if __name__ == "__main__":
    unittest.main()
