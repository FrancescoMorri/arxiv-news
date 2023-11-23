import arxiv
import streamlit as st
import json

full_taxonomy = [
        "astro-ph.CO",
        "astro-ph.EP",
        "astro-ph.GA",
        "astro-ph.HE",
        "astro-ph.IM",
        "astro-ph.SR",
        "cond-mat.dis-nn",
        "cond-mat.mes-hall",
        "cond-mat.mtrl-sci",
        "cond-mat.other",
        "cond-mat.quant-gas",
        "cond-mat.soft",
        "cond-mat.stat-mech",
        "cond-mat.str-el",
        "cond-mat.supr-con",
        "cs.AI",
        "cs.AR",
        "cs.CC",
        "cs.CE",
        "cs.CG",
        "cs.CL",
        "cs.CR",
        "cs.CV",
        "cs.CY",
        "cs.DB",
        "cs.DC",
        "cs.DL",
        "cs.DM",
        "cs.DS",
        "cs.ET",
        "cs.FL",
        "cs.GL",
        "cs.GR",
        "cs.GT",
        "cs.HC",
        "cs.IR",
        "cs.IT",
        "cs.LG",
        "cs.LO",
        "cs.MA",
        "cs.MM",
        "cs.MS",
        "cs.NA",
        "cs.NE",
        "cs.NI",
        "cs.OH",
        "cs.OS",
        "cs.PF",
        "cs.PL",
        "cs.RO",
        "cs.SC",
        "cs.SD",
        "cs.SE",
        "cs.SI",
        "cs.SY",
        "econ.EM",
        "econ.GN",
        "econ.TH",
        "eess.AS",
        "eess.IV",
        "eess.SP",
        "eess.SY",
        "gr-qc",
        "hep-ex",
        "hep-lat",
        "hep-ph",
        "hep-th",
        "math-ph",
        "math.AC",
        "math.AG",
        "math.AP",
        "math.AT",
        "math.CA",
        "math.CO",
        "math.CT",
        "math.CV",
        "math.DG",
        "math.DS",
        "math.FA",
        "math.GM",
        "math.GN",
        "math.GR",
        "math.GT",
        "math.HO",
        "math.IT",
        "math.KT",
        "math.LO",
        "math.MG",
        "math.MP",
        "math.NA",
        "math.NT",
        "math.OA",
        "math.OC",
        "math.PR",
        "math.QA",
        "math.RA",
        "math.RT",
        "math.SG",
        "math.SP",
        "math.ST",
        "nlin.AO",
        "nlin.CD",
        "nlin.CG",
        "nlin.PS",
        "nlin.SI",
        "nucl-ex",
        "nucl-th",
        "physics.acc-ph",
        "physics.ao-ph",
        "physics.app-ph",
        "physics.atm-clus",
        "physics.atom-ph",
        "physics.bio-ph",
        "physics.chem-ph",
        "physics.class-ph",
        "physics.comp-ph",
        "physics.data-an",
        "physics.ed-ph",
        "physics.flu-dyn",
        "physics.gen-ph",
        "physics.geo-ph",
        "physics.hist-ph",
        "physics.ins-det",
        "physics.med-ph",
        "physics.optics",
        "physics.plasm-ph",
        "physics.pop-ph",
        "physics.soc-ph",
        "physics.space-ph",
        "q-bio.BM",
        "q-bio.CB",
        "q-bio.GN",
        "q-bio.MN",
        "q-bio.NC",
        "q-bio.OT",
        "q-bio.PE",
        "q-bio.QM",
        "q-bio.SC",
        "q-bio.TO",
        "q-fin.CP",
        "q-fin.EC",
        "q-fin.GN",
        "q-fin.MF",
        "q-fin.PM",
        "q-fin.PR",
        "q-fin.RM",
        "q-fin.ST",
        "q-fin.TR",
        "quant-ph",
        "stat.AP",
        "stat.CO",
        "stat.ME",
        "stat.ML",
        "stat.OT",
        "stat.TH"
      ]


