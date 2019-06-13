"""
  created by IAmFiveHigh on 2019-06-05
 """
from . import web
from sqlalchemy import desc
from flask import jsonify, make_response
from app.models.classic import Classic
from app.models.base import db, Base


@web.route('/classic/latest')
def classic_latest():

    latest = Classic.query.filter_by().order_by(desc(Classic.index)).first()
    if latest:
        # 如果存在一条数据
        latest_dict = latest.serialize()
        return jsonify(latest_dict)
    else:
        # 数据库没有数据
        res = make_response()
        res.response = '没有数据'
        res.status_code = 400
        return res


@web.route('/classic/<index>/previous')
def classic_index_previous(index):
    index = int(index) - 1
    previous = Classic.query.filter_by(index=index).first()
    if previous:
        previous_dict = previous.serialize()
        return jsonify(previous_dict)
    else:
        res = make_response()
        res.response = '没有数据'
        res.status_code = 400
        return res


@web.route('/classic/<index>/next')
def classic_index_next(index):
    index = int(index) + 1
    next = Classic.query.filter_by(index=index).first()
    if next:
        next_dict = next.serialize()
        return jsonify(next_dict)
    else:
        res = make_response()
        res.response = '没有数据'
        res.status_code = 400
        return res

@web.route('/classic/addlatest')
def classic_add_latest():
    temp = {
        'content': '人生不能象做菜，把所有料准备好再下锅',
        'fav_num': 11,
        'image': 'http://bl.7yue.pro/images/movie.8.png',
        'index': 8,
        'like_status': 0,
        'pubdate': '2018-06-22',
        'title': '李安《饮食男女》',
        'type': 100
    }

    with db.auto_commit():
        classic = Classic()
        classic.set_attrs(temp)
        db.session.add(classic)
    return "add success"