# complex() returns a complex number with the value real + imag * 1j or
# converts a string or number to a complex number.

# If the first parameter is a string, it will be interpreted as a complex
# number and the function must be called without a second parameter.
# The second parameter can never be a string.
# Each argument may be any numeric type (including complex). If imag is omitted,
# it defaults to zero and the constructor serves as a numeric conversion like
# int and float. If both arguments are omitted, returns 0j.

print(f"complex(2): {complex(2)}")
print(f"complex(2, 3): {complex(2, 3)}")
print(f"complex('2+3j'): {complex('2+3j')}")
