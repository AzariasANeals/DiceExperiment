import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import unittest
from main import (
    roll_dice_once,
    simulate_rolls,
    calculate_simulated_distribution
)

class TestDiceProbability(unittest.TestCase):

    # NORMAL TEST CASES

    def test_roll_dice_once_normal(self):
        """
        Normal case: rolling 2 dice with 6 sides each.

        This test verifies:
        - The function returns the correct number of dice values
        - Each die value is within the valid range (1 to N)
        - The sum equals the total of the individual dice values
        """
        dice_values, total = roll_dice_once(2, 6)

        # Verify correct number of dice
        self.assertEqual(len(dice_values), 2)

        # Verify each die is within valid range
        for value in dice_values:
            self.assertTrue(1 <= value <= 6)

        # Verify sum is correct
        self.assertEqual(total, sum(dice_values))

    def test_simulate_multiple_rolls_normal(self):
        """
        Normal case: simulate multiple dice rolls.

        This test verifies:
        - The correct number of roll results is returned
        - Each roll sum is within the valid possible range
        """
        num_dice = 2
        num_sides = 6
        num_rolls = 10

        results = simulate_rolls(num_dice, num_sides, num_rolls)

        # Verify correct number of roll results
        self.assertEqual(len(results), num_rolls)

        # Valid sum range: 2 to 12
        for roll_sum in results:
            self.assertTrue(2 <= roll_sum <= 12)

    def test_probability_distribution_normal(self):
        """
        Normal case: calculate probability distribution from valid roll results.

        This test verifies:
        - Each probability is between 0 and 1
        - The probabilities sum to 1
        """
        results = [2, 3, 3, 4, 4, 4]
        distribution = calculate_simulated_distribution(results)

        total_probability = 0

        for count, probability in distribution.values():
            self.assertTrue(0 <= probability <= 1)
            total_probability += probability

        self.assertAlmostEqual(total_probability, 1.0)

    # EDGE TEST CASES

    def test_single_roll_single_die(self):
        """
        Edge case: rolling 1 die with 1 side.

        This test verifies:
        - The only possible roll value is 1
        - The sum returned is 1
        """
        dice_values, total = roll_dice_once(1, 1)

        self.assertEqual(dice_values, [1])
        self.assertEqual(total, 1)

    def test_simulate_one_roll(self):
        """
        Edge case: simulating exactly one roll.

        This test verifies:
        - Exactly one result is returned
        - The result is within the valid sum range
        """
        results = simulate_rolls(3, 6, 1)

        self.assertEqual(len(results), 1)
        self.assertTrue(3 <= results[0] <= 18)

    def test_probability_distribution_single_value(self):
        """
        Edge case: probability distribution with only one unique result.

        This test verifies:
        - The distribution contains one entry
        - The probability of that entry is 1.0
        """
        results = [7, 7, 7, 7]
        distribution = calculate_simulated_distribution(results)

        self.assertEqual(len(distribution), 1)

        count, probability = distribution[7]
        self.assertEqual(count, 4)
        self.assertEqual(probability, 1.0)


if __name__ == "__main__":
    unittest.main()
