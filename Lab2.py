#  Create a LIST with your domain attributes, insert the elements using the append (), insert(), extend() and 
#add any iterables (tuples, sets, dictionaries etc.) to the list (Use all the methods ).

domain_attributes = []

domain_attributes.append("website")
domain_attributes.append("email")
domain_attributes.append("server")

domain_attributes.insert(2, "subdomain")
domain_attributes.insert(4, "dns")

iterable_elements = [1, 2, 3]
domain_attributes.extend(iterable_elements)

domain_attributes.append(("domain_name", "example.com"))

domain_attributes.extend({4, 5, 6})

domain_attributes.append({"port": 80, "protocol": "http"})

print("List with domain attributes:", domain_attributes)


#   Create a list with numeric and perform the following operations.
 #      Write a program to swap the first and last elements in a list.
  #     Write a program to find the sum of the digits in a list.
   #    Write a program to find the smallest element in a list.

def swap_first_and_last(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

def sum_of_digits(lst):
    total_sum = 0
    for num in lst:
        total_sum += sum(int(digit) for digit in str(num))
    return total_sum

def find_smallest_element(lst):
    if not lst:
        return None
    return min(lst)

numeric_list = [23, 45, 12, 67, 89, 34]

swapped_list = swap_first_and_last(numeric_list.copy())

sum_of_digits_result = sum_of_digits(numeric_list)

smallest_element = find_smallest_element(numeric_list)

print("Original List:", numeric_list)
print("List after swapping first and last elements:", swapped_list)
print("Sum of digits in the list:", sum_of_digits_result)
print("Smallest element in the list:", smallest_element)


# Sort the dictionaries in ascending order based on the Key of the dictionary.
def sort_dict_by_key(input_dict):
    sorted_dict = dict(sorted(input_dict.items()))
    return sorted_dict

sample_dict = {'c': 3, 'a': 1, 'b': 2, 'd': 4}

sorted_dict = sort_dict_by_key(sample_dict)

print("Original Dictionary:", sample_dict)
print("Sorted Dictionary by Keys (Ascending Order):", sorted_dict)


#   Create the dictionary with Numeric as Value in Key – Value pair and find the sum of all the values in the Dictionary.
def create_numeric_dictionary():
    num_dict = {}
    n = int(input("Enter the number of key-value pairs in the dictionary: "))

    for i in range(n):
        key = input(f"Enter key {i + 1}: ")
        value = float(input(f"Enter value for key {i + 1}: "))
        num_dict[key] = value

    return num_dict

def sum_of_values(dictionary):
    return sum(dictionary.values())

numeric_dict = create_numeric_dictionary()

total_sum = sum_of_values(numeric_dict)

print("Dictionary:", numeric_dict)
print("Sum of all values:", total_sum)


#Write a Python code to demonstrate the sorting in descending order of values with lambda function.
values = [10, 5, 8, 2, 7, 3]

sorted_values = sorted(values, key=lambda x: -x)

print("Original values:", values)
print("Sorted values in descending order:", sorted_values)
