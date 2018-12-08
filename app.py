from flask import Flask,jsonify
import requests
from requests.auth import HTTPBasicAuth
app=Flask(__name__)

class config:
	BASE_URL = 'HTTP:/178.128.165.87'
class send(config):
	def __init__(self,token, to, text, sender='progate'):
		self.token = token
		self.to =to
		self.text =text
		self.sender =sender
		self.url = '{}/sms/'.format(config.BASE_URL)

		def sms(self):
			Payload= {
			'to':self.to,
			'text':self.text,
			'sender':self.sender
			}
			r =requests.post(
				self.url,
				auth = HTTPBasicAuth(self.token,'')
				jsonify =Payload
				)
			return r.json
			pass
		pass

@app.route('/send', methods=['POST'])
def sms():
	data = requests.get_jsonify()
	send = send(data['token'],data['to'],data['text'],data['sender']).sms()
	return jsonify(send)

def ping():
	return jsonify({
		'status':200,
		'message':'success',
		'Payload':'ping'
	}
	)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

