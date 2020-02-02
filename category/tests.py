from django.test import TestCase, Client
from django.urls import reverse

import json

from .models import Category

# Create your tests here.

c = Client()

class CategoryTest(TestCase):

    def setUp(self):
        data_input = {"name":"Category 1","children":[{"name":"Category 1.1","children":[{"name":"Category 1.1.1","children":[{"name":"Category 1.1.1.1"},{"name":"Category 1.1.1.2"},{"name":"Category 1.1.1.3"}]},{"name":"Category 1.1.2","children":[{"name":"Category 1.1.2.1"},{"name":"Category 1.1.2.2"},{"name":"Category 1.1.2.3"}]}]},{"name":"Category 1.2","children":[{"name":"Category 1.2.1"},{"name":"Category 1.2.2","children":[{"name":"Category 1.2.2.1"},{"name":"Category 1.2.2.2"}]}]}]}
        response = self.client.post('/categories/', json.dumps(data_input), content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_output_view1(self):
        data_output1 = {"id":2,"name":"Category 1.1","parents":[{"id":1,"name":"Category 1"}],"children":[{"id":3,"name":"Category 1.1.1"},{"id":7,"name":"Category 1.1.2"}],"siblings":[{"id":11,"name":"Category 1.2"}]}
        response = self.client.get('/categories/2/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(json.loads(response.content['data']), data_output1)

    def test_output_view2(self):
        data_output2 = {"id":8,"name":"Category 1.1.2.1","parents":[{"id":7,"name":"Category 1.1.2"},{"id":2,"name":"Category 1.1"},{"id":1,"name":"Category 1"},],"children":[],"siblings":[{"id":9,"name":"Category 1.1.2.2"},{"id":10,"name":"Category 1.1.2.3"}]}
        response = self.client.get('/categories/8/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response, data_output2)


