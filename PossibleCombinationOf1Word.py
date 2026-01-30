import itertools
import os
import sys

def generate_variable_combinations(word1, word2):
    """
    (Mode 1 - Original Functionality)
    Generates all unique word combinations (permutations) using the combined
    multiset of letters from word1 and word2, up to the length of the
    longest input word.
    
    :param word1: The first input word (string).
    :param word2: The second input word (string).
    :return: A tuple containing:
             - A list of unique, sorted combination strings.
             - The max length used for generation.
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
        for combination_tuple in itertools.permutations(all_letters, k):
            word = "".join(combination_tuple)
            unique_combinations.add(word)
            
    # 3. Sort the results alphabetically for consistent, easy-to-read output
    sorted_combinations = sorted(list(unique_combinations))
    
    return sorted_combinations, max_length

def generate_fixed_length_permutations(word):
    """
    (Mode 2 - New Functionality)
    Generates all unique permutations of the input word where the length
    of the generated word is exactly equal to the length of the input word.

    :param word: The single input word (string).
    :return: A list of unique, sorted permutation strings.
    """
    if not word:
        return []

    # Convert to lowercase letters to handle case, but we will print in uppercase 
    # as per the example (DUG, DGU, etc.) for a nice output.
    letters = list(word.upper())
    length = len(letters)
    unique_permutations = set()

    # Use itertools.permutations with length 'length'
    # Since we are permuting all characters, we don't need the second argument (length)
    # but using the letters multiset ensures unique permutations even if letters are duplicated (e.g., 'AAB')
    for perm_tuple in itertools.permutations(letters):
        unique_permutations.add("".join(perm_tuple))

    return sorted(list(unique_permutations))

def run_script():
    """
    Main function to handle user input, select mode, generation, and file output.
    """
    print("--- Word Combination Generator ---")
    print("Select Mode:")
    print("1: Combination Mode (2 words, variable length up to max length)")
    print("2: Permutation Mode (1 word, fixed length)")
    print("-" * 50)
    
    mode = input("Enter mode (1 or 2): ").strip()
    
    filename = "word_combinations.txt"
    combinations = []
    total_count = 0
    header_info = ""

    if mode == '1':
        print("\n--- Combination Mode Selected ---")
        word1 = input("Enter Word 1: ").strip()
        word2 = input("Enter Word 2: ").strip()

        if not word1 or not word2:
            print("Error: Both words must be provided in Combination Mode.")
            sys.exit(1)

        combinations, max_len = generate_variable_combinations(word1, word2)
        total_count = len(combinations)
        
        header_info = (
            f"Source Words: '{word1}' and '{word2}'\n"
            f"Letters Used (Multiset): {sorted(list(word1.lower() + word2.lower()))}\n"
            f"Combinations Generated up to Length: {max_len}\n"
        )
        
    elif mode == '2':
        print("\n--- Permutation Mode Selected ---")
        word = input("Enter Single Word: ").strip()

        if not word:
            print("Error: A word must be provided in Permutation Mode.")
            sys.exit(1)

        combinations = generate_fixed_length_permutations(word)
        total_count = len(combinations)
        
        header_info = (
            f"Source Word: '{word}'\n"
            f"Letters Used (Multiset): {sorted(list(word.upper()))}\n"
            f"All Permutations Generated at Fixed Length: {len(word)}\n"
        )
        
    else:
        print("Invalid mode selected. Exiting.")
        sys.exit(1)

    # Write to file (common logic for both modes)
    try:
        with open(filename, 'w') as f:
            f.write("--- Possible Unique Word Combinations/Permutations ---\n")
            f.write(header_info)
            f.write("-" * 50 + "\n")
            
            # Write combinations with serial numbers
            for i, word in enumerate(combinations, 1):
                f.write(f"{i}) {word}\n")
                
            # Write total count at the end
            f.write("-" * 50 + "\n")
            f.write(f"Total Unique Results Found: {total_count}\n")
            
        print(f"\nSuccessfully generated {total_count} unique results.")
        print(f"Results saved to '{os.path.abspath(filename)}'")

    except IOError as e:
        print(f"Error: Could not write to file '{filename}'. Details: {e}")

if __name__ == "__main__":
    run_script()