from django.test import TestCase
from django.urls import reverse
from .views import calculate_intervals

class IntervalTestCase(TestCase):
    def test_interval_calculation(self):
        includes = [[10, 100]]
        excludes = [[20, 30]]
        expected_result = [[10, 19], [31, 100]]
        result = calculate_intervals(includes, excludes)
        self.assertEqual(result, expected_result)

