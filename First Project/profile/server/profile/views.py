import jwt, requests, json

from flask import Blueprint, request, make_response, jsonify 
from flask.views import MethodView

from server.models import User


profile_blueprint = Blueprint('profile',__name__)

class UserDetailView(MethodView):
    """
    User Resource
    """

    def decode_auth_token(self, token):
        try:
            print(token)
            print("entering decode")
            unverified_headers = jwt.get_unverified_header(token)
            #with open("server/profile/keys/public_key.pem", 'r') as file:
            #    public_key_text = file.read()

            #public_key = public_key_text.encode()
            #print("new public key",public_key)
            url = "http://localhost:5000/public/.well-known/jwks.json"
            print(url)
        
    
            public_keys = requests.get(url=url).json()
            print("request successfull",public_keys)
            jwk = public_keys["keys"][0]

            print("jwk",jwk)

            public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))

            print(public_key)

            payload = jwt.decode(
                token,
                key=public_key,
                algorithms = unverified_headers["alg"]
                )
            print(payload)
            return payload['sub']
        
        except jwt.ExpiredSignatureError:
            return "Signature expired. Please login again"

        except jwt.InvalidTokenError:
            return "Invalid token. Please login again"

        except FileNotFoundError:
            return "Public key file not found"

    def get(self):
        # get the auth token
        auth_header = request.headers.get('Authorization')

        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
                print("auth_token",auth_token)
            except IndexError:
                responseObject = {
                    'status': 'fail',
                    'message': 'Bearer token malformed.'
                }
                return make_response(jsonify(responseObject)), 401
        else:
            auth_token = ''
        if auth_token:
            resp = self.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                #print('from instance')
                #print(resp)
                user = User.query.filter_by(id=resp).first()
                responseObject = {
                    'status': 'success',
                    'data': {
                        'user_id': user.id,
                        'name': user.name,
                        'number': user.number,
                        'email': user.email,
                        'location': user.location
                    }
                }
                return make_response(jsonify(responseObject)), 200
            responseObject = {
                'status': 'fail',
                'message': resp
            }
            return make_response(jsonify(responseObject)), 401
        else:
            responseObject = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return make_response(jsonify(responseObject)), 401

class Home(MethodView):
    def get(self):
        return "helloworld"

detail_view = UserDetailView.as_view('user_api')
home_view = Home.as_view('home')

# add Rules for API Endpoints


profile_blueprint.add_url_rule(
        "/profile/detail",
        view_func=detail_view,
        methods = ['GET']
        )
profile_blueprint.add_url_rule(
        "/",
        view_func=home_view,
        methods = ["GET"]
        )
