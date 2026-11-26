from text_preprocessor import normalize_text, tokenize_text, count_tokens

text = "I know Java and Python"

print("Normalized:", normalize_text(text))
print("Tokens:", tokenize_text(text))
print("Token count:", count_tokens(text))