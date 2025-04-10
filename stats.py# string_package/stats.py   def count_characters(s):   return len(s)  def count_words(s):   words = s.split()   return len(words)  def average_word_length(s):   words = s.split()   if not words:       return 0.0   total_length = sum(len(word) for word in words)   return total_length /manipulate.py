# string_package/manipulate.py
import string # Needed for remove_punctuation


def reverse_string(s):
  return s[::-1]

def capitalize_words(s):
  return s.title()

def remove_punctuation(s):
  translator = str.maketrans('', '', string.punctuation)
  return s.translate(translator)

# Test cases when running the module directly
if __name__ == "__main__":
    print("--- Testing manipulate.py ---")
    test_string = "hello, world! this is a test."
    print(f"Original: '{test_string}'")
    print(f"Reversed: '{reverse_string(test_string)}'")
    print(f"Capitalized: '{capitalize_words(test_string)}'")
    print(f"Punctuation Removed: '{remove_punctuation(test_string)}'")
    print("--- End of manipulate.py tests ---")
