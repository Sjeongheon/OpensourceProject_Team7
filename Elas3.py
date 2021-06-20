#!/usr/bin/python3

from elasticsearch import Elasticsearch

es_host="127.0.0.1"
es_port="9200"

def create_index():
	if not es.indices.exists(index=index):
		return es.indices.create(index=index)

def delete_index():
	if es.indices.exists(index=index):
		return es.indices.delete(index=index)

def insert(body):
	return es.index(index=index, doc_type=doc_type, body=body)

def delete(data):
	if data is None:
		data = {"match_all": {}}

	else:
		data = {"match": data}

	body = {"query": data}

	return es.delete_by_query(index, body=body)


def search(data=None):
	if data is None:
		data = {"match_all": {}}
	
	else:
		data = {"match": data}

	body = {"query": data}
	res = es.search(index=index, body=body)
	return res

def update(id, doc):
	body = {
		'doc':doc
	}

	res = es.update(index=index, id=id, body=body, doc_type=doc_type)
	return res

if __name__ == '__main__':

	es = Elasticsearch([{'host':es_host, 'port':es_port}], timeout=30)
	
	index = ''
	doc_type = 'times'

#	data = {
#		'date': '20210620',
#		'category': 'Tech',
#		'Title': 'Dumb Money',
#		'content': 'When the young Oracle heir enterd the entertainment industry~~'
#		
#	}

#	ir = insert(data)
#	print(ir)
	sr = search()
	print(sr)	
