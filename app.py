import streamlit as st
import pickle
import pandas as pd
teams=['Sunrisers Hyderabad',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders'
    'Kings XI Punjab',
    'Chennai Super Kings',
    'Rajasthan Royals',
    'Delhi Capitals']

cities=['Hyderabad', 'Bangalore', 'Mumbai', 'Delhi', 'Chennai', 'Jaipur',
       'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion',
       'Johannesburg', 'East London', 'Kimberley', 'Bloemfontein',
       'Ahmedabad', 'Cuttack', 'Nagpur', 'Visakhapatnam', 'Kolkata',
       'Sharjah', 'Abu Dhabi', 'Ranchi', 'Raipur', 'Pune',
       'Bengaluru']

pipe = pickle.load(open('pipe.pkl','rb'))
st.title('IPL Win Predictor')

col1,col2 =st.beta_columns(2)

with col1:
    batting_team=st.selectbox('Select the batting team',sorted(teams))

with col2:
    bowling_team=st.selectbox('Select the bowling team',sorted(teams))

selected_city=st.selectbox('Select host city',sorted(cities))

target = st.number_input('Target')

col3,col4,col5=st.beta_columns(3)

with col3:
    score=st.number_input('Score')

with col4:
    overs=st.number_input('Overs completed')

with col5:
    wickets=st.number_input('Wickets out')

if st.button("Predict Probability"):
    runs_left=target-score
    balls_left=120-(overs*6)
    wickets=10-wickets
    crr=score/overs
    rrr=(runs_left*6)/balls_left

    input_df=pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})
    st.table(input_df)
    result= pipe.predict_proba(input_df)
    loss=result[0][0]
    win=result[0][1]
    st.text(batting_team + "-" + str(round(win)) + "%")
    st.text(bowling_team + "-" + str(round(win)) + "%")