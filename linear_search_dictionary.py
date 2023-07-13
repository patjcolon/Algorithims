"""testing search functions in dicts value -> key"""

def linear_search_ditctionary(dictionary, target_value):
    """Searches through a dictionary for value and returns key of value if present"""
    #dict_values is a class that needs to be converted to a list to subscript [i]
    values = list(dictionary.values())
    keys = list(dictionary.keys())

    # can use i in range.len.values or i in values but iterate j=0 j+=1 for tracking index
    for i in range(len(values)):
        if values[i] == target_value:
            print(f"Found at key {keys[i]}.")
            return keys[i]
    print("Target value is not present in dictionary.")
    return None
    

favorites = {
            "favorite food": "burrito",
            "favorite drink": "coke",
            "favorite game": "rust",
            "favorite place": "Hawaii",
            "favorite hobby": "driving",
            "favorite color": "purple",
            "favorite animal": "red-crested cardinal"
}

linear_search_ditctionary(favorites, "driving")
linear_search_ditctionary(favorites, "burrito")
linear_search_ditctionary(favorites, "purple")

linear_search_ditctionary(favorites, "cats")