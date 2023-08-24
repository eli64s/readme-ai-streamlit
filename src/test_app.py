import streamlit as st
import snowflake.connector
import pandas as pd

# Function to query Snowflake
def run_snowflake_query(query):
    # Connect to Snowflake
    con = snowflake.connector.connect(
        user='YOUR_USER',
        password='YOUR_PASSWORD',
        account='YOUR_ACCOUNT',
        warehouse='YOUR_WAREHOUSE',
        database='YOUR_DATABASE',
        schema='YOUR_SCHEMA'
    )
    
    # Execute the query
    cur = con.cursor()
    cur.execute(query)
    result = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    
    # Convert the result to a pandas dataframe
    df = pd.DataFrame(result, columns=columns)
    
    # Close the connection
    cur.close()
    con.close()
    
    return df

# Streamlit UI
st.title('Enhanced Snowflake Query Runner')

# Styling
st.markdown("""
<style>
    .reportview-container {
        flex-direction: column;
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100%;
    }
    .main {
        flex: 1;
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>
""", unsafe_allow_html=True)

# Create a text area for the user's SQL query
query = st.text_area('Enter your SQL query:', height=150)

# When the user clicks the 'Search' button, run the query
if st.button('Execute'):
    if query:
        try:
            results = run_snowflake_query(query)
            st.write('Results:')
            st.dataframe(results)
        except Exception as e:
            st.error(f'Error executing the query: {e}')
    else:
        st.warning('Please enter a valid SQL query.')

