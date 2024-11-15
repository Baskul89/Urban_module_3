calls_count = 0

def count_calls():
    return calls_count


def string_info(s):
    global calls_count
    calls_count += 1

    return len(s), str(s).upper(), str(s).lower()

def is_contains(s, list_):
    global calls_count
    calls_count += 1

    for s_ in list_:
        if str(s).lower() == str(s_).lower():
            return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(count_calls())