# app/apis/__init__.py

from flask import Blueprint

apis = Blueprint('apis', __name__)

from . import views