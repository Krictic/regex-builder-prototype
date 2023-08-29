from RegexBuilder.regex_builder import RegexStringBuilder
import re

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