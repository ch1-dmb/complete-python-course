import re
'''
Practice Questions: 
Using Both [] and ()
Extract domain names from email addresses
Input: "Contact us at support@example.com and admin@website.org"
Expected Output: ['example.com', 'website.org']
'''
info1 = "Contact us at support@example.com and admin@website.org"
pattern1 = r"\@([a-z]+\.[a-z]+)"
# pattern1 = r"@([a-zA-Z0-9.-]+\.[a-zA-Z]+)" 
pattern1_list = re.findall(pattern1, info1)
print(pattern1_list)


'''
Extract phone numbers in the format (XXX) XXX-XXXX
Input: "Call (123) 456-7890 or (987) 654-3210"
Expected Output:

('123', '456', '7890')
('987', '654', '3210')
'''
info2 = "Call (123) 456-7890 or (987) 654-3210"
pattern2 = r"\((\d{3})\)\s(\d{3})\-(\d{4})"
# pattern1 = r"@([a-zA-Z0-9.-]+\.[a-zA-Z]+)" 
pattern2_list = re.findall(pattern2, info2)
print(pattern2_list)


'''
Extract hashtags from a tweet
Input: "Loving #regex and #coding! #100DaysOfCode"
Expected Output: ['#regex', '#coding', '#100DaysOfCode']
'''

info3 = "Loving #regex and #coding! #100DaysOfCode"
# pattern3 = r"(\#[a-zA-Z0-9]+)"
pattern3 = r"#\w+"

pattern3_list = re.findall(pattern3, info3)
print(pattern3_list)
'''
Extract words that start with a capital letter
Input: "Today John and Sarah went to New York."
Expected Output: ['Today', 'John', 'Sarah', 'New', 'York']
'''

info4 = "Loving #regex and #coding! #100DaysOfCode"

pattern4 = r"#\w+"

pattern4_list = re.findall(pattern4, info4)
print(pattern4_list)
'''
Bonus Challenge Question
Extract valid filenames ending in .jpg, .png, .gif, or .jpeg
Input: "My images: photo.jpg, image.png, doc.pdf, avatar.gif, banner.jpeg"
Expected Output: ['photo.jpg', 'image.png', 'avatar.gif', 'banner.jpeg']
'''

info5 = "My images: photo.jpg, image.png, doc.pdf, avatar.gif, banner.jpeg"

pattern5 = r"\s(\w+\.\w+)"

pattern5_list = re.findall(pattern5, info5)
print(pattern5_list)