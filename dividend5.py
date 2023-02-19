# here I set different widths to each column,
# meaning the first is 1 width and the second 3,
# i.e. 1/(1+3) = 25% and 3 / (1+4) = 75%
overview_columns = st.columns([1, 3])

# first column, basic information

# The <br/> tag in html simple adds a linebreak.
# I add 4 of those to lower the text to become more
# vertically aligned
overview_columns[0].markdown("<br/>"*4, unsafe_allow_html=True)
# text will be displayed and key is the key in info
for text, key in [
    ("Current price", "price"),
    ("Country", "country"),
    ("Exchange", "exchange"),
    ("Sector", "sector"),
    ("Industry", "industry"),
    ("Full time employees", "fullTimeEmployees")
]:
    overview_columns[0].markdown("")
    overview_columns[0].markdown(f"- {text}: **{info[key]}**")
