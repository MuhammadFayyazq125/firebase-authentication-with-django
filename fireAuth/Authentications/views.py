from django.shortcuts import render
import pyrebase as pb
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
config = {
    'apiKey': "AIzaSyBShaj0FjiiOGl_BlOnKSEMpRrAh7DLaD4",
    'authDomain': "learning-firestore-42cc5.firebaseapp.com",
    'projectId': "learning-firestore-42cc5",
    'storageBucket': "learning-firestore-42cc5.appspot.com",
    'messagingSenderId': "833279964632",
    'appId': "1:833279964632:web:860c9210f7d6208201eead",
    'measurementId': "G-PN3QP0YW2S",
    'databaseURL': "https://learning-firestore-42cc5-default-rtdb.firebaseio.com",
}

firebse_auth = pb.initialize_app(config)
auth = firebse_auth.auth()
# db = firebse_auth.database()

if not firebase_admin._apps:
    cred = credentials.Certificate("F:/firebase authentication/fireAuth/learning-firestore-42cc5-firebase-adminsdk-oppb6-c6418a46df.json")
    firebase_admin.initialize_app(cred)
    firebase_admin.get_app()
    
db = firestore.client()

# Create your views here.
def index(request):
    return render(request, 'index.html')
def signIn(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = auth.sign_in_with_email_and_password(email,password)
    context = {
        'e': email
    }
    data = db.collection('auth user').document()
    data.set({
        'user':user
    })
    return render(request, 'welcome.html', context)

def addUser(request):
    try:
        email = request.POST.get('email')
        password = request.POST.get('password')
        # creating a user with the given email and password
        user=auth.create_user_with_email_and_password(email,password)
        data = db.collection('users added').document()
        data.set({
        'user':user
            })
        # data = db.collection('users added').document()
        # data.set({
        # 'user':user
        #     })
        # idtoken = request.session['uid']
        # uid = user['localId']
    except:
        print("there is something wrong")
        
    # user = auth.create_user_with_email_and_password(email=email,password=password)
    context = {
        'email': email
    }
    return render(request, 'Register.html', context)