import re
# re.findall()
'''
Practice Questions: Using [] (Character Classes)
Find all vowels (a, e, i, o, u) in the string:
Input: "Hello World, regex is amazing!"
Expected Output: ['e', 'o', 'o', 'e', 'e', 'i', 'a', 'a', 'i']
'''

info = "Hello World, regex is amazing!"
pattern = "[aeiou]"
info_list = re.findall(pattern, info)
print(info_list)


'''
Extract all numbers from a string (only digits, no letters or symbols).
Input: "Order 5 pizzas and 2 sodas for $30.50"
Expected Output: ['5', '2', '30', '50']
'''
info2 = "Order 5 pizzas and 2 sodas for $30.50"
pattern2 = r"\d+"
info_list2 = re.findall(pattern2, info2)
print(info_list2)
'''
Find all lowercase words in a sentence (words made only of lowercase letters).
Input: "Python is fun but JAVA and C++ are not lowercase."
Expected Output: ['is', 'fun', 'but', 'and', 'are', 'not', 'lowercase']
'''

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
info3 = "Python is fun but JAVA and C++ are not lowercase."
# Pattern to match lowercase words not followed by an uppercase word
pattern3 = r"\b[a-z]+\b"

info_list3 = re.findall(pattern3, info3)
print(info_list3)  # Expected Output: ['is', 'fun', 'but']

