import sys

from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

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
    '''
    print "------"
    for p in pages:
        print repr(p.meta)
    print "------"
    '''
    return render_template('index.html', flatpages=flatpages)


@app.route('/<path:path>/')
def page(path):
    page = flatpages.get_or_404(path)
    return render_template('page.html', page=page)


@app.route('/tag/<string:tag>/')
def tag(tag):
    tagged = [p for p in flatpages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', flatpages=tagged, tag=tag)


@app.route('/tags/')
def tags():
    tags_list = []
    for p in flatpages:
        if p.meta['public']:
            page_tags = p.meta.get('tags', [])
            for t in page_tags:
                tags_list.append(t)
    unique_tags = sorted(set(tags_list))
    return render_template('tags.html', all_tags=unique_tags)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)

