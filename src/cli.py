"""
CLI configuration settings for the README-AI Streamlit web app.
"""

import logging

import streamlit as st

logging.basicConfig(level=logging.INFO)

QUICK_LINKS = """
<div align="left">

[Docs](https://eli64s.github.io/readme-ai/) &nbsp;&nbsp;|&nbsp;&nbsp;
[GitHub](https://github.com/eli64s/readme-ai) &nbsp;&nbsp;|&nbsp;&nbsp;
[PyPI](https://pypi.org/project/readmeai/)

</div>
"""


def app_settings() -> (
    tuple[
        str,
        str,
        str,
        str,
        str,
        bool,
        bool,
        int,
        str,
        float,
        str,
        str,
        str,
        str,
        int,
        bool,
    ]
):
    with st.sidebar:
        st.title(":rainbow[README-AI]")
        st.markdown(QUICK_LINKS, unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("### Configuration")

        repo_path = st.text_input(
            "Repository", value="https://github.com/eli64s/readme-ai"
        )
        api_key = st.text_input("LLM API Key", type="password")

        col1, col2 = st.columns(2)
        with col1:
            use_emojis = st.toggle(
                "Emoji Headings",
                value=False,
                help="Include emojis in headings.",
            )
        with col2:
            llm_image = st.toggle(
                "LLM Image",
                value=False,
                help="Generate project logo using LLM (OpenAI only).",
            )

        api_service = st.selectbox(
            "LLM API",
            ["openai", "ollama", "gemini", "offline"],
            index=0,
        )

        model = st.selectbox(
            "Language Model",
            [
                "gpt-3.5-turbo",
                "gpt-4",
                "gpt-4-turbo",
                "llama2",
                "llama3",
                "llama3.1",
                "gemma2",
                "mistral",
                "gemini-1.5-flash",
                "offline-mode",
            ],
            index=0,
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
            help="Badge Style",
        )

        project_logo = st.selectbox(
            "Project Logo",
            [
                "blue",
                "gradient",
                "black",
                "cloud",
                "purple",
                "grey",
                "custom",
                "llm",
            ],
            index=1,
            help="Project Logo Image",
        )

        header_style = st.selectbox(
            "Header Style",
            ["classic", "modern", "compact"],
            index=0,
            help="Style of the README header.",
        )

        toc_style = st.selectbox(
            "Table of Contents Style",
            ["bullet", "fold", "links", "number"],
            index=0,
            help="Style of the table of contents.",
        )

        header_alignment = st.selectbox(
            "Header Alignment",
            ["center", "left", "right"],
            index=0,
            help="README file header alignment.",
        )

        badge_color = st.color_picker(
            "Badge Color", "#0080ff", help="Color for the badges (hex code)."
        )

        col1, col2 = st.columns(2)
        with col1:
            context_window = st.number_input(
                "Context Window",
                min_value=1,
                max_value=99999,
                value=999,
                step=1,
            )
        with col2:
            temperature = st.slider(
                "Temperature", 0.0, 2.0, 0.9, step=0.1, format="%f"
            )

        tree_depth = st.slider(
            "Tree Depth",
            1,
            5,
            2,
            step=1,
            help="Maximum depth of the directory tree structure.",
        )

        col1, col2 = st.columns(2)
        with col1:
            generate_readme = st.button("Generate", use_container_width=True)
        with col2:
            reset_session = st.button("Reset", use_container_width=True)

    return (
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
    )
