#!/usr/bin/env python3

import os
import markdown

def clean_up(s: str) -> str:
  return s.replace('_', ' ')

for fname in os.listdir('.'):
  if fname.endswith('.md'):
    with open(fname, 'r') as f:
        text = f.read()
        fname = fname.replace('.md', '')
        body = markdown.markdown(text)
        html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Quantifier | {name}</title>
  <link rel="stylesheet" href="../styles.css">
</head>
<body>
  <div class="container">
    <!-- Navigation bar -->
    <div class="nav-wrapper">
      <!-- left column -->
      <div class="left-side">
        <div class="brand">
          <div class="brand-logo-wrapper">
            <img src="../images/universal-quantifier-for-all.png">
          </div>
        </div>
      </div>
      
      <!-- right column -->
      <div class="right-side">
        <div class="nav-link-wrapper">
          <a href="../index.html">Home</a>
        </div>
        <div class="nav-link-wrapper">
          <a href="../about.html">About</a>
        </div>
        <div class="nav-link-wrapper active-nav-link">
          <a href="../blog.html">Blog</a>
        </div>
        <div class="nav-link-wrapper">
          <a href="../contact.html">Contact</a>
        </div>
        <div class="nav-link-wrapper">
          <a href="https://www.github.com/Isaac-DeFrain">GitHub</a>
        </div>
      </div>
    </div>

    <!-- Content -->
    <div class="article-content-wrapper">
      <div class="article-body">
        {body}
      </div>
    </div>
  </div>
</body>
</html>
""".format(name=clean_up(fname), body=body)
    fname = fname + '.html'
    with open(fname, 'w') as f:
        f.write(html)
