import streamlit as st
import subprocess

from readmeai import *


def run_pypi_cli_tool(api_key, output_path, repository_path, template=None, language=None):
    command = [
        "readmeai",
        "-k", api_key,
        "-o", output_path,
        "-r", repository_path,
    ]
    
    # Add optional arguments if provided
    if template:
        command.extend(["-t", template])
    if language:
        command.extend(["-l", language])

    # Run the PyPI CLI tool using subprocess
    try:
        subprocess.run(command, check=True)
        st.success("PyPI CLI tool executed successfully!")
    except subprocess.CalledProcessError as e:
        st.error(f"Error running the PyPI CLI tool: {e}")


def main():
    st.title("PyPI CLI Tool Runner")
    st.write("Enter the arguments for your PyPI CLI tool and click the 'Run' button.")

    # Gather user input using Streamlit widgets
    api_key = st.text_input("API Key:")
    output_path = st.text_input("Output Path:")
    repository_path = st.text_input("Repository Path:")
    template = st.text_input("Template (optional):")
    language = st.text_input("Language (optional):")

    if st.button("Run"):
        run_pypi_cli_tool(api_key, output_path, repository_path, template, language)


if __name__ == "__main__":
    main()
