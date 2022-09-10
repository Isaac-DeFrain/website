#!/usr/bin/env python3

# must be executed from blog dir

from functools import reduce
import os
import markdown

def clean_up_name(s):
  return s.replace('_', ' ')

def indent(s, n):
  return reduce(
    lambda a, b: '{a}\n{w}{b}'.format(a=a, b=b, w=' ' * n),
    s.splitlines())

# parse title, name, summary, and tags from md file
def parse_meta(src):
  t = False # collecting tags
  d = False # collecting summary lines
  meta = {'name' : None, 'title' : None, 'description' : None, 'tags' : None}
  desc = ''
  tags = []
  src = src.splitlines()
  for l in src:
    if l.startswith('@name'):
      meta['name'] = l.split(':')[1].strip()
    elif l.startswith('@title'):
      meta['title'] = l.split(':')[1].strip()
    # start tag collection
    elif l.startswith('@tags'):
      t = True
      d = False
    # start description collection
    elif l.startswith('@description'):
      d = True
      t = False
    # end comment block
    elif l.startswith('-->'):
      d = False
      t = False
      meta['description'] = desc
      meta['tags'] = map(lambda s: s.strip(), tags)
      return meta
    # collect description
    elif d:
      desc += l.strip() + '\n'
    # collect tags
    elif t:
      tags += l.split('-')[1:]

def main():
  # convert all md to html + metadata
  for fname in filter(lambda f: f.endswith('.md'), os.listdir('./md')):
    with open('./md/' + fname, 'r') as f:
      og = f.read()
      body = markdown.markdown(og)
      meta = parse_meta(og)
      fname = fname.replace('.md', '')
      # grab the html template and format it
      with open('.html_template', 'r') as f:
        html = f.read().format(name=clean_up_name(fname), body=indent(body, 8))
        # write html to /html
        with open('./html/' + fname + '.html', 'w') as f:
          f.write(html)
        # write metadata to /html/meta
        if meta:
          # write name to /html/meta/name
          if meta['name']:
            with open('./html/meta/name/' + fname, 'w') as f:
              f.write(meta['name'])
          # write title to /html/meta/title
          if meta['title']:
            with open('./html/meta/title/' + fname, 'w') as f:
              f.write(meta['title'])
          # write description to /html/meta/description
          if meta['description']:
            with open('./html/meta/description/' + fname, 'w') as f:
              f.write(meta['description'])
          # write tags to /html/meta/tags
          if meta['tags']:
            with open('./html/meta/tags/' + fname, 'w') as f:
              f.write(reduce(lambda a, b: a + '\n' + b, meta['tags']))
