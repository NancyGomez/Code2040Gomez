import requests # for 'requests' which retrieves information from a url

# created a token that uses the key words 'token' and 'github' to refer to the
# token given on the website and my github repository
token = {'token':'0b89ba5ce586dc2507ea2871fd430657',
         'github':'https://github.com/NancyGomez/Code2040Gomez'}

# sending the token to the register given by the website
req = requests.post('http://challenge.code2040.org/api/register', json = token)

# printing to see the results of the above
print(req.text)
