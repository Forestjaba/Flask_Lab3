import unittest
from unittest import main
from trig import app
import requests


class TrigTest(unittest.TestCase):

    def test_connect(self):
        URL = "http://127.0.0.1:5000"
        r = requests.get(URL)
        self.assertEqual(r.status_code, 200)

    def test_sin_degrees(self):
        tester = app.test_client(self)
        response = tester.post("/", content_type='multipart/form-data',
                               data={'angle': '240', 'function': 'Sin', 'unit': 'degrees', 'precision': '3'})
        self.assertIn('-0.866', response.data.decode())

    def test_cos_degrees(self):
        tester = app.test_client(self)
        response = tester.post("/", content_type='multipart/form-data',
                               data={'angle': '60', 'function': 'Cos', 'unit': 'degrees', 'precision': '3'})
        self.assertIn('0.5', response.data.decode())

    def test_tg_degrees(self):
        tester = app.test_client(self)
        response = tester.post("/", content_type='multipart/form-data',
                               data={'angle': '30', 'function': 'Tg', 'unit': 'degrees', 'precision': '3'})
        self.assertIn('0.577', response.data.decode())

    def test_ctg_degrees(self):
        tester = app.test_client(self)
        response = tester.post("/", content_type='multipart/form-data',
                               data={'angle': '80', 'function': 'Ctg', 'unit': 'degrees', 'precision': '3'})
        self.assertIn('0.176', response.data.decode())


if __name__ == "__main__":
    main()