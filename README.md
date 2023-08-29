#RegexStringBuilder

RegexStringBuilder is a utility class designed to simplify the creation of complex regular expressions using a chainable, method-based approach.

This class provides an intuitive way to construct regular expressions by chaining various methods together. Each method corresponds to a specific regular expression operation or flag, allowing you to progressively build intricate patterns. The final regular expression string can be obtained using the build method.
# Example

python

import re
from regex_string_builder import RegexStringBuilder

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

#Methods

    case_insensitive: Add the case-insensitive flag to the regular expression.
    multiline: Add the multiline flag to the regular expression.
    match_newlines: Add the dot-all flag to match newlines with '.'.
    as_unicode: Add the Unicode matching flag to the regular expression.
    as_ascii: Add the ASCII matching flag to the regular expression.
    debug_mode: Add the debug flag to the regular expression.
    one_or_more: Match one or more occurrences of the preceding element.
    zero_or_more: Match zero or more occurrences of the preceding element.
    zero_or_one: Match zero or one occurrence of the specified element.
    starting_with: Ensure the regular expression starts with the specified element.
    ending_with: Ensure the regular expression ends with the specified element.
    match_any_character: Match any character optionally followed by a specified character.
    match_exactly: Match the entire string or specified element exactly.
    either_word_or_substring: Match either the whole regex or the specified element as a group.
    match_either_or: Match either of the two specified elements.
    match_previous_or_this: Match either the preceding element or the specified element.
    set_of: Match any character from the specified set of characters.
    match_from_n_to_m_occurrences: Match a preceding element from n to m occurrences.
    match_literal: Match the specified element literally.
    escape: Escape the specified element for literal matching.
    match_all_words: Match all words in the string.
    match_all_words_and_digits: Match words containing digits in the string.
    match_all_digits: Match all sequences of digits in the string.
    match_words_up_to_n_chars: Match words containing at least n characters.
    match_all_chars: Match any non-whitespace character.
    optional_character: Match the preceding character optionally.
    not_set_of: Match any character not in the specified set.
    match_non_whitespace: Match any non-whitespace character.

#Attributes

    regex_string: The current regular expression being constructed.
    regex_flags: A list of flags to be applied to the regular expression.
    previous_methods: A list of previously applied method names.

Feel free to use the RegexStringBuilder class to simplify your regular expression building process and create more readable and maintainable patterns.