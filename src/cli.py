"""Streamlit web app serving the Python package CLI readmeai."""


import os
from typing import List, Tuple

import streamlit as st


def app_settings() -> (
    Tuple[str, str, str, str, str, bool, bool, bool, int, str, float]
):
    """Collect user inputs from the sidebar."""
    with st.expander("Repository & LLM Settings", expanded=True):
        repo_path = st.text_input(
            "Repository URL",
            value="https://github.com/eli64s/readme-ai-streamlit",
        )
        run_offline = st.radio(
            "README Engine",
            ["Offline", "LLM API"],
            key="run_offline",
            index=0,
            help="Run readme-ai without using an API key.",
        )
        if run_offline == "LLM API":
            run_offline = False
            api_key = st.text_input("API Key", type="password")
            model = st.selectbox(
                "Language Model",
                [
                    "gpt-3.5-turbo",
                    "gpt-3.5-turbo-1106",
                    "gpt-4",
                    "gpt-4-1106-preview",
                ],
                index=0,
            )
            max_tokens = st.number_input(
                "Maximun Tokens",
                key="max_tokens",
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
                step=0.01,
                format="%f",
                help="The higher the temperature, the crazier the text.",
            )
        else:
            run_offline = True
            api_key = ""
            model = ""
            max_tokens = 0
            temperature = 1.0

    with st.expander("Markdown Settings", expanded=False):
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
            help="Style of badges for README header.",
        )
        st.markdown(
            """
            >![for-the-badge](https://img.shields.io/badge/for%20the%20badge-0080ff?style=for-the-badge)
            >![flat-square](https://img.shields.io/badge/flat%20square-0080ff?style=flat-square)
            >![flat](https://img.shields.io/badge/flat-0080ff?style=flat)
            >![plastic](https://img.shields.io/badge/plastic-0080ff?style=plastic)
![social](https://img.shields.io/badge/social-0080ff?style=social)
![flat](https://img.shields.io/badge/red-FF0000?style=flat)
![flat-square](https://img.shields.io/badge/orange-FF7F00?style=flat-square)
![plastic](https://img.shields.io/badge/yellow-FFFF00?style=plastic)  
![for-the-badge](https://img.shields.io/badge/green-00FF00?style=for-the-badge)
![skills](https://img.shields.io/badge/blue-0000FF?style=skills)
![skills-light](https://img.shields.io/badge/indigo-4B0082?style=skills-light)
![for-the-badge](https://img.shields.io/badge/violet-8A2BE2?style=for-the-badge)

            """
        )
        alignment = st.radio(
            "Header Alignment",
            ["left", "center"],
            index=0,
            horizontal=True,
            help="Alignment of the header in README.",
        )
        use_emojis = st.checkbox(
            "Include Emojis",
            value=False,
            help="Include emojis in README headers.",
        )

    with st.expander("Additional Settings", expanded=False):
        project_logo = st.selectbox(
            "Project Logo",
            ["black", "cloud", "gradient", "grey", "purple", "yellow"],
            index=1,
            help="Select a project logo for README.",
        )

        st.markdown(
            """
                    | **Options**   | **Preview** |
                    |---------------|----------------|
                    | **default**   | ![img](https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg) |
                    | **black**     | ![img](https://img.icons8.com/external-tal-revivo-regular-tal-revivo/96/external-readme-is-a-easy-to-build-a-developer-hub-that-adapts-to-the-user-logo-regular-tal-revivo.png) |
                    | **gradient**  | ![img](https://img.icons8.com/?size=512&id=55494&format=png) |
                    | **grey**      | ![img](https://img.icons8.com/external-tal-revivo-filled-tal-revivo/96/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-filled-tal-revivo.png) |
                    | **purple**    | ![img](https://img.icons8.com/external-tal-revivo-duo-tal-revivo/100/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-duo-tal-revivo.png) |
                    | **yellow**    | ![img](https://img.icons8.com/pulsar-color/96/markdown.png) |
                    | **cloud**     | ![img](https://cdn-icons-png.flaticon.com/512/6295/6295417.png) |
        """,
            unsafe_allow_html=True,
        )

    col1, col2 = st.columns(2)
    with col1:
        generate_readme = st.button(":blue[Run]", use_container_width=True)
    with col2:
        reset_session = st.button("Reset", use_container_width=True)

    if reset_session:
        st.session_state.readme_generated = False
        st.session_state.readme_content = ""
    elif generate_readme:
        st.session_state.readme_generated = True
        st.session_state.readme_content = "Generating README..."

    return (
        api_key,
        alignment,
        project_logo,
        repo_path,
        badge_style,
        use_emojis,
        run_offline,
        generate_readme,
        max_tokens,
        model,
        temperature,
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
    temperature: float,
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
    command.extend(["--temperature", str(temperature)])

    # if template:
    #    command.extend(["--template", template])
    # command.extend(["--language", language])

    return command
