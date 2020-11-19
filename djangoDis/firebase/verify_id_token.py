import argparse
from firebase_admin import auth

from init_admin import app

def get_uid(id_token):
    return auth.verify_id_token(id_token, app=app)['uid']

def get_email_arg():
    parser = argparse.ArgumentParser(description="Verify token")
    parser.add_argument("--token", required=True, help="The email address of the new user to be created")

    return parser.parse_args()



if __name__ == "__main__":
    arg = get_email_arg()
    print(f"uid - {get_uid(arg.token)}")