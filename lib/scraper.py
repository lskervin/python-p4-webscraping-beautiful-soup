from turtle import ht
from bs4 import BeautifulSoup
import requests

# headers = {'user-agent': 'my-app/0.0.1'}
# html = requests.get("https://flatironschool.com/", headers=headers)
# doc = BeautifulSoup(html.text, 'html.parser')

# # the class looks like this class="heading-financier color-white mb-20 text-shadow animate animate-1s"
# # only use the text before the first space in the class attribute "[heading-financier] color-white mb-20 text-shadow animate animate-1s"
# print(doc.select('.heading-primary'))
# output = doc.select('.heading-primary')[0].contents
# # Remove '\t' and '\n' characters
# cleaned_output = [item.replace('\t', '').replace('\n', '') for item in output]
# print(cleaned_output)

headers = {'user-agent': 'my-app/0.0.1'}

# We will be uses the our-courses page
html = requests.get("https://flatironschool.com/our-courses/", headers=headers)

doc = BeautifulSoup(html.text, 'html.parser')

# 
# <h3 class="heading-25-extrabold color-black">
#                                     Software Engineering                                </h3>
courses = doc.select('.heading-25-extrabold.color-black')
# print(doc.select('.heading-25-extrabold.color-black')[0])
for course in courses: 
  print(course.contents[0].strip())