from django.test import TestCase, Client
from django.urls import reverse

import json

from .models import Category

# Create your tests here.

c = Client()


class CategoryTest(TestCase):

    def setUp(self):
        data_input = {"name":"Category 1","children":[{"name":"Category 1.1","children":[{"name":"Category 1.1.1","children":[{"name":"Category 1.1.1.1"},{"name":"Category 1.1.1.2"},{"name":"Category 1.1.1.3"}]},{"name":"Category 1.1.2","children":[{"name":"Category 1.1.2.1"},{"name":"Category 1.1.2.2"},{"name":"Category 1.1.2.3"}]}]},{"name":"Category 1.2","children":[{"name":"Category 1.2.1"},{"name":"Category 1.2.2","children":[{"name":"Category 1.2.2.1"},{"name":"Category 1.2.2.2"}]}]}]}
        response = self.client.generic("POST", "/categories/", json.dumps(data_input))

    # def test_input_post_json(self):
        # global data_input
        # response = self.client.post('/categories/', json.dumps(data_input), content_type="application/json")
        # response = self.client.generic("POST", "/categories/", json.dumps(data_input))
        # self.assertEqual(response.status_code, 200)

    def test_data_in_base(self):
        # global data_input
        # response = self.client.generic("POST", "/categories/", json.dumps(data_input))
        answer1 = Category.objects.get(id=2)
        answer2 = Category.objects.get(id=8)
        self.assertEqual(answer1.number, "1.1")
        self.assertEqual(answer2.number, "1.1.2.1")

    def test_output_view1(self):
        data_output1 = {"id":2,"name":"Category 1.1","parents":[{"id":1,"name":"Category 1"}],"children":[{"id":3,"name":"Category 1.1.1"},{"id":7,"name":"Category 1.1.2"}],"siblings":[{"id":11,"name":"Category 1.2"}]}
        response = self.client.get("/categories/2/")
        self.assertEqual(response.status_code,200)
        print(response.content)
        # self.assertEqual(json.loads(response.content['data']), json.dumps(data_output1))
        self.assertEqual(json.loads(response.content), data_output1)

    def test_output_view2(self):
        data_output2 = {"id":8,"name":"Category 1.1.2.1","parents":[{"id":7,"name":"Category 1.1.2"},{"id":2,"name":"Category 1.1"},{"id":1,"name":"Category 1"},],"children":[],"siblings":[{"id":9,"name":"Category 1.1.2.2"},{"id":10,"name":"Category 1.1.2.3"}]}
        response = self.client.get('/categories/8/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(json.loads(response.content), data_output2)


