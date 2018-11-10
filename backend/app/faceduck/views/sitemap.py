from faceduck.blueprints import sitemap
from flask import make_response, render_template
from faceduck import core
from faceduck.config import FRONTEND_HOST, FRONTEND_PORT, FRONTEND_PATHS


@sitemap.route('/sitemap.xml')
def sitemap():
    pages = []
    base_url = "http://{}:{}".format(FRONTEND_HOST, FRONTEND_PORT)
    
    # Static pages
    for path in FRONTEND_PATHS:
        url = "{}{}".format(base_url, path)
        pages.append(url)
    
    # User pages
    for user in core.get_all_users():
        path = "/user/{}".format(user.username)
        url = "{}{}".format(base_url, path)
        pages.append(url)

    sitemap_xml = render_template('sitemap.xml', pages=pages)
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"

    return response
