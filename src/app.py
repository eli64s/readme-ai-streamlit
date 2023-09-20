"""Streamlit app for README-AI."""

import logging
import os
import subprocess

import streamlit as st

logging.basicConfig(level=logging.INFO)


def init_session_state():
    """Initialize session state variables if they don't exist."""
    if "readme_generated" not in st.session_state:
        st.session_state.readme_generated = False
    if "readme_content" not in st.session_state:
        st.session_state.readme_content = ""


def get_user_inputs():
    """Collect user inputs from the sidebar."""
    with st.sidebar:
        st.header("**:rainbow[README-AI] Configuration**")
        api_key = st.text_input("**OpenAI API Key**", type="password")
        repo_path = st.text_input("**Repository**", "")

        col1, col2 = st.columns([1, 1])

        with col1:
            generate_readme = st.button("**:green[Run]**", key="sidebar_button",use_container_width=True)
        
        with col2:
            reset_session = st.button("**:red[Reset]**",use_container_width=True)
            if reset_session:
                st.session_state.readme_generated = False
                st.session_state.readme_content = ""
                st.experimental_rerun()
                

    return api_key, repo_path, generate_readme



def execute_command(command, path):
    """Execute the command and handle its output."""
    with st.spinner(f"Processing repository - {path}"):
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        output_container = st.empty()
        stderr_accumulated = ""

        while True:
            stderr_line = process.stderr.readline()
            if stderr_line:
                stderr_accumulated += stderr_line
                output_container.text_area(
                    ":rainbow[README-AI] Log:",
                    value=stderr_accumulated,
                    height=200,
                    max_chars=10000,
                )
            if process.poll() is not None:
                break


def display_readme_output(output_path):
    """Display the generated README content and provide a download link."""
    st.markdown("### *Output*")
    tab1, tab2, tab3 = st.tabs(["Preview File", "Download File", "Copy Markdown"])
    tab1.markdown(st.session_state.readme_content, unsafe_allow_html=True)
    tab2.download_button(
            label=f"**Download :rainbow[{output_path}]**",
            data=st.session_state.readme_content,
            file_name=output_path,
            mime="text/markdown",
        )
    tab3.code(st.session_state.readme_content, language="markdown", line_numbers=True)


def main():
    init_session_state()
    st.set_page_config(page_title="Streamlit | README-AI", layout="wide")
    st.title(":rainbow[README-AI]")
    title_text = (
        f"""\
        ‣ Generate beautiful README.md files for your coding projects!  
        ‣ Powered by OpenAI's GPT language model APIs 💫
        """
    )
    st.markdown(title_text)

    api_key, repo_path, generate_readme = get_user_inputs()
    output_path = "README-AI.md"

    if generate_readme and api_key:
        os.environ["OPENAI_API_KEY"] = api_key
        command = ["readmeai"]

        if repo_path:
            command.extend(["--repository", repo_path])

        try:
            execute_command(command, repo_path)
            st.success(f"README-AI execution completed successfully.")
            if os.path.exists(output_path):
                with open(output_path, "r") as file:
                    readme_content = file.read()
                st.session_state.readme_generated = True
                st.session_state.readme_content = readme_content

        except subprocess.CalledProcessError as excinfo:
            logging.error(f"Subprocess Error: {excinfo}")
            st.error(f"❌ README generation failed.\nError: {excinfo.stderr.decode()}")

        except Exception as excinfo:
            logging.error(f"An unexpected error occurred: {excinfo}")
            st.error(f"❌ README generation failed.\nError: {str(excinfo)}")

    if st.session_state.readme_generated:
        display_readme_output(output_path)


if __name__ == "__main__":
    main()
