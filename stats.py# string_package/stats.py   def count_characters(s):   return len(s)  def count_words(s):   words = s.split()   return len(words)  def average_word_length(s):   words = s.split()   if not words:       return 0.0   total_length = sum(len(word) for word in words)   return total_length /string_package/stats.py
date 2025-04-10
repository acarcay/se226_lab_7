# string_package/stats.py


def count_characters(s):
  return len(s)

def count_words(s):
  words = s.split()
  return len(words)

def average_word_length(s):
  words = s.split()
  if not words:
      return 0.0
  total_length = sum(len(word) for word in words)
  return total_length / len(words)

# Test cases when running the module directly
if __name__ == "__main__":
    print("--- Testing stats.py ---")
    test_string = "This is another sample sentence."
    test_string_cleaned = "This is another sample sentence" # Assuming punctuation removed for word stats
    empty_string = ""
    spaces_string = "   "

    print(f"Original: '{test_string}'")
    print(f"Character Count: {count_characters(test_string)}")
    print(f"Word Count (on cleaned): {count_words(test_string_cleaned)}")
    print(f"Average Word Length (on cleaned): {average_word_length(test_string_cleaned):.2f}")

    print(f"\nTesting edge cases:")
    print(f"Stats for empty string ('{empty_string}'):")
    print(f"  Chars: {count_characters(empty_string)}")
    print(f"  Words: {count_words(empty_string)}")
    print(f"  Avg Len: {average_word_length(empty_string):.2f}")

    print(f"Stats for spaces string ('{spaces_string}'):")
    print(f"  Chars: {count_characters(spaces_string)}")
    print(f"  Words: {count_words(spaces_string)}")
    print(f"  Avg Len: {average_word_length(spaces_string):.2f}")
    print("--- End of stats.py tests ---")
