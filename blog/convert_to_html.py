#!/usr/bin/env python3

# must be executed from blog dir

import os
import markdown

def clean_up_name(s: str) -> str:
  return s.replace('_', ' ')

def clean_up_body(s: str) -> str:
  res = ''
  lines = s.splitlines()
  for i, l in enumerate(lines):
    if i == 0:
      res += l + '\n'
    elif i == len(lines) - 1:
      res += ' ' * 8 + l
    else:
      res += ' ' * 8 + l + '\n'
  return res

# convert all
for fname in filter(lambda f: f.endswith('.md'), os.listdir('./md')):
  with open('./md/' + fname, 'r') as f:
    text = f.read()
    fname = fname.replace('.md', '')
    body = markdown.markdown(text)
    with open('.html_template', 'r') as f:
      html = f.read().format(name=clean_up_name(fname), body=clean_up_body(body))
      fname = fname + '.html'
      with open('./html/' + fname, 'w') as f:
        f.write(html)
