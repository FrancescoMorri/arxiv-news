import arxiv
import streamlit as st


options = ['cs.AI','cs.GT', 'cs.CY', 'cs.LG','cs.CE', 'cs.MA', 'econ.TH', 'cond-mat.dis-nn', 'cond-mat.stat-mech', 'q-fin.CP', 'stat.ML']

def special_func(l):
    dic = {
       'cs.AI':'Artificial Intelligence',
       'cs.GT':'Game Theory',
       'cs.LG':'Machine Learning',
       'cs.CE':'Comp. Engineering, Finance, Science',
       'cs.CY':'Computers and Society',
       'cs.MA':'Multiagent Systems',
       'econ.TH':'Economic Theory',
       'cond-mat.dis-nn':'Disordered Systems and Neural Networks',
       'cond-mat.stat-mech':'Statistical Mechanics',
       'q-fin.CP':'Computational Finance',
       'stat.ML':'Statistical Machine Learning'
    }
    return dic[l]

def encode_query(data):
    out = ''
    for i,d in enumerate(data):
        if i == len(data)-1:
            out += 'cat:'
            out += d
        else:
            out += 'cat:'
            out += d
            out += ' OR '
    
    
    return out


st.set_page_config(page_title="Arxiv Personal News", page_icon="black_joker", initial_sidebar_state="auto", layout='wide')

st.title("Arxiv multiple domain catchup")

with st.form('A'):
    selections = st.multiselect("Categories", options, default=None, format_func=special_func, key=None,
                   help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible",
                   max_selections=None)
    tmp = 'cat$:$cs.AI OR cat$:$cs.CE'
    manual_selections = st.text_input(label=f"If you want some different categories, add them here, following the syntax: '_{tmp}_'")
    max_search = st.slider(label='Number of papers', min_value=1, max_value=100, value=25)
    abs_check = st.checkbox(label='With abstract')

    print_out = st.form_submit_button("Search!")

if print_out:
    
    search = arxiv.Search(
      query = encode_query(selections)+' '+manual_selections,
      max_results = max_search,
      sort_by = arxiv.SortCriterion.SubmittedDate
    )

    date_titles = {}

    for result in search.results():
        date = result.published.strftime('%Y-%m-%d')
        if date in date_titles.keys():
            date_titles[date].append({'title':result.title, 'abs':result.summary, 'main_cat':result.primary_category, 'link':result.entry_id})
        else:
            date_titles[date] = [{'title':result.title, 'abs':result.summary, 'main_cat':result.primary_category, 'link':result.entry_id}]
    
    for k in date_titles.keys():
        st.header(k)
        cols = st.columns(spec=2, gap='small')
        for i,el in enumerate(date_titles[k]):
            with cols[i%(len(cols))]:
                tmp = el['link']
                link = f':blue[{tmp}]'
                tmp = el['main_cat']
                cat = f' (:red[_{tmp}_]) '
                st.subheader(el['title'] + cat + link)
                if abs_check:
                    st.write(el['abs'])

