import requests # for 'requests' which retrieves information from a url
import ast # for literal_eval()

# created a token that uses the key words 'token' and 'github' to refer to the
# token given on the website and my github repository
token = {'token':'0b89ba5ce586dc2507ea2871fd430657',
         'github':'https://github.com/NancyGomez/Code2040Gomez'}

# sending the token to the register given by the website
req = requests.post('http://challenge.code2040.org/api/prefix', json = token)

# in order to access the actual values from the request, I will use the ast lib
# function literal_eval which turns it into a dict I can access
my_dict = ast.literal_eval(req.text)

# defined a function that returns true if the word does not include prefix
def noPrefix(word):
    # compares the beginning of the word (up to prefix's length) to the prefix
    return (word[:len(my_dict['prefix'])] != my_dict['prefix'])

# filtered through the elements in the list and it must not have the prefix
# value in order for it to be added to my list
my_list = filter(noPrefix, my_dict['array'])

# updated the dictionary and add in a new keyword 'array'
token = {'token':'0b89ba5ce586dc2507ea2871fd430657','array': my_list}

# finally I send in my result and check to see if my code is correct
req = requests.post('http://challenge.code2040.org/api/prefix/validate',
                     json = token)
print(req.text)
