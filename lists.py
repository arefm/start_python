# - *-coding: utf- 8 - *-

#Lists in Python
"""
languages = list()

languages.append('Python')
languages.append('Ruby')
languages.append('Nodejs')
languages.append('Go')
"""

languages = ['Go', 'Nodejs', 'Php', 'Python', 'Ruby', 'Scala']
libraries = ['jquery', 'zepto']
# languages = sorted(languages)
first = languages[0] # 1, 1:, :1, 1:3

#get length
lanCnt = len(languages)

#concatination
conc = languages + libraries

#repetition
rpt = languages[1:2] * 3

#membership
member = 'ASPX' in languages

#iteration
for lang in languages:
	print lang

# print member