import unittest
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        ','.join(SUPPORTED) in rv.data

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        self.assertEquals('{ "imie":"Piotr", "mgs":Witaj Swiecie!"}', rv.data)
    def test_msg_with_given_output(self):
	imie_test= "Maria"
	rv = self.app.get('/?output=jason'+imie_test)
	self.asserEquals('{ "imie":'+imie_test+', "mgs":Witaj Swiecie!"}', rv.data)
