import requests # for 'requests' which retrieves information from a url
import ast # for literal_eval()
# in order to efficiently work with the datestamp, I use the datetime data type
from datetime import date, datetime, time, timedelta

# created a token that uses the key words 'token' and 'github' to refer to the
# token given on the website and my github repository
token = {'token':'0b89ba5ce586dc2507ea2871fd430657',
         'github':'https://github.com/NancyGomez/Code2040Gomez'}
         
# sending the token to the register given by the website
req = requests.post('http://challenge.code2040.org/api/dating', json = token)

# storing the dictionary returned from the post
r_dict = ast.literal_eval(req.text)

# transform the string that was entered into a datetime object with the format:
stamp = datetime.strptime(r_dict['datestamp'], '%Y-%m-%dT%H:%M:%SZ')

# format the datetime object into a string format within ISO 8601, but
# this format doesn't add the Z, so it's manually appended at the end
updated = datetime.isoformat(stamp + timedelta(seconds=r_dict['interval'])) + 'Z'

# update token to hold my resulting date
token = {'token':'0b89ba5ce586dc2507ea2871fd430657', 'datestamp': updated}

# finally, I send in my result and check to see if my code is correct
req = requests.post('http://challenge.code2040.org/api/dating/validate',
                     json = token)
print(req.text)
