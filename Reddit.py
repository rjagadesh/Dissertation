import requests
import praw

def get_access_token(code):
    client_auth = requests.auth.HTTPBasicAuth('t9k4MDfCoep_xxYk1rbKA', 'fYQZUf5i1_1q405g8qn-fY0lkqvmVM4g')
    post_data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://localhost:8080"
    }
    headers = {"User-Agent": "WebApp/1.0 by Able-Firefighter4749"}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    token_json = response.json()
    if 'access_token' in token_json:
        return token_json["access_token"]
    else:
        print("Failed to retrieve access token:", token_json)  # Print error message from Reddit
        return None

def generate_auth_url():
    client_id = 't9k4MDfCoep_xxYk1rbKA'
    redirect_uri = 'http://localhost:8080'
    scope = 'read'
    state = 'SOME_RANDOM_STRING'
    auth_url = (f"https://www.reddit.com/api/v1/authorize?client_id={client_id}"
                f"&response_type=code&state={state}&redirect_uri={redirect_uri}"
                f"&duration=temporary&scope={scope}")
    return auth_url

def main(code):
    access_token = get_access_token(code)
    if access_token:
        reddit = praw.Reddit(client_id='t9k4MDfCoep_xxYk1rbKA',
                             client_secret='fYQZUf5i1_1q405g8qn-fY0lkqvmVM4g',
                             user_agent='WebApp/1.0 by Able-Firefighter4749',
                             refresh_token=access_token)
        
        # Example usage: print 10 hot posts from the Python subreddit
        for submission in reddit.subreddit('python').hot(limit=10):
            print(submission.title)
    else:
        print("Error: Unable to obtain access token.")

if __name__ == "__main__":
    print("Visit this URL to authorize:", generate_auth_url())
    auth_code = input("Enter the authorization code: ")
    main(auth_code)
