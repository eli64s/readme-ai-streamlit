"""
Streamlit web app serving the readme-ai CLI Python package.
"""

import logging
import subprocess
import tempfile

import streamlit as st

from src.cli import app_settings
from src.commands import build_command, execute_command

logging.basicConfig(level=logging.INFO)


DESCRIPTION = "README file generator, powered by large language model APIs 👾"


def init_session_state() -> None:
    """
    Initialize session state variables if they don't exist.
    """
    if "readme_generated" not in st.session_state:
        st.session_state.readme_generated = False
    if "readme_content" not in st.session_state:
        st.session_state.readme_content = ""


def main():
    """
    Main function for the Streamlit web app for README-AI.
    """
    st.set_page_config(
        page_title="README-AI",
        page_icon="🏎💨",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.title(":rainbow[README-AI]")
    st.markdown(DESCRIPTION)

    init_session_state()

    (
        api_key,
        header_alignment,
        project_logo,
        repo_path,
        badge_style,
        use_emojis,
        generate_readme,
        context_window,
        model,
        temperature,
        api_service,
        header_style,
        toc_style,
        badge_color,
        tree_depth,
        llm_image,
    ) = app_settings()

    if generate_readme:
        with tempfile.NamedTemporaryFile(
            suffix=".md", mode="w+", delete=False
        ) as tmpfile:
            output_path = tmpfile.name

            command = build_command(
                repo_path,
                output_path,
                api_key,
                use_emojis,
                badge_style,
                project_logo,
                header_alignment,
                context_window,
                model,
                api_service,
                header_style,
                toc_style,
                badge_color,
                tree_depth,
                llm_image,
            )
            try:
                execute_command(command, api_key, output_path)

                st.success("✅ Successfully generated README.md file.")

                with open(output_path) as file:
                    readme_content = file.read()

                st.session_state.readme_generated = True
                st.session_state.readme_content = readme_content

                if st.session_state.readme_generated:
                    with st.expander("Preview File", expanded=True):
                        st.markdown(readme_content, unsafe_allow_html=True)

                    with st.expander("Download File"):
                        st.download_button(
                            label="Download :blue[README-AI.md]",
                            data=readme_content,
                            file_name="README-AI.md",
                            mime="text/markdown",
                        )

                    with st.expander("Copy Markdown"):
                        st.write("Copy the markdown below to your clipboard.")
                        st.code(readme_content, language="markdown")

            except (Exception, subprocess.CalledProcessError) as exc:
                logging.error(f"An error occurred: {exc}")
                st.error(f"❌ README generation failed.\nError: {exc!s}")


if __name__ == "__main__":
    main()
