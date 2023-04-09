
object_input = input("Please enter the nested object in the form of a dictionary: ")
key_input = input("Please enter the key in the form of 'x/y/z': ")

object_dict = eval(object_input)  
value = get_value_from_nested_object(object_dict, key_input)