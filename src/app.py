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

    st.set_page_config(page_title="Streamlit | readme-ai", layout="wide")

    st.title(":rainbow[README-AI]")
    title_text = """:blue[🚀 Generate beautiful README.md files for your coding projects! Powered by OpenAI's GPT language model APIs 💫]"""
    st.markdown(title_text)

    generate_readme = False

    # Sidebar for user inputs
    with st.sidebar:
        st.header(":blue[Configure] :rainbow[README-AI]")
        api_key = st.text_input("OpenAI API Key:", type="password")
        output_path = st.text_input("Output Path:", "readme-ai.md")
        repository_url = st.text_input("Repository Source:", "")

        if st.button("**:blue[Run] :rainbow[README-AI]**", key="sidebar_button"):
            generate_readme = True

    helper_text = output_path.lower()

    if generate_readme:
        st.header(":blue[Status]")

        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key

            command = ["readmeai"]
            if output_path:
                command.extend(["--output", output_path])
            if repository_url:
                command.extend(["--repository", repository_url])

            try:
                with st.spinner(
                    f"🤖 :blue[Processing repository] :green[:] {repository_url}"
                ):
                    subprocess.run(command, capture_output=True, check=True)

                st.success(
                    f"✅ :blue[Successfully generated file] :rainbow[:] {helper_text}"
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
                    f"An unexpected error occurred.\nError: {excinfo.stderr.decode()}"
                )

    # If README has been generated, display the download button and content
    if st.session_state.readme_generated:
        st.markdown("### :blue[Output File]")

        col1, col2 = st.columns([1, 0.1], gap="small")

        with col1:
            st.download_button(
                label=f"**Download File -** :blue[{helper_text}]",
                data=st.session_state.readme_content,
                file_name=output_path,
                mime="text/markdown",
            )

        with col2:
            if st.button("**Reset Session**"):
                # Reset session state variables and reload the page
                st.session_state.readme_generated = False
                st.session_state.readme_content = ""
                st.experimental_rerun()

        # Expander for raw code
        with st.expander(f"**View File - :blue[{helper_text}]**"):
            st.markdown(
                "**📋 Click icon in the top right corner to copy Markdown code.**"
            )
            st.code(
                st.session_state.readme_content, language="markdown", line_numbers=True
            )


if __name__ == "__main__":
    main()
