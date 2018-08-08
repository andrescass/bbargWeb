from flask import Flask,jsonify,json

from . import apis
from .. import db
from ..models import Lore

@apis.route('/getLores', methods=['GET'])
def getLoreList():
	lores = Lore.query.all()

	loreList = []

	for lor in lores:
		lorDict = {
		'title': lor.title,
		'loreBody': lor.loreBody,
		'imageUri': lor.imageUrl
		}
		loreList.append(lorDict)

	jsonStr = json.dumps(loreList)


	resp = jsonify(loreList)

	return resp


