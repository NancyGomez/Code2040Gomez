import requests # for 'requests' which retrieves information from a url
import ast # for literal_eval()

# created a token that uses the key words 'token' and 'github' to refer to the
# token given on the website and my github repository
token = {'token':'0b89ba5ce586dc2507ea2871fd430657',
         'github':'https://github.com/NancyGomez/Code2040Gomez'}

# finally I send in my result and check to see if my code is correct
req = requests.post('http://challenge.code2040.org/api/haystack/validate',
print(req.text)
