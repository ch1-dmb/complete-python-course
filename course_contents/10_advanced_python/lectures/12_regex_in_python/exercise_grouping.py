import re
'''
Practice Questions: 
Using () (Grouping & Capturing)
Extract all prices from a string (capture the numeric part after $).
Input: "The prices are $99.99, $20, and $5.50."
Expected Output: ['99.99', '20', '5.50']
'''
info1 = "The prices are $99.99, $20, and $5.50."
# pattern1 = r"[\d\.]+\d"
pattern1 = r"\$(\d+(\.\d+)?)"
info1_list = re.findall(pattern1, info1)
# print(info1_list)
info1_result = [i[0]for i in info1_list]
print(info1_result)
'''
Extract full names from a list (first name and last name).
Input: "John Doe, Alice Smith, Bob Johnson"
Expected Output: ['John Doe', 'Alice Smith', 'Bob Johnson']
'''

info2 = "John Doe, Alice Smith, Bob Johnson, robert Jelly"
# pattern1 = r"[\d\.]+\d"
pattern2 = r"([A-Z][a-z]+)\s([A-Z][a-z]+)"

# pattern2 = r"()"
info2_list = re.findall(pattern2, info2)
info_result = [' '.join(i) for i in info2_list]

print(info2_list)
# print(info_result)
# info2 = "John Doe, Alice Smith, Bob Johnson"
# pattern2 = r"([A-Z][a-z]+)\s([A-Z][a-z]+)"

# info2_list = re.findall(pattern2, info2)
# full_names = [' '.join(name) for name in info2_list]  # Join the first and last names
# print(full_names)

'''
Extract dates in YYYY-MM-DD format and separate year, month, day
Input: "Event dates: 2024-02-19, 2025-06-30"
Expected Output:

('2024', '02', '19')
('2025', '06', '30')
'''

info3 = "Event dates: 2024-02-19, 2025-06-30"
# pattern1 = r"[\d\.]+\d"
pattern3 = r"\s(\d{4}\-\d{2}\-\d{2})"
info3_list = re.findall(pattern3, info3)

print(info3_list)