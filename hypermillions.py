import json
import random
import sys
import argparse

def pick_winner(tickets, winners=1):
    all_winners = []

    for i in range(winners):
        indices = range(len(tickets))
        winning_index = random.choice(indices)
        all_winners.append(tickets[winning_index])
        tickets.pop(winning_index)

    return all_winners

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pick winners from a raffle')
    parser.add_argument('filepath', help='Path to the JSON file containing tickets')
    parser.add_argument('seed', help='Random seed for reproducibility')
    parser.add_argument('--winners', type=int, default=1, help='Number of winners to pick (default: 1)')

    args = parser.parse_args()

    random.seed(args.seed)

    try:
        with open(args.filepath) as f:
            tickets = json.loads(f.read())

        all_winners = pick_winner(tickets, args.winners)

        for i, winner in enumerate(all_winners):
            print(f"{i+1}.", winner)

    except FileNotFoundError:
        print(f"Error: File '{args.filepath}' not found")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: File '{args.filepath}' is not valid JSON")
        sys.exit(1)
