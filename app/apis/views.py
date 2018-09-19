from flask import Flask,jsonify,json

from . import apis
from .. import db
from ..models import Lore, Hunter, NewsModel, VideoModel

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

@apis.route('/getNews', methods=['GET'])
def getNews():
	newses = NewsModel.query.all()

	newsList = []

	for nius in newses:
		niusDict = {
		'ID': nius.id,
		'title': nius.title,
		'newsBody': nius.newsBody,
		'imageUri': nius.imageUrl
		}
		newsList.append(niusDict)

	jsonStr = json.dumps(newsList)


	resp = jsonify(newsList)

	return resp

@apis.route('/getVideos', methods=['GET'])
def getVideos():
	videos = VideoModel.query.all()

	videoList = []

	for video in videos:
		videoDict = {
		'ID': video.id,
		'title': video.name,
		'videoBody': video.videoBody,
		'videoUri': video.videoUrl
		}
		videoList.append(videoDict)

	jsonStr = json.dumps(videoList)


	resp = jsonify(videoList)

	return resp