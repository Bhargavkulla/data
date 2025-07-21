def get_value_from_path(nested_dict,key_path):
    keys=key_path.split('/')
    current_value=nested_dict

    for key in keys:
        current_value=current_value[key]
    return current_value
nested_dict={'a':{'b':{'c':'d'}}}
key_path='a/b/c'
result=get_value_from_path(nested_dict,key_path)
print(result)