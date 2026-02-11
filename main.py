import random
from itertools import product


def roll_dice_once(num_dice, num_sides):
    """
    Simulates rolling M number of N-sided dice once.
    Returns individual dice values and their sum.
    """
    dice_values = [random.randint(1, num_sides) for _ in range(num_dice)]
    return dice_values, sum(dice_values)


def simulate_rolls(num_dice, num_sides, num_rolls):
    """
    Simulates rolling M N-sided dice K times.
    Prints each roll and returns list of sums.
    """
    results = []

    for i in range(1, num_rolls + 1):
        dice_values, roll_sum = roll_dice_once(num_dice, num_sides)
        results.append(roll_sum)

        addition_string = " + ".join(map(str, dice_values))
        print(f"Roll {i}: {addition_string} = {roll_sum}")

    return results


def calculate_simulated_distribution(results):
    """
    Calculates simulated frequency and probability distribution.
    """
    distribution = {}
    total = len(results)

    for value in results:
        distribution[value] = distribution.get(value, 0) + 1

    for key in distribution:
        count = distribution[key]
        distribution[key] = (count, count / total)

    return dict(sorted(distribution.items()))


def calculate_theoretical_distribution(num_dice, num_sides):
    """
    Calculates the theoretical combinations and probabilities
    using all possible dice outcomes.
    """
    distribution = {}
    all_combinations = list(product(range(1, num_sides + 1), repeat=num_dice))
    total_combinations = len(all_combinations)

    for combo in all_combinations:
        roll_sum = sum(combo)
        distribution[roll_sum] = distribution.get(roll_sum, 0) + 1

    for key in distribution:
        count = distribution[key]
        distribution[key] = (count, count / total_combinations)

    return dict(sorted(distribution.items())), total_combinations


def print_distribution_table(title, distribution, total_combinations=None):
    """
    Prints a formatted distribution table.
    """
    print(f"\n{title}")
    print("-" * 50)

    if total_combinations is not None:
        print(f"Total Possible Combinations: {total_combinations}\n")

    print(f"{'Sum':<10}{'Ways':<10}{'Probability'}")
    print("-" * 50)

    for roll_sum, (count, probability) in distribution.items():
        print(f"{roll_sum:<10}{count:<10}{probability:.4f}")


def main():
    print("🎲 Dice Roll Probability Simulator 🎲")

    try:
        N = int(input("Enter number of sides per die (N): "))
        M = int(input("Enter number of dice (M): "))
        K = int(input("Enter number of simulation rolls (K): "))

        if N <= 0 or M <= 0 or K <= 0:
            raise ValueError

    except ValueError:
        print("Error: Please enter valid positive integers.")
        return

    # THEORETICAL DISTRIBUTION
    theoretical_dist, total_combos = calculate_theoretical_distribution(M, N)
    print_distribution_table(
        "Theoretical Distribution (All Possible Combinations)",
        theoretical_dist,
        total_combos
    )

    # SIMULATION
    print("\n--- Simulation Rolls ---\n")
    results = simulate_rolls(M, N, K)

    simulated_dist = calculate_simulated_distribution(results)
    print_distribution_table(
        "Simulated Distribution",
        simulated_dist
    )


if __name__ == "__main__":
    main()
