import json
import re

with open(input(), 'r') as f:
    j = json.loads(f.read())

#print(json.dumps(j,sort_keys=True,indent=4))

t = j[0]['texto']

# 
tags = re.compile(r'<.*?>')
t2 = tags.sub('', t)
#print(t2)

no_white_spaces = t2.split()
t3 = ' '.join(no_white_spaces)
#print(t3)

no_new_lines = re.compile(r'\n')
t4 = no_new_lines.sub('', t3)
print(t4)
