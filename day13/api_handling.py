import requests

def fetch_api():
    url = "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"
    
    req = requests.get(url)
    req_data = req.json()
    
    if req_data['success'] and 'data' in req_data:
        for res in req_data['data']['data']:
            print(f"{res['id']}.  {res['content']}")
    

def main():
    try:
        fetch_api()
    except Exception as e:
        print(str(e))
    

if __name__ == "__main__":
    main()