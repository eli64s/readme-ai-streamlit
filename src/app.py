"""Streamlit web app serving the Python package CLI readmeai."""

import logging
import subprocess
import tempfile
from typing import List

import streamlit as st

from src.cli import app_settings, build_command

logging.basicConfig(level=logging.INFO)


def init_session_state() -> None:
    """Initialize session state variables if they don't exist."""
    if "readme_generated" not in st.session_state:
        st.session_state.readme_generated = False
    if "readme_content" not in st.session_state:
        st.session_state.readme_content = ""


def execute_command(command: List[str], path: str) -> None:
    """Execute the command and handle its output."""
    with st.spinner(f"Processing repository @ {path}"):
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
                    "Logging output of readme-ai",
                    value=stderr_accumulated,
                    height=150,
                )
            if process.poll() is not None:
                break


def main(output_path: str) -> None:
    """Main function for the Streamlit web app for README-AI."""
    st.set_page_config(
        page_title="README-AI",
        page_icon="🏎💨",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.title(":rainbow[README-AI]")
    st.markdown("🎈 Automated README file generator, powered by AI.")

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
    ) = app_settings()

    if generate_readme:
        command = build_command(
            repo_path,
            output_path,
            api_key,
            use_emojis,
            badge_style,
            project_logo,
            header_alignment,
            max_tokens,
            model,
            run_offline,
        )
        try:
            execute_command(command, output_path)

            st.success("✅ README generation complete.")

            with open(output_path, "r") as file:
                readme_content = file.read()

            st.session_state.readme_generated = True
            st.session_state.readme_content = readme_content

            if st.session_state.readme_generated:
                with st.expander("Preview File"):
                    with open(output_path, "r") as file:
                        readme_content = file.read()
                        st.markdown(readme_content, unsafe_allow_html=True)

                    st.session_state.readme_generated = True
                    st.session_state.readme_content = readme_content

                with st.expander("Download File"):
                    with open(output_path, "rb") as file:
                        st.download_button(
                            label="Download :blue[README-AI.md]",
                            data=file,
                            file_name="README-AI.md",
                            mime="text/markdown",
                        )

                with st.expander("Copy Markdown"):
                    st.write("Copy the markdown below to your clipboard.")
                    st.code(st.session_state.readme_content, language="markdown")

        except (Exception, subprocess.CalledProcessError) as exc:
            logging.error(f"An error occurred: {exc}")
            st.error(f"❌ README generation failed.\nError: {str(exc)}")


if __name__ == "__main__":
    with tempfile.NamedTemporaryFile(suffix=".md", mode="w+", delete=False) as tmpfile:
        main(tmpfile.name)
