#!/usr/bin/env python
import tweepy

#from our keys module (keys.py), import the keys dictionary
from keys import keys

print("o bot está rodando!!")

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

twt = api.search(q="um tweet extremamente especifico para nao dar erro no bot assinado pjmfIeur")

#list of specific strings we want to check for in Tweets
t = ['um tweet extremamente especifico para nao dar erro no bot assinado pjmfIeur']

for s in twt:
    for i in t:
        if i == s.text:
            sn = s.user.screen_name
            m = "@%s Hello!" % (sn)
            s = api.update_status(m, s.id)

'''console.log('Este bot está rodando...');

var tweetsRespondidos = [''];
var respostasTweet = [''];

function encontrarTweets(){
 
    Bot.get("search/tweets", {q: 'oi @nomebot' }, (err, data) => {
        if (err) {
            console.log(err.message);
        } else {
            console.log('achou!');
            var tweetId = data.statuses[0].id_str;
            var username = data.statuses[0].user.screen_name;
            var mostrarRespostas = respostasTweet[Math.floor((Math.random() * respostasTweet.length))];
  
            if (tweetsRespondidos.includes(tweetId)){
                console.log('Esse tweet já foi respondido!');
            } else {
                Bot.post('statuses/update', Bot.post('statuses/update', { in_reply_to_status_id: tweetId, status: `@${username} ${mostrarRespostas}` }, function(err){
                    console.log('Respondeu ao: ', tweetId);
                    if (err) {
                        console.log(err.message);
                    }
                }))
            }
          
            tweetsRespondidos.push(tweetId);
        }
    })
} setInterval(encontrarTweets, 60000);
'''