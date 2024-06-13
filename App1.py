import streamlit as st
import pickle
import pandas as pd
import requests

#for fetching posters through api
def fetch_poster(game_id):
    response = requests.get('https://api.rawg.io/api/games/{}?key=2844174cac8840dbaa62ca5fb474aacb'.format(game_id))
    data = response.json()
    if 'background_image' in data:
        return data['background_image']
    else:
        return "no image"


def recommend(game):
    game_index = games[games['title'] == game].index[0]
    distances = similarity[game_index]
    games_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[2:12]

    recommended_games = []
    recommend_posters = []
    no_image = 'no-image.png'
    for i in games_list:
        game_id = games.iloc[i[0]].id
        recommended_games.append(games.iloc[i[0]].title)

        # fetch poster from API
        if fetch_poster(game_id) == "no image":
            recommend_posters.append(no_image)
        else:
            recommend_posters.append(fetch_poster(game_id))
    return recommended_games,recommend_posters
    #returning both movies and posters


#movies_list = pickle.load(open('movies.pkl', 'rb'))
#movies = movies_list['title'].values

similarity = pickle.load(open('similarity_game.pkl', 'rb'))
#if dierct new_df wla nii chale then
games_dict = pickle.load(open('game_dict.pkl', 'rb'))
games = pd.DataFrame(games_dict)


st.title('Game Recommender System')

selected_game = st.selectbox(
    "games u may like?",
     games['title'].values) #if new_df direct na chale

if st.button("Recommend"):
    names, posters = recommend(selected_game)
    
    cols = st.columns(10)
    for i in range(10):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])


