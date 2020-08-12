
from random import choice
from flask import Flask, jsonify, request, Response
import requests
from license_sever import LICENSE_SEVER


license_sever = LICENSE_SEVER()


desktop_agents = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']


def random_headers():
    return {'User-Agent': choice(desktop_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}



def jsonify_str(output_list):
    with app.app_context():
        with app.test_request_context():
            result = jsonify(output_list)
    return result


app = Flask(__name__)


def create_query_result(input_url, results, error=None):
    if error is not None:
        results = 'Error: ' + str(error)
    query_result = {
        'results': results
    }
    return query_result


@app.route("/generate_license", methods=['GET', 'POST'])
def generate_license_query():


    email = request.args.get('email', default='', type=str)
    print(email)
    data = {"email": email}
    license_generated = license_sever.genLicense(data=data)
    if license_generated is None:
        result = {"Result": "License already exists"}
    else:
        result = {"Email: ": email, "License" : license_generated}
    return jsonify_str(result)



@app.route("/check_license", methods=['POST', 'GET'])
def checkLicenseQuery():
    data_json = request.get_json()
    print(data_json)

    res = license_sever.checkLicense(data_json['license'])
    # print(res)
    return jsonify(result=res)



app.run("localhost", 1915, threaded=True, debug=False)

