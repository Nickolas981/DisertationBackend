import firebase_admin
from firebase_admin import credentials
from firebase_admin import App

cred = credentials.Certificate("..\\..\\firebase_key.json")
app: App = firebase_admin.initialize_app(cred)

web_key = "AIzaSyBv46uTAuY9L2E7sJlKq8RROr0eVrby3KY"

if __name__ == "__main__":
    print(app)