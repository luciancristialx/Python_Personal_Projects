import itertools
import math
CHARACTER_EXCLUSION = [',','-',' ','\'']
CONFIDENCE_SCORE = 100
class Name:

    @staticmethod
    def cleanup(string_value):
        formatted_string = string_value
        for character in formatted_string:
            if character=="-":
                formatted_string = formatted_string.replace(character, ' ')
            elif (character in CHARACTER_EXCLUSION) and character != " ":
                formatted_string = formatted_string.replace(character, '')
        return formatted_string


    def __init__(self,internal_name,external_name):

        self.internal_name = Name.cleanup(internal_name)
        self.external_name = external_name
        self.name_combinations = []


    def get_name_list(self):
        name_list = self.internal_name.split()
        return name_list


    def get_name_to_match_length(self):
        name_as_list = self.get_name_list()
        return len(name_as_list)


    def get_name_combinations(self):
        name_as_list = self.get_name_list()
        name_as_list_length = self.get_name_to_match_length()
        combinations = itertools.permutations(name_as_list,name_as_list_length)
        for comb in combinations:
            blank_name = ""
            for i in range(len(comb)):
                blank_name += comb[i] + " "
            self.name_combinations.append(blank_name.strip())


    def get_alpha_count(self):
        alpha_char_count = 0
        for character in self.internal_name:
            if character.isalpha():
                alpha_char_count+=1
            else:
                continue
        return alpha_char_count

    def get_char_score(self):
        char_score = float(CONFIDENCE_SCORE / self.get_alpha_count())
        return round(char_score, 2)

    def match_score(self):
        confidence_scores = []
        confidence = 0
        char_score = self.get_char_score()
        combinations = self.name_combinations
        if self.external_name in self.name_combinations:
            confidence += CONFIDENCE_SCORE
            dict_details = {
                "Internal name":self.internal_name,
                "External name":self.external_name,
                "Confidence score":confidence
            }
            confidence_scores.append(dict_details)
        else:
            name_to_match = self.external_name
            length = len(name_to_match)
            for name_combo in combinations:
                if len(name_to_match) > len(name_combo):
                    length = len(name_combo)
                for index in range(0,length):
                    char = name_to_match[index]
                    if char == " ":
                        confidence+=0
                    elif char == name_combo[index]:
                        confidence+=char_score
                    else:
                        confidence+=0
                if confidence > CONFIDENCE_SCORE:
                    confidence = math.floor(confidence)
                dict_details = {
                    "Internal name": name_combo,
                    "External name": self.external_name,
                    "Confidence score": confidence
                }
                confidence_scores.append(dict_details)
                confidence=0
        return confidence_scores

    def match_score_v2(self):
        confidence_score = 0
        li_internal_name = self.internal_name.split()
        li_external_name = self.external_name.split()
        char_seq_score = round(CONFIDENCE_SCORE/len(li_internal_name),2)

        for index in range(0,len(li_external_name)):
            ext_name_element = li_external_name[index]
            if ext_name_element in li_internal_name:
                confidence_score+=char_seq_score
            else:
                internal_seq_length = len(li_internal_name[index])
                external_seq_length = len(ext_name_element)
                char_score = round(char_seq_score / internal_seq_length,2)
                if ext_name_element in li_internal_name[index]:
                    confidence_score+=(char_score*external_seq_length)
                # if internal_seq_length == external_seq_length:
                #     i = 0
                #     for j in range(0, external_seq_length):
                #         char = ext_name_element[j]
                #         if char == li_internal_name[index][i]:
                #             confidence_score+=char_score
                #         i+=1
        dict_details = {
            "Internal name": self.internal_name,
            "External name": self.external_name,
            "Confidence score": round(confidence_score,2)
        }
        return dict_details








