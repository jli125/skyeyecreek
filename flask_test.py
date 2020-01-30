from app import app
import unittest

class FlaskappTests(unittest.TestCase):
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def test_users_status_code(self):
        # send HTTP GET request to the application
        result = self.app.get('/api/v1/users')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_tweets_status_code(self):
        # send HTTP GET request to the application
        result = self.app.get('/api/v2/tweets')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_info_status_code(self):
        # send HTTP GET request to the application
        result = self.app.get('/api/v1/info')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_addusers_status_code(self):
        # send HTTP POST request to the application
        result = self.app.post('/api/v1/users', data='{"username":"jli125","email":"jli125@123.com","password":"test123"}',content_type='application/json')
        print(result)
        # assert the status code of the response
        self.assertEqual(result.status_code, 201)

    def test_updusers_status_code(self):
        # send HTTP PUT request to the application
        result = self.app.put('/api/v1/users/26', data='{"password":"test456"}',content_type='application/json')
        print(result)
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_addtweets_status_code(self):
        # send HTTP POST request to the application
        result = self.app.post('/api/v2/tweets', data='{"username":"jli125@rocks","body":"WoW! It is in working #testing"}',content_type='application/json')
        print(result)
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_delusers_status_code(self):
        # send HTTP Delete request to the application
        result = self.app.delete('/api/v1/users', data='{"username":"jli125"}',content_type='application/json')
        print(result)
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)
