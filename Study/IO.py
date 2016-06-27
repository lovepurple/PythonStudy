#序列化与反序列化
import io
import pickle

#序列化
with open("d:\\testIO.txt","wb") as f:
	d = dict(name="lovepurple",age=20,score=99)
	pickle.dump(d,f)

#反序列化
with open("d:\\testIO.txt","rb") as f:
	d = pickle.load(f)
	print(d)

#python对JSON支持非常好
import json
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)