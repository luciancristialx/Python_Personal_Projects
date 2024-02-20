import pandas as pd

CHARACTER_EXCLUSION = [',','-',' ','\'']
CONFIDENCE_SCORE = 100

def get_user_input(name_type):
    name = input(f"Please enter {name_type} name:").upper()
    print(f"Original {name_type} name: {name}\n")
    return name


def replace_excluded_chars(string_value):
    for char in string_value:
        if char in CHARACTER_EXCLUSION:
            string_value = string_value.replace(char, " ")
    return string_value

#Get unique letters in string value
def get_unique_letters(string_value):
    unique_letters = []
    for char in string_value:
        if char not in unique_letters:
            unique_letters.append(char)
    return unique_letters


#Count characters in string value
def count_characters(string_value):
    char_count = 0
    for char in internal_string:
        if char.isalpha():
            char_count+=1
    return char_count

internal_string = get_user_input("internal")
external_string = get_user_input("external")

internal_string = replace_excluded_chars(internal_string)
external_string = replace_excluded_chars(external_string)

print(f"internal name after special chars removal: {internal_string}")
print(f"external name after special chars removal: {external_string}")
print("\n")

internal_unique_letters = get_unique_letters(internal_string)
external_unique_letters = get_unique_letters(external_string)


data_internal = []
for letter in internal_unique_letters:
    if letter != " ":
        list_indexes = [str(pos) for pos, char in enumerate(internal_string) if char == letter]
        my_list = [letter,",".join(list_indexes),len(list_indexes)]
        data_internal.append(my_list)

df_internal = pd.DataFrame(data_internal, columns = ['letter', 'index', 'occurrences'])
df_internal.to_csv('df_internal.csv', index = False)

data_external = []
for letter in external_unique_letters:
    if letter != " ":
        list_indexes = [str(pos) for pos, char in enumerate(external_string) if char == letter]
        my_list = [letter,",".join(list_indexes),len(list_indexes)]
        data_external.append(my_list)

df_external = pd.DataFrame(data_external, columns = ['letter', 'index', 'occurrences'])
df_external.to_csv('df_external.csv', index = False)

count_char_internal = count_characters(internal_string)
print(f"Internal string char count: {count_char_internal}")

char_score = round(CONFIDENCE_SCORE / count_char_internal,2)

print(f"Internal string char score: {char_score}")

confidence_score = 0
for ind in df_internal.index:
    char = df_internal['letter'][ind]
    result_df_internal = df_internal[df_internal['letter'] == char]
    result_df_external = df_external[df_external['letter'] == char]
    if result_df_external.empty:
        confidence_score += 0
    else:
        external_occurrences = result_df_external.occurrences.values[0]
        internal_occurrences = result_df_internal.occurrences.values[0]
        occurrence = 0
        if int(external_occurrences) > int(internal_occurrences):
            occurrence = result_df_internal.occurrences.values[0]
        else:
            occurrence = result_df_external.occurrences.values[0]
        letter_score = occurrence * char_score
        confidence_score += letter_score

print(confidence_score)



