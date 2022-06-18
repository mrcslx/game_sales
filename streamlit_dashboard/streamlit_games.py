
# TO RUN THE APP:
#	* open terminal
#	* navigate to streamlit file location
#	* use command: "streamlit run streamlit_games.py"


# import libraries
import pandas as pd
import streamlit as st
import plotly.express as px


# customise app
st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 90%;
        padding-top: 5rem;
        padding-right: 5rem;
        padding-left: 5rem;
        padding-bottom: 5rem;
    }}
    img{{
    	max-width:40%;
    	margin-bottom:40px;
    }}
</style>
""",
        unsafe_allow_html=True,
    )


# define containers
header_container = st.container()
pc_data_container = st.container()
ps4_data_container = st.container()
xbox_data_container = st.container()


# header container contents
with header_container:

	st.title("Explore Global Game Sales by Platform and Genre")
	st.write("The three plots below will allow you to view global sales by year and game genre for the following platforms: PC, PS4 and Xbox One")
	st.write("Note: The plots are interactive, click/double-click to select specific game genres")


# PC container contents
with pc_data_container:

    pc = pd.read_csv('sales-pc.csv')

    sales_year_genre_pc = pc.groupby(['year', 'genre']).agg(
    sales=pd.NamedAgg(column='global_sales', aggfunc=sum)
    ).reset_index().copy()

    fig1 = px.line(sales_year_genre_pc, x="year", y="sales", color="genre", line_shape="spline",
             labels={
                 "year": "Year",
                 "sales": "Global Sales (millions)",
                 "genre": "Game Genre"
             },
             title="Global Sales by Year and Genre - PC Games")
    fig1.update_xaxes(tickangle=45)
    fig1.update_layout(width=1100, height=600)

    st.write(fig1)

    pc_genre_list = pc['genre'].unique().tolist()

    s_pc_genre = st.selectbox('Which game genre would you like to explore?', pc_genre_list, key='genre')

    genre_pc = pc.loc[pc["genre"] == s_pc_genre]

    genre_pc_mean_sales = genre_pc.groupby("publisher")["global_sales"].mean().sort_values(ascending = False).head(5).reset_index(name = "mean global sales")

    fig4 = px.bar(genre_pc_mean_sales, x="publisher", y="mean global sales",
             labels={
                 "publisher": "Publisher",
                 "mean global sales": "Mean Global Sales (millions)"
             },
             title="Mean Global Sales by Publisher and Chosen Game Genre (PC)")
    fig4.update_xaxes(tickangle=45)
    fig4.update_layout(width=1100, height=600)

    st.write(fig4)


# PS4 container contents
with ps4_data_container:

    ps4 = pd.read_csv('sales-ps4.csv')

    sales_year_genre_ps4 = ps4.groupby(['year', 'genre']).agg(
    sales=pd.NamedAgg(column='global_sales', aggfunc=sum)
    ).reset_index().copy()

    fig2 = px.line(sales_year_genre_ps4, x="year", y="sales", color="genre", line_shape="spline",
             labels={
                 "year": "Year",
                 "sales": "Global Sales (millions)",
                 "genre": "Game Genre"
             },
             title="Global Sales by Year and Genre - PS4 Games")
    fig2.update_xaxes(tickangle=45)
    fig2.update_layout(width=1100, height=600)

    st.write(fig2)


# Xbox container contents
with xbox_data_container:

    xbox = pd.read_csv('sales-xbox.csv')

    sales_year_genre_xbox = xbox.groupby(['year', 'genre']).agg(
    sales=pd.NamedAgg(column='global_sales', aggfunc=sum)
    ).reset_index().copy()

    fig3 = px.line(sales_year_genre_xbox, x="year", y="sales", color="genre", line_shape="spline",
             labels={
                 "year": "Year",
                 "sales": "Global Sales (millions)",
                 "genre": "Game Genre"
             },
             title="Global Sales by Year and Genre - Xbox One Games")
    fig3.update_xaxes(tickangle=45)
    fig3.update_layout(width=1100, height=600)

    st.write(fig3)
