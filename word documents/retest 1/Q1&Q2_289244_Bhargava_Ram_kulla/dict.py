def merge_dictionaries(dict1, dict2):
   
    merged_dict = dict1.copy()  
    for key, value in dict2.items():
        if key in merged_dict:
            if isinstance(merged_dict[key], list) and isinstance(value, list):
                merged_dict[key] += value
            elif isinstance(merged_dict[key], (int, float)) and isinstance(value, (int, float)):
                merged_dict[key] += value
            else:
                merged_dict[key] = value
        else:
            merged_dict[key] = value
    return merged_dict

# I am taking one example to run this code
dict1 = {'a': [1, 2], 'b': 10, 'c': 'hello'}
dict2 = {'a': [3, 4], 'b': 5, 'c': 'world'}
result = merge_dictionaries(dict1, dict2)
print(result)
