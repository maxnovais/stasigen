import sys

from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'
PAGE_DIR = 'pages'


app = Flask(__name__)
app.config.from_object(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)

'''
IMPORTANT: when building new routes, certify all of them end with a trailing
slash ('/'). Otherwise, when you run the build, Flask-Frozen will complain
about a MimetypeMismatchWarning between text/html and application/octet-stream.
'''

@app.route("/")
def index():
    """ On the index page of the site show a list of posts. """
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    return render_template('index.html', posts=posts)


@app.route('/pages/<name>/')
def page(name):
    """ 
    For non-blogpost type pages, e.g. About.
    They serve for the purpose of being specifically linked, for example, 
    on the site menu or other places.
    """
    path = '{}/{}'.format(PAGE_DIR, name)
    page = flatpages.get_or_404(path)
    return render_template('page.html', page=page)


@app.route('/posts/<slug>/')
def post(slug):
    """ For posts only. """
    posts = [p for p in flatpages if (
        p.path.startswith(POST_DIR)) and (p.meta['slug']==slug)]
    try:
        post = posts[0]
    except:
        post = None
    return render_template('post.html', post=post)


@app.route('/posts/tag/<string:tag>/')
def tag(tag):
    ''' Show all posts from a tag (remember: pages do not have tags). '''
    tagged = [p for p in flatpages if (
        tag in p.meta.get('tags', []) and (p.path.startswith(POST_DIR)))]
    return render_template('tag.html', posts=tagged, tag=tag)


@app.route('/posts/tags/')
def tags():
    ''' Show all tags applied to Posts. '''
    tags_list = []
    for p in flatpages:
        if ((p.path.startswith(POST_DIR)) and (p.meta['public'])):
            post_tags = p.meta.get('tags', [])
            for t in post_tags:
                tags_list.append(t)
    unique_tags = sorted(set(tags_list))
    return render_template('tags.html', all_tags=unique_tags)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)

