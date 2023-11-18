from django.test import TestCase
from .views import calculate_intervals

class IntervalTestCase(TestCase):
    def test_example_1(self):
        # Includes: 10-100, Excludes: 20-30
        self.assertEqual(
            calculate_intervals([[10, 100]], [[20, 30]]),
            [[10, 19], [31, 100]]
        )

    def test_example_2(self):
        # Includes: 50-5000, 10-100, Excludes: (none)
        self.assertEqual(
            calculate_intervals([[50, 5000], [10, 100]], []),
            [[10, 5000]]
        )

    def test_example_3(self):
        # Includes: 200-300, 50-150, Excludes: 95-205
        self.assertEqual(
            calculate_intervals([[200, 300], [50, 150]], [[95, 205]]),
            [[50, 94], [206, 300]]
        )

    def test_example_4(self):
        # Includes: 200-300, 10-100, 400-500, Excludes: 410-420, 95-205, 100-150
        self.assertEqual(
            calculate_intervals([[200, 300], [10, 100], [400, 500]], [[410, 420], [95, 205], [100, 150]]),
            [[10, 94], [206, 300], [400, 409], [421, 500]]
        )

    def test_empty_includes(self):
        # Test with empty includes
        self.assertEqual(
            calculate_intervals([], [[10, 20]]),
            []
        )

    def test_single_number_interval(self):
        # Test with single number interval
        self.assertEqual(
            calculate_intervals([[5, 5]], []),
            [[5, 5]]
        )

    def test_high_number_of_sets(self):
        # Test with a high number of interval sets
        includes = [[i, i+10] for i in range(0, 1000, 11)]  # Slightly offset includes
        excludes = [[i, i+5] for i in range(0, 1000, 22)]  # Offset excludes to partially overlap
        # Expected results should capture the non-overlapping parts of the includes
        expected_result = []
        for i in range(0, 1000, 11):
            if i % 22 == 0:
                expected_result.append([i+6, i+10])
            else:
                expected_result.append([i, i+10])

        self.assertEqual(calculate_intervals(includes, excludes), expected_result)
        
    def test_large_range(self):
        # Test with a very large range
        includes = [[0, 1000000]]
        excludes = [[500000, 600000]]
        expected_result = [[0, 499999], [600001, 1000000]]
        self.assertEqual(calculate_intervals(includes, excludes), expected_result)

    def test_combination_high_number_large_range(self):
        # Includes
        includes = [
            [5000, 15000],
            [6000, 16000],
            [11000, 17000],
            [18000, 35555],
            [41300, 66000],
        ]

        # Excludes
        excludes = [
            [0, 5000],
            [10000, 15000],
            [35000, 40000],
            [45000, 50000],
        ]

        # Expected Result
        expected_result = [
            [5001, 9999],
            [15001, 17000],
            [18000, 34999],
            [41300, 44999],
            [50001, 66000],
            
        ]

        self.assertEqual(calculate_intervals(includes, excludes), expected_result)
