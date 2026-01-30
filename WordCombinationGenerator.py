import itertools
import os
import sys

def generate_combinations(word1, word2):
    """
    Generates all unique word combinations (permutations) using the combined
    multiset of letters from word1 and word2, up to the length of the
    longest input word.
    
    :param word1: The first input word (string).
    :param word2: The second input word (string).
    :return: A list of unique, sorted combination strings.
    """
    
    # 1. Determine the multiset of all letters combined (e.g., 'as' + 'an' -> ['a', 's', 'a', 'n'])
    # We convert to lowercase to handle case-insensitivity in combinations.
    all_letters = list(word1.lower()) + list(word2.lower())
    
    # Determine the maximum length for the combinations to be generated
    max_length = max(len(word1), len(word2))
    
    # Use a set to store unique generated combination strings
    unique_combinations = set()
    
    # 2. Iterate through lengths from 1 up to the max_length
    for k in range(1, max_length + 1):
        # itertools.permutations generates unique permutations from the multiset.
        # We use a set on the resulting strings to ensure uniqueness across
        # different initial permutations and across different lengths.
        for combination_tuple in itertools.permutations(all_letters, k):
            word = "".join(combination_tuple)
            unique_combinations.add(word)
            
    # 3. Sort the results alphabetically for consistent, easy-to-read output
    sorted_combinations = sorted(list(unique_combinations))
    
    return sorted_combinations, max_length

def run_script():
    """
    Main function to handle user input, generation, and file output.
    """
    print("--- Word Combination Generator ---")
    
    # Get user input
    word1 = input("Enter Word 1: ").strip()
    word2 = input("Enter Word 2: ").strip()

    if not word1 or not word2:
        print("Error: Both words must be provided to generate combinations.")
        # Exit the script gracefully if input is missing
        sys.exit(1)

    # Define output file path
    filename = "word_combinations.txt"

    # Generate combinations
    combinations, max_len = generate_combinations(word1, word2)
    
    # Write to file
    try:
        with open(filename, 'w') as f:
            total_count = len(combinations)
            
            # Write header information
            f.write("--- Possible Unique Word Combinations ---\n")
            f.write(f"Source Words: '{word1}' and '{word2}'\n")
            f.write(f"Letters Used (Multiset): {sorted(list(word1.lower() + word2.lower()))}\n")
            f.write(f"Combinations Generated up to Length: {max_len}\n")
            f.write("-" * 50 + "\n")
            
            # Write combinations with serial numbers
            for i, word in enumerate(combinations, 1):
                f.write(f"{i}) {word}\n")
                
            # Write total count at the end
            f.write("-" * 50 + "\n")
            f.write(f"Total Unique Combinations Found: {total_count}\n")
            
        print(f"\nSuccessfully generated {total_count} unique combinations.")
        print(f"Results saved to '{os.path.abspath(filename)}'")

    except IOError as e:
        print(f"Error: Could not write to file '{filename}'. Details: {e}")

if __name__ == "__main__":
    run_script()