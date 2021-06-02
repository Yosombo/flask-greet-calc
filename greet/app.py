from flask import Flask, request
app = Flask(__name__)


@app.route('/welcome')
def wwelcome():
    return 'welcome'


@app.route('/welcome/home')
def welcome_home():
    return 'welcome home'


@app.route('/welcome/back')
def welcome_back():
    return 'welcome back'
    # from app import app
    # import unittest

    # class TestSimpleRoutes(unittest.TestCase):

    #     def test_welcome(self):
    #         tester = app.test_client(self)
    #         response = tester.get('/welcome', content_type='html/text')
    #         self.assertIn(b'welcome', response.data.lower())
    #         self.assertEqual(response.status_code, 200)

    #     def test_welcome_home(self):
    #         tester = app.test_client(self)
    #         response = tester.get('/welcome/home', content_type='html/text')
    #         self.assertIn(b'welcome home', response.data.lower())
    #         self.assertEqual(response.status_code, 200)

    #     def test_welcome_back(self):
    #         tester = app.test_client(self)
    #         response = tester.get('/welcome/back', content_type='html/text')
    #         self.assertIn(b'welcome back', response.data.lower())
    #         self.assertEqual(response.status_code, 200)
