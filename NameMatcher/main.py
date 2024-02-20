from name import Name

input_name = input("Internal name value:\n").upper()
i_name_to_match = input("External name value:\n").upper()

name = Name(input_name,i_name_to_match)
print("Object created!\n")

# print(f"Original argument value for parameter input_name: {name.internal_name}")
# name.internal_name = Name.cleanup(input_name)
# print(f"Altered argument value for parameter input_name: {name.internal_name}")
# print("")

# name.get_name_combinations()
# print(f"Name combinations: {name.name_combinations}")

# confidence_score = name.match_score_v2()
# print(confidence_score)

confidence_score = name.match_score_v3()
print(confidence_score)

