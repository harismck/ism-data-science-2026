import streamlit as st
import duckdb
import plotly.express as px

st.set_page_config(
    layout="wide",
    page_title="Vehicle Inspection Analysis",
    page_icon="🚗",
)


@st.cache_data
def load_data():
    conn = duckdb.connect()
    conn.execute("ATTACH 'data.duckdb' AS data (READ_ONLY)")
    conn.execute("USE data.vehicle_inspection")

    return conn.sql(
        """
        SELECT
            vehicle_identifier,
            fuel_type,
            body_type,
            inspection_station_code,
            inspection_station_municipality,
            CAST(inspection_passed AS BOOLEAN) AS inspection_passed,
            CAST(inspection_date_week AS DATE) AS inspection_date_week,
            date_trunc('month', CAST(inspection_date_week AS DATE)) AS inspection_month,
            date_trunc('year', CAST(inspection_date_week AS DATE)) AS inspection_year,
            CASE
                WHEN year(CAST(inspection_date_week AS DATE)) - CAST(manufacture_year AS INTEGER) BETWEEN 0 AND 100
                THEN year(CAST(inspection_date_week AS DATE)) - CAST(manufacture_year AS INTEGER)
            END AS vehicle_age
        FROM inspection
        WHERE class = 'M1'
        AND inspection_type_en = 'Technical inspection'
        AND CAST(inspection_date_week AS DATE) > DATE '2019-05-01'
        AND inspection_passed IS NOT NULL
        """
    ).df()


df = load_data()


municipality_options = sorted(df["inspection_station_municipality"].unique())
min_inspection_date = df["inspection_date_week"].min().date()
max_inspection_date = df["inspection_date_week"].max().date()


with st.sidebar:
    st.title("Lithuanian Vehicle Inspection Analysis")
    st.markdown(
        "This dashboard analyzes Lithuanian technical inspections for M1 passenger vehicles. "
        "The data is filtered to regular technical inspections after 2019-05-01."
    )
    st.divider()
    st.markdown("### Filters")
    selected_municipalities = st.multiselect(
        "Municipality",
        options=municipality_options,
    )
    date_from = st.date_input(
        "Date from",
        value=min_inspection_date,
        min_value=min_inspection_date,
        max_value=max_inspection_date,
    )
    date_to = st.date_input(
        "Date to",
        value=max_inspection_date,
        min_value=min_inspection_date,
        max_value=max_inspection_date,
    )

    st.divider()
    with st.form("feedback_form"):
        rating = st.slider("Rating", 1, 5, 3)
        feedback = st.text_area("Feedback")
        submit_btn = st.form_submit_button("Submit")

    if submit_btn:
        st.markdown("Rating:", rating)
        st.markdown("Feedback:", feedback)

df = df[df["inspection_date_week"].dt.date.between(date_from, date_to)]
if selected_municipalities:
    df = df[df["inspection_station_municipality"].isin(selected_municipalities)]


tab1, tab2, tab3 = st.tabs(["Main Dashboard", "Pass Rate Analysis", "Other"])

with tab1:
    inspections = len(df)
    pass_rate = df["inspection_passed"].mean()
    inspection_points = df["inspection_station_code"].nunique()
    vehicles = df["vehicle_identifier"].nunique()

    metric_cols = st.columns(4)
    with metric_cols[0]:
        st.metric("Inspections", f"{inspections:,.0f}")
    with metric_cols[1]:
        st.metric("Pass Rate", f"{pass_rate:.1%}")
    with metric_cols[2]:
        st.metric("Inspection Points", f"{inspection_points:,.0f}")
    with metric_cols[3]:
        st.metric("Vehicles", f"{vehicles:,.0f}")

    date_column = st.segmented_control(
        "Aggregation",
        options=["inspection_month", "inspection_year"],
        default="inspection_month",
    )

    st.divider()

    aggregated = (
        df.groupby(date_column)
        .agg(
            inspections=("vehicle_identifier", "size"),
            pass_rate=("inspection_passed", "mean"),
        )
        .reset_index()
    )
    chart_cols = st.columns(2)
    with chart_cols[0]:
        fig = px.bar(
            aggregated,
            x=date_column,
            y="inspections",
            title="Inspections Over Time",
        )
        st.plotly_chart(fig)

    with chart_cols[1]:
        fig = px.line(
            aggregated,
            x=date_column,
            y="pass_rate",
            title="Pass Rate Over Time",
        )
        st.plotly_chart(fig)

    st.divider()

    with st.expander("See dataset"):
        st.dataframe(
            df.sample(20),
        )

with tab2:

    '''
    TASK 1

    Add a st.selectbox with options fuel_type, inspection_station_municipality and body_type

    Implement two barcharts:
    1. inspection pass rate by selected categorical variable
    2. number of inspections by selected categorical variable

    put the charts side-by-side using st.columns

    useful:
    - selectbox documentation: https://docs.streamlit.io/develop/api-reference/widgets/st.selectbox

    '''
    pass

with tab3:
    '''
    TASK 2
    
    Choose an input from Streamlit documentation: https://docs.streamlit.io/develop/api-reference/widgets

    Implement a chart that uses the input (does not have to be a filter - could for instance change a chart parameter).

    '''
    pass
