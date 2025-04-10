# string_package/__init__.py



from .manipulate import reverse_string, capitalize_words, remove_punctuation
from .stats import count_characters, count_words, average_word_length

__all__ = [
    'reverse_string',
    'capitalize_words',
    'remove_punctuation',
    'count_characters',
    'count_words',
    'average_word_length'
]

print("string_package initialized") # Just to show when the package is imported

if __name__ == "__main__":
    print("--- Running string_package/__init__.py directly (for testing imports) ---")
    try:
        # These should be defined because of the imports above
        print(f"reverse_string available: {'reverse_string' in globals()}")
        print(f"count_words available: {'count_words' in globals()}")
    except NameError as e:
        print(f"Error accessing imported function: {e}")
    print("--- End of __init__.py direct run test ---")
