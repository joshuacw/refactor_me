#!/usr/bin/env python
# COMMAND LINE PROGRAM TO DOWNLOAD A USER'S AVATAR FROM GITHUB. USAGE: `PYTHON get_avatar.py <GITHUB_USERNAME>`. 

import sys, json
import argparse
import requests
import shutil

# PARSE COMMAND LINE ARGUMENTS

parser = argparse.ArgumentParser()
parser.add_argument(  'username')
args = parser.parse_args()
# CALL THE GITHUB API AND GET USER INFO
RequestUrl = 'https://api.github.com/users/' + args.username

result = requests.get( RequestUrl )
if result.ok :
    user_info = json.loads(result.content)
    avatarURL = user_info['avatar_url']
else:
    sys.stderr.write( "Error fetching user information for {0}; exiting now, sorry...\n".format(args.username) )
    sys.exit()
# DOWNLOAD AND SAVE IMAGE FILE
I = requests.get(avatarURL , stream=True)
if I.ok:
    
    with open(args.username + '.png' , 'wb') as outfile:
        shutil.copyfileobj( I.raw,  outfile )
