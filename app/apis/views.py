from flask import Flask,jsonify,json

from . import apis
from .. import db
from ..models import Lore, Hunter

@apis.route('/getLores', methods=['GET'])
def getLoreList():
	lores = Lore.query.all()

	loreList = []

	for lor in lores:
		lorDict = {
		'ID': lor.id,
		'title': lor.title,
		'loreBody': lor.loreBody,
		'imageUri': lor.imageUrl
		}
		loreList.append(lorDict)

	jsonStr = json.dumps(loreList)


	resp = jsonify(loreList)

	return resp

@apis.route('/getHunters', methods=['GET'])
def getHunterList():
	hunters = Hunter.query.all()

	hunterList = []

	for hunt in hunters:
		huntDict = {
		'ID': hunt.id,
		'name': hunt.name,
		'position': hunt.position,
		'lastPos': hunt.lastPosition
		}
		hunterList.append(huntDict)

	jsonStr = json.dumps(hunterList)


	resp = jsonify(hunterList)

	return resp

