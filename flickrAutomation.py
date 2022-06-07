import requests
response = requests.get(" https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=b7b910748bc066f4dfa7967c61e9c857&user_id=195789692%40N03&format=json&nojsoncallback=1")
if(response.status_code==200):
    print("request sucessfull....")
    print("printing Data.............")
    print(response.json())
else:
    print("some error occured")