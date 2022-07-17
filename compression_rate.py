import math

def compute_kl_distance(assumed_model, actual_model, bits= False):
    sum_of_distance = 0
    for char, assumed_percentage in assumed_model.items():
        assumed_prob = assumed_percentage / 100
        actual_prob = actual_model[char] / 100
        if (not(bits)):
            distance = actual_prob * math.log(actual_prob / assumed_prob)
        else:
            distance = actual_prob * math.log2(actual_prob / assumed_prob)
        sum_of_distance = sum_of_distance + distance  
    return sum_of_distance

def compute_space_saving_ratio(ori_text, comp_text):
    ori_size = len(ori_text) * 8
    comp_size = len(comp_text)
    comp_ratio = 1 - comp_size / ori_size
    return comp_ratio, ori_size, comp_size
    