import streamlit as st
gender = st.radio(label='Gender', options=['Male', "Female"])
age = st.slider(label="Age", min_value=17, max_value=90) # numerical
Edu_lvl = st.selectbox(label='Education Level', options=['3.0','4.0','5.0','6.0','7.0','8.0', '9.0','10.0','11.0', '12.0','13.0', '14.0','15.0', '16.0']) # categorical
marital_status = st.selectbox(label='Work Life Balance', options=[' Never-married', ' Married-civ-spouse' ,' Divorced',
 ' Married-spouse-absent', ' Separated' ,' Married-AF-spouse', ' Widowed']) # categorical
Occupation = st.selectbox(label='Occupation', options=[' Adm-clerical' ,' Exec-managerial', ' Handlers-cleaners', ' Prof-specialty'
 ' Other-service', ' Sales', ' Transport-moving' ,' Farming-fishing',
 ' Machine-op-inspct', ' Tech-support' ,' Craft-repair' ,' Protective-serv',
 ' Armed-Forces', ' Priv-house-serv'])
work_lb = st.selectbox(label='Work Life Balance', options=['Good Balance', 'High Balance', 'Low Balance', 'Moderate Balance']) # categorical
capital_gain = st.number_input(label="capital gain",min_value=1 , max_value=99999)
capital_loss = st.number_input(label="capital loss",min_value=1 , max_value=4356)
income_per_hr =st.number_input(label="income per hour",min_value=1 , max_value=11365)



is_submit = st.button("Submit") # True / False
if is_submit:
    print(f"gender: {gender}")
    print(f"age: {age}")
    print(f"Edu_lvl: {Edu_lvl}")
    print(f"Occupation: {Occupation}")
    print(f"marital_status: {marital_status}")
    print(f"work_lb: {work_lb}")
    print(f"capital_gain: {capital_gain}")
    print(f"capital_loss: {capital_loss}")
    print(f"income_per_hr: {income_per_hr}")
