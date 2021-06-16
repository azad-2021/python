#A regular expressin is a set of characters which helps us to find or match other strings or a set of strings using specialized syntax held in a pattern
import re			#import regular expression module
#square brackets [] matches a set ofcharacters

s = "cb"
print(re.search('[abc]',s))

#period matches any single character except \n and these type of characters
s = "sc"
print(re.search('.',s))

#carror symbol '^' is used to check if a string start with a certain character.
s = 'mumbai'
print(re.search('^m',s))

#carror symbol '$' is used to check if a string ends with a certain character.
s = 'mumbai'
print(re.search('i$',s))

#'*' matches zero or more occurance of the pattern left to it
a = re.search('z*','man')
b = re.search('ma*','woman')

print(a)
print(b,'\n')

#'+' matches one or more occurance of the pattern left to it
a = re.search('z+','man')
b = re.search('ma+','woman')

print(a)
print(b,'\n')

#'()' braces matches the exact specify number of occurances
a = re.search('z{2}','man')
b = re.search('a{3}','aaaaa')

print(a)
print(b,'\n')

#'|' vertical bar is used match either one character or another character.
a = re.search('z|x','man')
b = re.search('m|w+','woman')

print(a)
print(b,'\n')

#paranthesis '()' used to group sub patterns for example 'a(m)' matches any string followed by 'am'
a = re.search('a(n)','mansnnn')
b = re.search('a(b)','woman')

print(a)
print(b,'\n')

#backslash for reserved characters
a = re.search('\$a','$abc')
b = re.search('\nb','\nbcc')

print(a)
print(b,'\n')


#Biultin functions
'''
1. findall()
2. search()
3. split()
4. sub()
'''

#findall() search for all occurances that match a given pattern from a string and return a list.
st = "India is my country and"	#there is 2 'nd' in this string
x = re.findall('nd',st)
print(x,'\n')

#search() looks for the pattern at any position in the string. If there is more than one match it returns first match only.
st = "India is my country and"	#there is 2 'nd' in this string
x = re.search('my',st)
print(x,'\n')

#split function returns a list where the string has been split for each match
st = "I love watching movies"	
x = re.split('\s',st)
print(x,'\n')

#sub() function replaces the matches with the text of our choice in a string
st = "I love watching movies"
x = re.sub('\s','2',st)			#'\s' is sapace character
print(x,'\n')

#special character of regular expression

#\A returns a match if the specified characters are at the begning of the string
st = "I love watching movies"
x = re.findall('\Athe',st)	
print(x,'\n')

st = "The India"	#there is 2 'nd' in this string
x = re.findall('\AThe',st)
print(x,'\n')

#\b returns a match where the specified characters are at the begning or end of a word.
st = "I love watching movies"
x = re.findall(r'\bI',st)	
print(x,'\n')

#\B returns a match where the specified characters are present at end of a word.// doubt
st = "I love watching movies"
x = re.findall(r'\Bi',st)	
print(x,'\n')

#\D returns a match where the strings doesn't contain digits. If there is it remove it.
st = "I love watching 1 movies"
x = re.findall('\D',st)	
print(x,'\n')


#sets for regular expressions

st = "I love watching 1 movies"
x = re.findall('[wsz]',st)	
print(x,'\n')

st = "I love watching 1 movies"
x = re.findall('[a-n]',st)				#find all lower characters between a to n
print(x,'\n')

st = "I love watching 1 movies"
x = re.findall('[^wso]',st)			#returns all character accept wsz 	
print(x,'\n')

st = "I love watching 1 movies"		#returns digit between 0-9
x = re.findall('[0-9]',st)	
print(x,'\n')

st = "I love watching 1 movies" #returns all character between a-z or A-Z
x = re.findall('[a-zA-Z]',st)	
print(x,'\n')

#[+] returns '+' character matches in the string
st = "I love watching + 1 movies" #returns all character between a-z or A-Z
x = re.findall('[+]',st)	
print(x,'\n')


sentence = 'horses are fast'

regex = re.compile('(?P<animal>\w+) (?P<verb>\w+) (?P<adjective>\w+)')

matched = re.search(regex, sentence)

print(matched.group(2))

#What will be the output of the following Python code?

sentence = 'horses are fast'

regex = re.compile('(?P<animal>\w+) (?P<verb>\w+) (?P<adjective>\w+)')

matched = re.search(regex, sentence)

print(matched.groupdict())


sentence = 'we are humans'

matched = re.match(r'(.*) (.*?) (.*)', sentence)

print(matched.group(2))

