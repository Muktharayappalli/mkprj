import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from backend.db import dbconn
from bson.objectid import ObjectId
from backend import logger

@api_view(['POST'])
def signup(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password or not email:
            logger.warning("Signup attempt with missing fields: %s", request.data)
            return Response({'message': 'All fields are required'}, status=400)
        
        existing_user = dbconn.user.find_one({'$or': [{'username': username}, {'email': email}]})
        if existing_user:
            logger.warning("Username or email already exists: %s", {'username': username, 'email': email})
            return Response({'message': 'Username or email already exists'}, status=400)

        user_data = {
            'username': username,
            'password': password,
            'email': email
        }
        result = dbconn.user.insert_one(user_data)

        inserted_user = dbconn.user.find_one({'_id': ObjectId(result.inserted_id)})

        inserted_user.pop('_id')
        logger.info("User created successfully: %s", inserted_user)

        return Response({'message': 'User created successfully', 'user': inserted_user})

    except Exception as e:
        logger.error("Error in signup: %s", str(e))
        return Response({'message': 'Internal server error'}, status=500)


@api_view(['POST'])
def sign_in(req):
    try:
        data = json.loads(req.body)

        if 'username' not in data:
            logger.warning("Login attempt missing username: %s", data)
            return Response({'message': 'Username not found'}, status=400)
        
        if 'password' not in data:
            logger.warning("Login attempt missing password: %s", data)
            return Response({'message': 'Password not found'}, status=400)

        query = {
            'username': data['username'],
            'password': data['password']
        }

        auth = dbconn.user.find_one(query)

        if auth:
            logger.info("Login success for username: %s", data['username'])
            return Response({'message': 'Login success'}, status=200)
        else:
            logger.warning("Invalid login attempt for username: %s", data['username'])
            return Response({'error': 'Invalid username or password'}, status=401)

    except Exception as e:
        logger.error("Error in sign_in: %s", str(e))
        return Response({'message': 'Internal server error'}, status=500)