def special_func(l):
    dic = {
        'cs.GT':'Game Theory',
        'cs.MA':'Multiagent Systems',
        'cs.CE':'Comp. Engineering, Finance, Science',
        'cs.AI':'Artificial Intelligence',
        'cs.LG':'Machine Learning',
        'cs.CY':'Computers and Society',
        'econ.TH':'Economic Theory',
        'cond-mat.dis-nn':'Disordered Systems and Neural Networks',
        'cond-mat.stat-mech':'Statistical Mechanics',
        'q-fin.CP':'Computational Finance',
        'stat.ML':'Statistical Machine Learning'
    }
    return dic[l]

def get_category_display(category):
    full_categories = json.load(open("arxiv_taxonomy.json"))
    return full_categories[category]['category_name']

def get_specifics_categories(id, not_present=False):
    if not_present:
        return [k for k in full_taxonomy if id not in k]
    else:
        tmp = []
        for k in full_taxonomy:
            identifier = k.split('.')[0]
            if id == identifier:
                tmp.append(k)
        return tmp

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
selections = []

with st.form('A'):
    st.subheader("Select between :blue[Computer Science] (**cs**) categories")
    tmp = st.multiselect("**cs**", get_specifics_categories('cs'), default=None, format_func=get_category_display, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, max_selections=None)
    selections.extend(tmp)

    st.subheader("Select between :blue[Economics] (**econ**) categories")
    tmp = st.multiselect("**econ**", get_specifics_categories('econ'), default=None, format_func=get_category_display, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, max_selections=None)
    selections.extend(tmp)

    st.subheader("Select between :blue[Electrical Engineering and System Science] (**eess**) categories")
    tmp = st.multiselect("**eess**", get_specifics_categories('eess'), default=None, format_func=get_category_display, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, max_selections=None)
    selections.extend(tmp)

    st.subheader("Select between :blue[Mathematics] (**math**) categories")
    tmp = st.multiselect("**math**", get_specifics_categories('math'), default=None, format_func=get_category_display, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, max_selections=None)
    selections.extend(tmp)

    st.subheader("Select between :blue[Physics] (**physics**) categories")
    tmp = st.multiselect("**physics**", get_specifics_categories('physics'), default=None, format_func=get_category_display, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, max_selections=None)
    selections.extend(tmp)

    st.subheader("Select between :blue[Astro-Physics] (**astro-ph**) categories")
    tmp = st.multiselect("**astro-ph**", get_specifics_categories('astro-ph'), default=None, format_func=get_category_display, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False,  max_selections=None)
    selections.extend(tmp)

    st.subheader("Select between :blue[Condensed Matter] (**cond-mat**) categories")
    tmp = st.multiselect("**cond-mat**", get_specifics_categories('cond-mat'), default=None, format_func=get_category_display, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False,  max_selections=None)
    selections.extend(tmp)

    st.subheader("Select between :blue[other Physics Domains]")
    tmp = st.multiselect("", get_specifics_categories('.', not_present=True), default=None, format_func=get_category_display, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False,  max_selections=None)
    selections.extend(tmp)

    st.subheader("Select between :blue[Non-Linear Sciences] (**nlin**) categories")
    tmp = st.multiselect("**nlin**", get_specifics_categories('nlin'), default=None, format_func=get_category_display, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False,  max_selections=None)
    selections.extend(tmp)

    st.subheader("Select between :blue[Quantitative Biology] (**q-bio**) categories")
    tmp = st.multiselect("**q-bio**", get_specifics_categories('q-bio'), default=None, format_func=get_category_display, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False,  max_selections=None)
    selections.extend(tmp)

    st.subheader("Select between :blue[Statistics] (**stat**) categories")
    tmp = st.multiselect("**stat**", get_specifics_categories('stat'), default=None, format_func=get_category_display, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, max_selections=None)
    selections.extend(tmp)

    
    
    max_search = st.slider(label='Number of papers', min_value=10, max_value=150, value=25)
    abs_check = st.checkbox(label='With abstract')
    print_out = st.form_submit_button("Search!")

if print_out:
    search = arxiv.Search(
      query=encode_query(selections),
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

