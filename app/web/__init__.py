"""
  created by IAmFiveHigh on 2019-02-20
 """
from flask import Blueprint

# 蓝图 blueprint
web = Blueprint('web', __name__)

from app.web import test
from app.web import goods
from app.web import comment
from app.web import blink