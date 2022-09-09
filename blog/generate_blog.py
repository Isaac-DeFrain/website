import os
import convert_to_html

# convert md to html + metadata
convert_to_html.main()

# TODO tags

toc = ''
toc_items = ''

articles = ''
article_items = ''

# get the metadata
for fname_html in filter(lambda f: f.endswith('.html'), os.listdir('./html')):
  fname = fname_html.replace('.html', '')
  # generate toc item
  with open('.toc_item_template', 'r') as f:
    with open('./html/meta/name/' + fname, 'r') as n:
      toc_items += f.read().format(fname=fname_html, name=n.read()) + '\n'
  # generate article item
  with open('.article_template', 'r') as f:
    with open('./html/meta/title/' + fname, 'r') as t:
      with open('./html/meta/description/' + fname, 'r') as d:
        article_items += f.read().format(fname=fname_html, title=t.read(), description=d.read()) + '\n'
  # generate toc
  with open('.toc_template', 'r') as f:
    toc = f.read().format(toc_items=toc_items)
  # generate articles
  with open('.articles_template', 'r') as f:
    articles = f.read().format(article_items=article_items)

# generate the main blog html
with open('.blog_template', 'r') as f:
  blog = f.read().format(articles=articles, toc=toc)
  with open('blog.html', 'w') as f:
    f.write(blog)
