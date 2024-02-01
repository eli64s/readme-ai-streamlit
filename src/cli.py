"""Streamlit web app serving the Python package CLI readmeai."""

import os
from typing import List, Tuple

import streamlit as st


def app_settings() -> Tuple[str, str, str, str, str, bool, bool, bool, int, str, float]:
    """Collect user inputs from the sidebar."""
    with st.sidebar:
        st.title(":blue[README Configuration]")

        repo_path = st.text_input(
            "Repository", value="https://github.com/eli64s/readme-ai-streamlit"
        )

        api_key = st.text_input("LLM API Key", type="password")

        col1, col2 = st.columns(2)
        with col1:
            run_offline = st.toggle(
                "Offline",
                value=False,
                help="Run readme-ai without using an API key.",
            )
        with col2:
            use_emojis = st.toggle(
                "Emojis",
                value=False,
                help="Include emojis in each header of the README file.",
            )

        badge_style = st.selectbox(
            "Badge Style",
            [
                "flat",
                "flat-square",
                "plastic",
                "for-the-badge",
                "skills",
                "skills-light",
                "social",
            ],
            index=0,
            help="Style of the badges to include in the README file header.",
        )

        project_logo = st.selectbox(
            "Project Logo",
            ["black", "cloud", "gradient", "grey", "purple", "yellow"],
            index=1,
            help="URL or path to the project logo image for the README header.",
        )

        header_alignment = st.selectbox(
            "Header Alignment",
            ["center", "left"],
            index=0,
            help="Align the header text to the left or center of the README file.",
        )

        model = st.selectbox(
            "Language Model",
            ["gpt-3.5-turbo", "gpt-3.5-turbo-1106", "gpt-4", "gpt-4-1106-preview"],
            index=0,
        )
        max_tokens = st.number_input(
            "Max Tokens",
            min_value=1,
            max_value=99999,
            value=999,
            step=1,
            help="Max tokens to generate.",
        )
        temperature = st.slider(
            "Temperature",
            0.0,
            2.0,
            1.0,
            step=0.1,
            format="%f",
            help="The higher the temperature, the crazier the text.",
        )

        # template = st.text_input("Template", "")
        # language = st.selectbox(
        #    "Language",
        #   ["English (en)", "other-languages"],
        #    index=0,
        # )

        col1, col2 = st.columns(2)
        with col1:
            generate_readme = st.button("Run", use_container_width=True)
        with col2:
            reset_session = st.button("Reset", use_container_width=True)

        if reset_session:
            st.session_state.readme_generated = False
            st.session_state.readme_content = ""
            st.rerun()

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


def build_command(
    repo_path: str,
    output_path: str,
    api_key: str,
    use_emojis: bool,
    badge_style: str,
    project_logo: str,
    header_alignment: str,
    max_tokens: int,
    model: str,
    run_offline: bool,
) -> List[str]:
    """Build the command to execute the readme-ai CLI and generate the README."""
    command = ["readmeai", "--repository", repo_path, "--output", output_path]

    if not run_offline:
        os.environ["OPENAI_API_KEY"] = api_key
    else:
        command.extend(["--offline"])

    if use_emojis:
        command.extend(["--emojis"])

    command.extend(["--badges", badge_style])
    command.extend(["--image", project_logo])
    command.extend(["--align", header_alignment])
    command.extend(["--max-tokens", str(max_tokens)])
    command.extend(["--model", model])

    # if template:
    #    command.extend(["--template", template])
    # command.extend(["--language", language])

    return command
