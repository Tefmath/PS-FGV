import json
import re
import datetime as dt

#file_path = input()
file_path = "/home/bruno/Downloads/noticias_brutas.json"
with open(file_path, 'r') as f:
    j = json.loads(f.read())

#print(json.dumps(j,sort_keys=True,indent=4))

t = j[0]['texto']
#print(t)
t = t.split('\n')
t = t[:len(t)-1]
#print(t)
t = ''.join(t)

#a_tag = re.compile(r'<a.*>')
#t2 = a_tag.sub('',t)
tags = re.compile(r'<.*?>')
t2 = tags.sub('', t)
#print(t2)

no_white_spaces = t2.split()
t3 = ' '.join(no_white_spaces)
#print(t3)

no_new_lines = re.compile(r'\n')
t4 = no_new_lines.sub('', t3)
#print(t4)

d = dt.date.fromisoformat(j[0]['data']).strftime('%d/%m/%Y')
#print(d)

timestamp = r'.*?' + f' {d}' + r'.*?(\d+)h(\d+)'
#print(timestamp)
timestamps = re.compile(timestamp)
t5 = timestamps.sub('', t4)
print(t5)

