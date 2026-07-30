import streamlit as st
import random
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="LSTTP - One Coin Toss Explorer",
    layout="wide"
)

# Session State
if "heads" not in st.session_state:
    st.session_state.heads = 0

if "tails" not in st.session_state:
    st.session_state.tails = 0

if "total" not in st.session_state:
    st.session_state.total = 0

if "history" not in st.session_state:
    st.session_state.history = []

# Header
st.title("🎲 LSTTP")
st.subheader("Learn Stats To The Point")
st.markdown("## One Coin Toss Explorer")

# Buttons
col1, col2, col3, col4 = st.columns(4)

def toss_coin(n):

    for _ in range(n):

        result = random.choice(["Head", "Tail"])

        st.session_state.total += 1

        if result == "Head":
            st.session_state.heads += 1
        else:
            st.session_state.tails += 1

        p_head = st.session_state.heads / st.session_state.total

        st.session_state.history.append(
            {
                "Toss": st.session_state.total,
                "P_Head": p_head
            }
        )

with col1:
    if st.button("Toss 1"):
        toss_coin(1)

with col2:
    if st.button("Toss 10"):
        toss_coin(10)

with col3:
    if st.button("Toss 100"):
        toss_coin(100)

with col4:
    if st.button("Reset"):

        st.session_state.heads = 0
        st.session_state.tails = 0
        st.session_state.total = 0
        st.session_state.history = []

# Statistics
st.markdown("---")

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("Total Tosses", st.session_state.total)
c2.metric("Heads", st.session_state.heads)
c3.metric("Tails", st.session_state.tails)

if st.session_state.total > 0:

    ph = st.session_state.heads / st.session_state.total
    pt = st.session_state.tails / st.session_state.total

else:
    ph = 0
    pt = 0

c4.metric("Experimental P(H)", f"{ph:.3f}")
c5.metric("Experimental P(T)", f"{pt:.3f}")

# Sample Space
st.markdown("---")

st.markdown("""
### Concept Panel

**Experiment:** Tossing a Coin

**Sample Space:** {H, T}

**P(H) = 0.5**

**P(T) = 0.5**
""")

# Charts
left, right = st.columns(2)

# Pie Chart
with left:

    pie_df = pd.DataFrame(
        {
            "Outcome": ["Head", "Tail"],
            "Probability": [50, 50]
        }
    )

    fig_pie = px.pie(
        pie_df,
        names="Outcome",
        values="Probability",
        title="Theoretical Probability"
    )

    st.plotly_chart(fig_pie, use_container_width=True)

# Bar Chart
with right:

    bar_df = pd.DataFrame(
        {
            "Outcome": ["Head", "Tail"],
            "Count": [
                st.session_state.heads,
                st.session_state.tails
            ]
        }
    )

    fig_bar = px.bar(
        bar_df,
        x="Outcome",
        y="Count",
        title="Observed Frequency"
    )

    st.plotly_chart(fig_bar, use_container_width=True)

# Convergence Graph
st.markdown("---")

history_df = pd.DataFrame(st.session_state.history)

fig = go.Figure()

if len(history_df) > 0:

    fig.add_trace(
        go.Scatter(
            x=history_df["Toss"],
            y=history_df["P_Head"],
            mode="lines",
            name="Experimental P(H)"
        )
    )

fig.add_hline(
    y=0.5,
    line_dash="dash",
    annotation_text="Theoretical P(H)=0.5"
)

fig.update_layout(
    title="Law of Large Numbers",
    xaxis_title="Number of Tosses",
    yaxis_title="Experimental Probability of Head"
)

st.plotly_chart(fig, use_container_width=True)

st.info(
    "Observe how the experimental probability approaches 0.5 as the number of tosses increases."
)
