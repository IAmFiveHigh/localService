"""
  created by IAmFiveHigh on 2019-02-20
 """

from . import web

@web.route('/test/<content>')
def test(content):
    return '<p>content</p>'