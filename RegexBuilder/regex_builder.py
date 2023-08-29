class RegexStringBuilder:
    """
    A utility class for building complex regular expressions using a chainable, method-based approach.

    This class provides an intuitive way to construct regular expressions by chaining various methods together.
    Each method corresponds to a specific regular expression operation or flag, allowing you to gradually build up
    complex patterns. The final regular expression string can be obtained using the `build` method.

    Example:
    ```
    # Example usage
    text = "https://www.youtube.com/watch?v=qzOzad7ngOs"
    builder = RegexStringBuilder()

    pattern = (
        builder
        .match_literal("http")
        .optional_character("s")
        .match_previous_or_this("ftp")
        .either_word_or_substring()
        .match_literal("://")
        .not_set_of("\s/$.?#")
        .match_any_character()
        .match_non_whitespace()
        .zero_or_more()
        .match_exactly()
        .build()
    )

    matches = re.findall(pattern, text)
    print(pattern)
    print(matches)
    ```

    Methods:
    - case_insensitive: Add the case-insensitive flag to the regular expression.
    - multiline: Add the multiline flag to the regular expression.
    - match_newlines: Add the dot-all flag to match newlines with '.'.
    - as_unicode: Add the Unicode matching flag to the regular expression.
    - as_ascii: Add the ASCII matching flag to the regular expression.
    - debug_mode: Add the debug flag to the regular expression.
    - one_or_more: Match one or more occurrences of the preceding element.
    - zero_or_more: Match zero or more occurrences of the preceding element.
    - zero_or_one: Match zero or one occurrence of the specified element.
    - starting_with: Ensure the regular expression starts with the specified element.
    - ending_with: Ensure the regular expression ends with the specified element.
    - match_any_character: Match any character optionally followed by a specified character.
    - match_exactly: Match the entire string or specified element exactly.
    - either_word_or_substring: Match either the whole regex or the specified element as a group.
    - match_either_or: Match either of the two specified elements.
    - match_previous_or_this: Match either the preceding element or the specified element.
    - set_of: Match any character from the specified set of characters.
    - match_from_n_to_m_occurrences: Match a preceding element from n to m occurrences.
    - match_literal: Match the specified element literally.
    - escape: Escape the specified element for literal matching.
    - match_all_words: Match all words in the string.
    - match_all_words_and_digits: Match words containing digits in the string.
    - match_all_digits: Match all sequences of digits in the string.
    - match_words_up_to_n_chars: Match words containing at least n characters.
    - match_all_chars: Match any non-whitespace character.
    - optional_character: Match the preceding character optionally.
    - not_set_of: Match any character not in the specified set.
    - match_non_whitespace: Match any non-whitespace character.

    Attributes:
    - regex_string: The current regular expression being constructed.
    - regex_flags: A list of flags to be applied to the regular expression.
    - previous_methods: A list of previously applied method names.

    """

    def __init__(self):
        """
        Initialize the RegexStringBuilder instance.
        """
        self.regex_string: str = ""
        self.regex_flags: list = []
        self.previous_methods: list = []

    def _add_flag(self, flag):
        """
        Internal method to add a flag to the list of regex_flags.

        Args:
            flag (str): The regex flag to be added.
        """
        self.regex_flags.append(flag)

    def _apply_changes(self):
        """
        Apply changes to the regular expression by adding flags if specified.
        """
        if self.regex_flags:
            flags = "|".join(self.regex_flags)
            self._add_to_regex_string(f"(?{flags})")

    def case_insensitive(self):
        """
        Add the case-insensitive flag to the regular expression.

        Returns:
            self: The current RegexStringBuilder instance.
        """
        return self._add_flag(re.IGNORECASE)

    def multiline(self):
        """
        Add the multiline flag to the regular expression.

        Returns:
            self: The current RegexStringBuilder instance.
        """
        return self._add_flag(re.MULTILINE)

    def match_newlines(self):
        """
        Add the dot-all flag to match newlines with '.'

        Returns:
            self: The current RegexStringBuilder instance.
        """
        return self._add_flag(re.DOTALL)

    def as_unicode(self):
        """
        Add the Unicode matching flag to the regular expression.

        Returns:
            self: The current RegexStringBuilder instance.
        """
        return self._add_flag(re.UNICODE)

    def as_ascii(self):
        """
        Add the ASCII matching flag to the regular expression.

        Returns:
            self: The current RegexStringBuilder instance.
        """
        return self._add_flag(re.ASCII)

    def debug_mode(self):
        """
        Add the debug flag to the regular expression.

        Returns:
            self: The current RegexStringBuilder instance.
        """
        return self._add_flag(re.DEBUG)

    def one_or_more(self, element=None):
        """
        Match one or more occurrences of the preceding element.

        Args:
            element (str, optional): The element to be repeated. If None, the preceding element is repeated.

        Returns:
            self: The current RegexStringBuilder instance.
        """
        self.regex_string += "+" if element is None else f"{element}+"
        return self

    def zero_or_more(self, element=None):
        """
        Match zero or more occurrences of the preceding element.

        Args:
            element (str, optional): The element to be repeated. If None, the preceding element is repeated.

        Returns:
            self: The current RegexStringBuilder instance.
        """
        self.regex_string += "*" if element is None else f"{element}*"
        return self

    def zero_or_one(self, element):
        """
        Match zero or one occurrence of the specified element.

        Args:
            element (str): The element to be matched optionally.

        Returns:
            self: The current RegexStringBuilder instance.
        """
        self._add_postfix(element, "?")
        return self

    def starting_with(self, element=None):
        """
        Ensure the regular expression starts with the specified element.

        Args:
            element (str, optional): The element that the regex should start with. If None, the regex itself is used.

        Returns:
            self: The current RegexStringBuilder instance.
        """
        if element is None:
            self._add_prefix(self.regex_string, "^")
        else:
            self._add_prefix(element, "^")
        return self

    def ending_with(self, element=None):
        """
        Ensure the regular expression ends with the specified element.

        Args:
            element (str, optional): The element that the regex should end with. If None, the regex itself is used.

        Returns:
            self: The current RegexStringBuilder instance.
        """
        self.regex_string += "$" if element is None else f"{element}$"
        return self

    def match_any_character(self, character: str = None, match_newlines: bool = False):
        """
        Match any character optionally followed by a specified character.

        Args:
            character (str, optional): The optional character to match.
            match_newlines (bool, optional): Whether to match newlines with '.'.

        Returns:
            self: The current RegexStringBuilder instance.
        """
        self.regex_string += "." if character is None else f".{character}"
        if match_newlines:
            self.regex_flags += "| Re.DOTALL"
        return self

    def match_exactly(self, element=None):
        """
        Match the entire string or specified element exactly.

        Args:
            element (str, optional): The element to match exactly. If None, the regex matches the whole string.

        Returns:
            self: The current RegexStringBuilder instance.
        """
        if element is None:
            temp = self.regex_string
            self.regex_string = ""
            self.regex_string += f"^{temp}$"
        else:
            self.regex_string += f"^{element}$"
        return self

    def either_word_or_substring(self, element=None):
        """
        Match either the whole regex or the specified element as a group.

        Args:
            element (str, optional): The element to match as a group. If None, the regex itself is matched.

        Returns:
            self: The current RegexStringBuilder instance.
        """
        if element is None:
            temp = self.regex_string
            self.regex_string = ""
            self.regex_string = f"({temp})"
        else:
            self.regex_string += f"({element})"
        return self

    def match_either_or(self, element1, element2):
        """
        Match either of the two specified elements.

        Args:
            element1 (str): The first element to match.
            element2 (str): The second element to match.

        Returns:
            self: The current RegexStringBuilder instance.
        """
        self.regex_string += f"{element1}|{element2}"
        return self

    def match_previous_or_this(self, element):
        """
        Match either the preceding element or the specified element.

        Args:
            element (str): The element to match if the preceding element is not found.

        Returns:
            self: The current RegexStringBuilder instance.
        """
        self.regex_string += f"|{element}"
        return self

    def set_of(self, element):
        """
        Match any character from the specified set of characters.

        Args:
            element (str): The set of characters to match.

        Returns:
            self: The current RegexStringBuilder instance.
        """
        self.regex_string += f"[{element}]"
        return self

    def match_from_n_to_m_occurrences(self, n, m=""):
        """
        Match a preceding element from n to m occurrences.

        Args:
            n (int): Minimum number of occurrences.
            m (int or str, optional): Maximum number of occurrences. If empty, only minimum is specified.

        Returns:
            self: The current RegexStringBuilder instance.
        """
        self.regex_string += f"{{{n}, {m}}}"
        return self

    def match_literal(self, element):
        """
        Match the specified element literally.

        Args:
            element (str): The element to match literally.

        Returns:
            self: The current RegexStringBuilder instance.
        """
        self.regex_string += element
        return self

    def escape(self, element):
        """
        Escape the specified element for literal matching.

        Args:
            element (str): The element to escape.

        Returns:
            self: The current RegexStringBuilder instance.
        """
        self.regex_string += f'\\{element}'
        return self

    def match_all_words(self):
        """
        Match all words in the string.

        Returns:
            self: The current RegexStringBuilder instance.
        """
        self.regex_string += f'\\b\\w+\\b'
        return self

    def match_all_words_and_digits(self):
        """
        Match words containing digits in the string.

        Returns:
            self: The current RegexStringBuilder instance.
        """
        self.regex_string += f"\\b\\w*\\d*\\w+\\b"
        return self

    def match_all_digits(self):
        """
        Match all sequences of digits in the string.

        Returns:
            self: The current RegexStringBuilder instance.
        """
        self.regex_string += f"\\d+"
        return self

    def match_words_up_to_n_chars(self, n):
        """
        Match words containing at least n characters.

        Args:
            n (int): Minimum number of characters in the word.

        Returns:
            self: The current RegexStringBuilder instance.
        """
        self.regex_string += f'\\b\\w{{{n},}}\\b'
        return self

    def match_all_chars(self):
        """
        Match any non-whitespace character.

        Returns:
            self: The current RegexStringBuilder instance.
        """
        self.regex_string += f"\\S"
        return self

    def optional_character(self, char):
        """
        Match the preceding character optionally.

        Args:
            char (str): The character to match optionally.

        Returns:
            self: The current RegexStringBuilder instance.
        """
        self.regex_string += f"{char}?"
        return self

    def not_set_of(self, element):
        """
        Match any character not in the specified set.

        Args:
            element (str): The set of characters to exclude.

        Returns:
            self: The current RegexStringBuilder instance.
        """
        if element == "\s":
            print("This pattern is equivalent to \S, please consider using it (call the  match_non_whitespace method)"
                  " if you want less verbosity.")
        self.regex_string += f"[^{element}]"
        return self

    def match_non_whitespace(self):
        """
        Match any non-whitespace character.

        Returns:
            self: The current RegexStringBuilder instance.
        """
        self.regex_string += f"\\S"
        return self

    def build(self):
        """
        Apply changes and build the final regular expression.

        Returns:
            str: The constructed regular expression string.
        """
        self._apply_changes()
        return self.regex_string
