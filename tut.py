def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return f"{first} {last}"

full_name = create_name("john", "doe")
print(full_name) 