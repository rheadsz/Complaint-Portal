from flask import Flask, jsonify, request

app = Flask(__name__)


Electricity = [{'COMPLAINT_ID': "0",
          'complainant': "Mr.Danish Sait",
          'address': " Near Infosys, Urwa Mangalore",
	  'Contact no.': "897654326",
          'description': "Wrong and disproportionate bills"},

         {'COMPLAINT_ID': "1",
          'complainant': "Aditi Hegde",
          'address': "Sai Baba Temple, Chilimbi, Mangalore",
	  'Contact no.': "45678907",
          'description': "Very old bills without notice"}
        ]

Road = [{'COMPLAINT_ID': "0",
          'complainant': "Meaford Pinto",
          'address': "Near Cambridge School, Neeramarga, Mangalore",
	  'contact no.': "1234567890",
          'description': "Potholes and broken roads"},

         {'COMPLAINT_ID': "1",
          'complainant': "Athul SK",
          'address': "Majila Jeppu,Near St.Josephs Seminary, Mangalore",
	  'contact no.': "43267889087",
          'description': "No proper footpath for the pedestrians"}]

Sanitary = [{'COMPLAINT_ID': "0",
          'complainant': "Manish shetty",
          'address': "Nandigudda Mangalore",
	  'contact no.': "4532167890",
          'description': "No proper garbage disposal facility"},

         {'COMPLAINT_ID': "1",
          'complainant': "Aster Machado",
          'address': "Casia High School, Monkey Stand, Mangalore",
	  'contact no.': "5432178906",
          'description': "Open drains "}]

Water = [{'COMPLAINT_ID': "0",
          'complainant': "Disha Attavar",
          'address': "5th Cross, Urwa Mangalore",
	  'contact no.': "6754327896",
          'description': "Bills for others' connection"},

         {'COMPLAINT_ID': "1",
          'complainant': "Meghana Shetty",
          'address': "Bejai New Road, Opp Bejai Market,Bejai, Mangalore",
	  'contact no.': "7654327890",
          'description': "Disconnection without notice and reason"}]


@app.route('/')
def index():
        return "Welcome to the ONLINE COMPLAINT PORTAL"

@app.route("/depts", methods=['GET'])
def get():
        return jsonify(
        {'COMPLAINT REGARDING THE ELECTRICITY DEPARTMENT':Electricity},
        {'COMPLAINT REGARDING THE ROAD DEPARTMENT': Road},
        {'COMPLAINT REGARDING THE SANITARY DEPARTMENT': Sanitary},
        {'COMPLAINT REGARDING THE WATER DEPARTMENT': Water},)

@app.route("/depts/<int:COMPLAINT_ID>",methods={'GET'})
def get_complaint(COMPLAINT_ID):
        return jsonify(
        {'Electricity Department': Electricity[COMPLAINT_ID]},
        {'Road Department': Road[COMPLAINT_ID]},
        {'Sanitary Department': Sanitary[COMPLAINT_ID]},
        {'Water Department': Water[COMPLAINT_ID]})
        
@app.route("/depts/ele/<int:COMPLAINT_ID>",methods={'GET'})
def get_complaint_ele(COMPLAINT_ID):
	if request.method == 'GET':
		if len(Electricity)>0:
			return jsonify(Electricity[COMPLAINT_ID]) 
		else:
			'Nothing Found', 404
			
    
@app.route("/depts/rd/<int:COMPLAINT_ID>",methods={'GET'})
def get_complaint_rd(COMPLAINT_ID):
	if request.method == 'GET':
		if len(Road)>0:
			return jsonify(Road[COMPLAINT_ID]) 
		else:
			'Nothing Found', 404
			
@app.route("/depts/san/<int:COMPLAINT_ID>",methods={'GET'})
def get_complaint_san(COMPLAINT_ID):
	if request.method == 'GET':
		if len(Sanitary)>0:
			return jsonify(Sanitary[COMPLAINT_ID]) 
		else:
			'Nothing Found', 404
@app.route("/depts/wtr/<int:COMPLAINT_ID>",methods={'GET'})
def get_complaint_wtr(COMPLAINT_ID):
	if request.method == 'GET':
		if len(Water)>0:
			return jsonify(Water[COMPLAINT_ID]) 
		else:
			'Nothing Found', 404

			
      
@app.route("/depts", methods=['POST'])
def create():
        new_complaint = {'COMPLAINT_ID': 2,
			'complainant': "Alston Roche",
			'address': "Nandigudda, Mangalore",
			'Contact no.': "876543267",
			'description': "Unclean supply of water"},
        Water.append(new_complaint)
        return jsonify({'Created': new_complaint})



@app.route("/depts/ele/<int:COMPLAINT_ID>",methods=['DELETE'])
def delete_e(COMPLAINT_ID):
        Electricity.remove(Electricity[COMPLAINT_ID])
        return jsonify({'result': True}) 

@app.route("/depts/san/<int:COMPLAINT_ID>",methods=['DELETE'])
def delete_s(COMPLAINT_ID):
        Sanitary.remove(Sanitary[COMPLAINT_ID])
        return jsonify({'result': True})
        
@app.route("/depts/rd/<int:COMPLAINT_ID>",methods=['DELETE'])
def delete_r(COMPLAINT_ID):
        Road.remove(Road[COMPLAINT_ID])
        return jsonify({'result': True})
        
@app.route("/depts/wtr/<int:COMPLAINT_ID>",methods=['DELETE'])
def delete_w(COMPLAINT_ID):
        Water.remove(Water[COMPLAINT_ID])
        return jsonify({'result': True})


if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000, debug=True)






