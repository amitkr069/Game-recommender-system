import streamlit as st
import pickle
import pandas as pd
import requests

#api - https://api.rawg.io/api/games/10001?key=2844174cac8840dbaa62ca5fb474aacb

#for fetching posters through api
def fetch_poster(game_id):
    response = requests.get('https://api.rawg.io/api/games/{}?key=2844174cac8840dbaa62ca5fb474aacb'.format(game_id))
    data = response.json()
    return data['background_image']

def recommend(game):
    game_index = games[games['title'] == game].index[0]
    distances = similarity[game_index]
    games_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[2:12]

    recommended_games = []
    recommend_posters = []
    for i in games_list:
        game_id = games.iloc[i[0]].id
        recommended_games.append(games.iloc[i[0]].title)

        # fetch poster from API
        recommend_posters.append(fetch_poster(game_id))
    return recommended_games,recommend_posters
    #returning both movies and posters


#movies_list = pickle.load(open('movies.pkl', 'rb'))
#movies = movies_list['title'].values

similarity = pickle.load(open('similarity_game.pkl', 'rb'))
#if dierct new_df wla nii chale then
games_dict = pickle.load(open('game_dict.pkl', 'rb'))
games = pd.DataFrame(games_dict)

# av direct ye new_df wla pickle ho rha h but video me nii ho rha tha
# so we will pass the dictionary of the data frame

st.title('Game Recommender System')

selected_game = st.selectbox(
    "games u may like?",
    #movies)
     games['title'].values) #if new_df direct na chale

if st.button("Recommend"):
    names, posters = recommend(selected_game)  #isme recommended funcction me selected movie ka naam denge and similiar like
    # google colab ka recommend wala function ye v same kaam karega

    # for i in recommendations:
    #     st.write(i)  #isme only names display kra rhe the


    #it is to display both name and image
    # col1, col2, col3, col4, col5 = st.columns(5)
    # with col1:
    #     st.text(names[0])
    #     st.image(posters[0])
    #
    # with col2:
    #     st.text(names[1])
    #     st.image(posters[1])
    #
    # with col3:
    #     st.text(names[2])
    #     st.image(posters[2])
    #
    # with col4:
    #     st.text(names[3])
    #     st.image(posters[3])
    #
    # with col5:
    #     st.text(names[4])
    #     st.image(posters[4])


    #it is through iteration of the uppper code
    cols = st.columns(10)
    for i in range(10):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])

    # cols1 = st.columns(5)
    # cols2 = st.columns(5)
    # for i in range(5):
    #     with cols1[i]:
    #         st.text(names[i])
    #         st.image(posters[i])
    #
    # for j in range(5, 10):
    #     with cols1[j]:
    #         st.text(names[j])
    #         st.image(posters[j])

