"""Streamlit web app serving the Python package CLI readmeai."""

import logging
import os
import subprocess
from typing import Tuple

import streamlit as st

from utils import get_readme_tempfile


logging.basicConfig(level=logging.INFO)


def init_session_state() -> None:
    """Initialize session state variables if they don't exist."""
    if "readme_generated" not in st.session_state:
        st.session_state.readme_generated = False
    if "readme_content" not in st.session_state:
        st.session_state.readme_content = ""


def get_user_inputs() -> Tuple:
    """Collect user inputs from the sidebar."""
    with st.sidebar:
        st.header("README Settings")

        api_key = st.text_input("OpenAI API Key", type="password")

        repo_path = st.text_input("Repository Path", "")

        badge_style = st.selectbox(
            "Badge Style",
            [
                "default",
                "flat",
                "flat-square",
                "plastic",
                "for-the-badge",
                "skills",
                "skills-light",
                "social",
            ],
            index=0,
            help="Select badge style for the output file.",
        )
        use_emojis = st.checkbox(
            "Use Emojis",
            value=False,
            help="Include emojis in the README file.",
        )
        run_offline = st.checkbox(
            "Offline Mode",
            value=False,
            help="Run README-AI without an API key.",
        )
        header_alignment = st.selectbox(
            "Header Alignment",
            ["center", "left"],
            index=0,
            help="Set header text alignment in the README file.",
        )
        project_logo = st.selectbox(
            "Project Logo",
            ["BLACK", "BLUE", "CLOUD", "PURPLE", "YELLOW"],
            index=0,
            help="URL or path to the project logo image for the README header.",
        )
        max_tokens = st.number_input("Max Tokens", min_value=1, value=3899, step=1)
        model = st.selectbox(
            "GPT Model",
            ["gpt-3.5-turbo", "gpt-4", "gpt-4-1106-preview"],
            index=0,
        )
        temperature = st.slider("Temperature", 0.0, 2.0, 0.1)

        # template = st.text_input("Template", "")
        # language = st.selectbox(
        #    "Language",
        #   ["English (en)", "other-languages"],
        #    index=0,
        # )

        generate_readme = st.button("Run", key="sidebar_button")
        reset_session = st.button("Clear")

        if reset_session:
            st.session_state.readme_generated = False
            st.session_state.readme_content = ""
            st.experimental_rerun()

        st.markdown(
            """
            ## 🔗 :blue[Resources]
            - [Readme-ai @ PyPI](https://pypi.org/project/readmeai/)
            - [Readme-ai @ GitHub](https://github.com/eli64s/readme-ai)
            - [Readme-ai @ Docker Hub](https://hub.docker.com/r/zeroxeli/readme-ai)
            """,
            unsafe_allow_html=True,
        )

    return (
        api_key,
        header_alignment,
        project_logo,
        repo_path,
        badge_style,
        use_emojis,
        run_offline,
        generate_readme,
        max_tokens,
        model,
        temperature,
        # template,
        # language,
    )


def execute_command(
    command: list, path: str, use_emojis: bool, run_offline: bool
) -> None:
    """Execute the command and handle its output."""
    with st.spinner(f"Processing repository - {path}"):
        if use_emojis:
            command.append("--emojis")
        if run_offline:
            command.append("--offline")

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


def display_readme_output(output_path: str) -> None:
    """Display the README output."""
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


def display_readme_output(output_path: str) -> None:
    """Display the README output."""
    st.markdown("### Output")

    with st.expander("Preview File"):
        with open(output_path, "r") as file:
            readme_content = file.read()
        st.markdown(readme_content, unsafe_allow_html=True)

    with st.expander("Download File"):
        with open(output_path, "rb") as file:
            st.download_button(
                label="Download README",
                data=file,
                file_name=os.path.basename(output_path),
                mime="text/markdown",
            )

    with st.expander("Copy Markdown"):
        st.code(readme_content, language="markdown")


def main(output_path: str = "README-AI.md") -> None:
    """Main function for the Streamlit web app for README-AI."""
    st.set_page_config(
        page_title="README-AI",
        page_icon=":robot_face:",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.title(":blue[README-AI]")
    st.markdown(
        """🎈 Automated README file generator, powered by GPT language model APIs."""
    )

    init_session_state()
    (
        api_key,
        header_alignment,
        project_logo,
        repo_path,
        badge_style,
        use_emojis,
        run_offline,
        generate_readme,
        max_tokens,
        model,
        temperature,
        # template,
        # language,
    ) = get_user_inputs()

    if generate_readme:
        command = ["readmeai", "--repository", repo_path]

        if not run_offline:
            os.environ["OPENAI_API_KEY"] = api_key

        command.extend(["--badges", badge_style])
        command.extend(["--image", project_logo])
        command.extend(["--align", header_alignment])
        command.extend(["--max-tokens", str(max_tokens)])
        command.extend(["--model", model])
        command.extend(["--temperature", str(temperature)])

        # if template:
        #    command.extend(["--template", template])
        # command.extend(["--language", language])

        try:
            execute_command(command, repo_path, use_emojis, run_offline)

            st.success(f"README generated successfully - {output_path}")

            if os.path.exists(output_path):
                with open(output_path, "r") as file:
                    readme_content = file.read()

                st.session_state.readme_generated = True
                st.session_state.readme_content = readme_content

        except subprocess.CalledProcessError as exc:
            logging.error(f"Subprocess error occurred: {exc}")
            st.error(f"❌ README generation failed.\nError: {str(exc)}")

        except Exception as exc:
            logging.error(f"An unexpected error occurred: {exc}")
            st.error(f"❌ README generation failed.\nError: {str(exc)}")

    if st.session_state.readme_generated:
        temp_readme_path = get_readme_tempfile(st.session_state.readme_content)
        display_readme_output(temp_readme_path)


if __name__ == "__main__":
    main()
