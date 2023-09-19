"""Streamlit app for README-AI."""

import logging
import os
import subprocess

import streamlit as st

logging.basicConfig(level=logging.INFO)


def main():
    # Initialize session state variables if they don't exist
    if "readme_generated" not in st.session_state:
        st.session_state.readme_generated = False
    if "readme_content" not in st.session_state:
        st.session_state.readme_content = ""
    logging.basicConfig(level=logging.INFO)

    st.set_page_config(page_title="streamlit | readme-ai", layout="wide")

    st.title(":blue[README-AI]")
    title_text = f"""
    :blue[🚀 Generate beautiful README.md files for your coding projects! Powered by OpenAI's GPT language model APIs 💫]
    """
    st.markdown(title_text)

    generate_readme = False

    # Sidebar for user inputs
    with st.sidebar:
        st.header("**:rainbow[README-AI] :blue[Configuration]**")
        api_key = st.text_input("**‣ OpenAI API Key**", type="password")
        output_path = st.text_input("**‣ Output Path**", "readme-ai.md")
        repo_path = st.text_input("**‣ Repository**", "")

        if st.button("**:rainbow[Run README-AI]**", key="sidebar_button"):
            generate_readme = True
            
    readme_path = output_path.lower()

    if generate_readme:
        st.markdown("### :blue[Status]")

        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key

            command = ["readmeai"]
            if output_path:
                command.extend(["--output", output_path])
            if repo_path:
                command.extend(["--repository", repo_path])

            try:
                with st.spinner(f":blue[🗃 Processing repository -] {repo_path}"):
                    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    
                    output_container = st.empty()
                    stderr_accumulated = ''
                    
                    while True:
                        stderr_line = process.stderr.readline()
                        if stderr_line:
                            stderr_accumulated += stderr_line
                            output_container.text_area("README-AI Log", value=stderr_accumulated, height=200)
                        
                        if process.poll() is not None:
                            break

                st.success(
                    f":blue[✅ README file generated -] {readme_path}"
                )
 
                if os.path.exists(output_path):
                    with open(output_path, "r") as file:
                        readme_content = file.read()
                    st.session_state.readme_generated = True
                    st.session_state.readme_content = readme_content

            except subprocess.CalledProcessError as excinfo:
                logging.error(f"Subprocess Error: {excinfo}")
                st.error(
                    f"❌ README generation failed.\nError: {excinfo.stderr.decode()}"
                )
            except Exception as excinfo:
                logging.error(f"An unexpected error occurred: {excinfo}")
                st.error(
                    f"❌ README generation failed.\nError: {str(excinfo)}"
                )

    # Display download button and content if README is generated.
    if st.session_state.readme_generated:
        st.markdown("### :blue[README-AI Output]")
        
        col1, col2 = st.columns([1, 0.1], gap="small")
        with col1:
            st.download_button(
                label=f"**Download File - :blue[{readme_path}]**",
                data=st.session_state.readme_content,
                file_name=output_path,
                mime="text/markdown",
                use_container_width=True,
            )
        with col2:
            if st.button("**Reset Session**"):
                # Reset session state variables and reload the page
                st.session_state.readme_generated = False
                st.session_state.readme_content = ""
                st.experimental_rerun()

        tab1, tab2 = st.tabs(["📃 Copy README.md", "👀 Preview README.md"])
        tab1.markdown(f"#### :blue[Copy Markdown] - :rainbow[{readme_path}]")
        tab1.code(
                st.session_state.readme_content, language="markdown", line_numbers=True
            )
        tab2.markdown(f"#### :blue[Preview Markdown] - :rainbow[{readme_path}]")
        tab2.markdown(st.session_state.readme_content, unsafe_allow_html=True)


if __name__ == "__main__":
    main()