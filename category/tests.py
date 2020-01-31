from django.test import TestCase
from django.urls import reverse

from .models import Category
# Create your tests here.

class CategoryTest(TestCase):

    def setUp(self):
        data_input = {"name": "Category 1",
            "children": 
            [{ "name": "Category 1.1",
                "children": [{ "name": "Category 1.1.1",
                    "children": [{ "name": "Category 1.1.1.1"},
                                {"name": "Category 1.1.1.2"},
                                {"name": "Category 1.1.1.3"}]
                             },
                            {"name": "Category 1.1.2", 
                               "children": [{"name": "Category 1.1.2.1"},
                                   {"name": "Category 1.1.2.2"},
                                   {"name": "Category 1.1.2.3"}]
                            }]},
                            {"name": "Category 1.2",
                            "children": [{"name": "Category 1.2.1"},
                                         {"name": "Category 1.2.2",
                                         "children": [{"name": "Category 1.2.2.1"},
                                            {"name": "Category 1.2.2.2"
                            }]}]}]}

        response = self.client.get('/categories/', data_input)
        print(response)



    data_output1 = {"id": 2, "name": "Category 1.1",
                 "parents": [{"id": 1, "name": "Category 1"}],
                 "children": [{"id": 3, "name": "Category 1.1.1"},
                 {"id": 7, "name": "Category 1.1.2"}],
                  "siblings": [                         #// sisters and brothers
                {"id": 11, "name": "Category 1.2"}]}

    data_output2 = {"id": 8, "name": "Category 1.1.2.1",
                  "parents": [{"id": 7, "name": "Category 1.1.2"},
                              {"id": 2, "name": "Category 1.1"},
                              {"id": 1, "name": "Category 1"},
                              ],
                  "children": [],
                  "siblings": [{"id": 9, "name": "Category 1.1.2.2"},
                               {"id": 10, "name": "Category 1.1.2.3"}]}
