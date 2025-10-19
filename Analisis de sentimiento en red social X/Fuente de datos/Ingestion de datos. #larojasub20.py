import tweepy 
import json

# Configuracion de la API de X para obtener tweets.

client = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAGoV4wEAAAAAyFl1rOAGC%2Fo8bVPab%2BCAgrTz7QI%3DA70xIVbCLzhMx0jQm8mIzkfP5IcqFEcDn0xrN6ylhuGcFEM6qA")


query = "#larojasub20 -is:retweet lang:es" # Hashtag para buscar tweets relacionados a la roja sub20 
tweets = client.search_recent_tweets(query=query, tweet_fields=['id','text','created_at','author_id','geo','note_tweet'], max_results=79) # Los datos que queremos obtenerD de cada tweet

# Guardar los datos en un archivo JSON
with open('tweets_crudos_laroja.json', 'w', encoding='utf-8') as f:
    for tweet in tweets.data:
        json.dump(tweet.data, f)
        f.write('\n')

