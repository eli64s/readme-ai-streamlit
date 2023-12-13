"""Streamlit application serving the readme-ai package."""

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
        st.header("Configuration")
        api_key = st.text_input("OpenAI API Key", type="password")
        repo_path = st.text_input("Repository Path", "")
        output_path = st.text_input("Output Path", "readmeai.md")

        badge_style = st.selectbox(
            "Badge Style",
            [
                "flat",
                "flat-square",
                "plastic",
                "for-the-badge",
                "social",
                "apps",
                "apps-light",
            ],
            index=0,  # default selection (flat)
            help="Select badge style for the output file.",
        )

        use_emojis = st.checkbox(
            "Use Emojis",
            value=True,  # default checked
            help="Include emojis in the README file.",
        )

        run_offline = st.checkbox(
            "Run Offline",
            value=False,  # default unchecked
            help="Run README-AI without an API key.",
        )

        generate_readme = st.button("Run", key="sidebar_button")
        reset_session = st.button("Clear")

        if reset_session:
            st.session_state.readme_generated = False
            st.session_state.readme_content = ""
            st.experimental_rerun()

        st.markdown(
            """
            ## Resources
            - [GitHub](https://github.com/eli64s/readme-ai)
            - [PyPI](https://pypi.org/project/readmeai/)
            - [Docker Hub](https://hub.docker.com/r/zeroxeli/readme-ai)
            """,
            unsafe_allow_html=True,
        )

    return (
        api_key,
        output_path,
        repo_path,
        badge_style,
        use_emojis,
        run_offline,
        generate_readme,
    )


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
                    "Logging README-AI execution",
                    value=stderr_accumulated,
                    height=250,
                )
            if process.poll() is not None:
                break


def display_readme_output(output_path):
    """Display the generated README content and provide a download link."""
    st.markdown("### Output")
    with st.expander("Preview File"):
        st.markdown(st.session_state.readme_content, unsafe_allow_html=True)
    with st.expander("Download File"):
        st.download_button(
            label="Download README",
            data=st.session_state.readme_content,
            file_name=output_path,
            mime="text/markdown",
        )
    with st.expander("Copy Markdown"):
        st.code(st.session_state.readme_content, language="markdown")


def main():
    init_session_state()
    st.set_page_config(page_title="README-AI", layout="centered")
    st.title("README-AI")
    st.markdown("🚀 Automated README generation from the terminal, powered by GPT 🪐")

    (
        api_key,
        output_path,
        repo_path,
        badge_style,
        use_emojis,
        run_offline,
        generate_readme,
    ) = get_user_inputs()

    if generate_readme:
        command = ["readmeai", "--output", output_path, "--repository", repo_path]

        # Include conditions and additional flags based on new inputs
        if not run_offline:
            os.environ["OPENAI_API_KEY"] = api_key

        command.extend(["--badges", badge_style])
        command.extend(["--emojis", str(use_emojis).lower()])
        command.extend(["--offline", str(run_offline).lower()])

        try:
            execute_command(command, repo_path)
            st.success(f"README generated successfully - {output_path}")
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
