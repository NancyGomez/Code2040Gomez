import requests # for 'requests' which retrieves information from a url
import ast # for literal_eval()

# created a token that uses the key words 'token' and 'github' to refer to the
# token given on the website and my github repository
token = {'token':'0b89ba5ce586dc2507ea2871fd430657',
         'github':'https://github.com/NancyGomez/Code2040Gomez'}

# sending the token to the register given by the website
req = requests.post('http://challenge.code2040.org/api/haystack', json = token)

# in order to access the actual values from the request, I will use the ast lib
# function literal_eval which turns it into a dict I can access
my_dict = ast.literal_eval(req.text)

# now I need to store the actual value associated with the key 'needle'
needle = my_dict['needle']

# then, I need to find the index where the needle value is at in the haystack
index = my_dict['haystack'].index(needle)

# Updated the dictionary with the key 'needle' and value index
token = {'token':'0b89ba5ce586dc2507ea2871fd430657', 'needle': index}

# finally I send in my result and check to see if my code is correct
req = requests.post('http://challenge.code2040.org/api/haystack/validate',
                     json = token)
print(req.text)
