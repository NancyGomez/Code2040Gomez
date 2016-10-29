import requests # for 'requests' which retrieves information from a url

# created a token that uses the key words 'token' and 'github' to refer to the
# token given on the website and my github repository
token = {'token':'0b89ba5ce586dc2507ea2871fd430657',
         'github':'https://github.com/NancyGomez/Code2040Gomez'}

# sending the token to the register given by the website
req = requests.post('http://challenge.code2040.org/api/reverse', json = token)

# storing the value from the request in a value
string = req.text

# Slicing the array by stepping backwards and storing it into reverse
reverse = string[::-1]

# Updated the dictionary with the key 'needle' and value index
token = {'token':'0b89ba5ce586dc2507ea2871fd430657','string': reverse}

# returning the reversed word back
req = requests.post('http://challenge.code2040.org/api/reverse/validate',
                      json = token)
print(req.text)
