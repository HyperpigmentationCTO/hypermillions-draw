# HyperMillions Draw System
This repository contains the code for running verifiable HyperMillions draws. The system is designed to be transparent and provably fair.

## How It Works
1. Before each draw, we publish:
   - A JSON file containing all valid entries (`lottery_{number}.json`)
   - The hash of this file (generated using `hash.py`)
   - A future Solana block number that will be used for randomness

2. You can verify the entries file hasn't been tampered with by:
   ```bash
   python hash.py <json_entries_file>
   ```
   The output should match the hash we published. This ensures the entries file is exactly the same one we announced.

3. Once the announced block is mined, we use its hash as the random seed for the draw:
   ```bash
   python hypermillions.py <json_entries_file> <block_hash>
   ```
   Replace BLOCK_HASH with the actual hash of the pre-announced block.

## Why This Is Fair
- The entries file is locked in by its hash before the draw
- The random seed comes from a future block hash that couldn't be known when entries closed
- Anyone can run the same code with the same inputs to verify the results
- Each address in the JSON file appears once per entry they have

## Requirements
- Python 3.6 or higher
- The files from this repository
- A copy of the entries JSON file

## Step by Step Verification
1. Download this repository and the announced entries.json file
2. Run `hash.py` to verify the file matches our announced hash
3. Get the hash of the pre-announced block
4. Run `hypermillions.py` with the block hash to see the winners
5. The winners should match our official announcement

This system ensures complete transparency and allows anyone to verify the fairness of each draw.
