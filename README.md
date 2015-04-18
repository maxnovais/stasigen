# Static Site Generator

A simple static site generator. 

It is based on initial work by Nicolas, at: https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/ .

## How to use:

- To add content to the site, add markdown files with the extension '.md' to the "pages" directory. 

- To test if everything is all right (layout, content, etc.), you can run as a normal flask app:

        $ python sitebuilder.py 

- Once you checked everything is all right, you can then proceed to generating the static site:

        $ python sitebuilder.py build

- Your static files will then be at the "build" directory. Now you can just copy this folder contents to your webserver.

- BONUS: You can use python also as a static web server:

        $ cd build
        $ python -m SimpleHTTPServer 8888

  Now, just go to your preferred browser and access: http://localhost:8888


