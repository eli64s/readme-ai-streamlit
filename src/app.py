import asyncio
import logging
import os
import subprocess
import tempfile

import streamlit as st

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


TITLE = "README-AI"
DESCRIPTION = """
README file generator, powered by AI.
"""

SUPPORTED_MODELS = {
    "OPENAI": ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo"],
    "ANTHROPIC": ["claude-3-opus-20240229", "claude-3-sonnet-20240229"],
    "GEMINI": ["gemini-1.5-pro", "gemini-1.5-flash"],
    "OLLAMA": ["llama3", "mistral", "gemma"],
    "OFFLINE": ["offline-mode"],
}

BADGE_STYLES = [
    "default",
    "flat",
    "flat-square",
    "plastic",
    "for-the-badge",
    "skills",
    "skills-light",
    "social",
]

LOGO_OPTIONS = [
    "blue",
    "gradient",
    "black",
    "cloud",
    "purple",
    "grey",
    "custom",
    "llm",
]

HEADER_STYLES = ["classic", "modern", "compact", "ascii", "ascii_box", "svg"]

TOC_STYLES = ["bullet", "fold", "links", "number", "roman"]


class ReadmeAIApp:
    """
    Streamlit web app serving the readme-ai CLI.
    """

    def __init__(self):
        self.init_session_state()
        self.setup_page_config()
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    def init_session_state(self) -> None:
        if "readme_generated" not in st.session_state:
            st.session_state.readme_generated = False
        if "readme_content" not in st.session_state:
            st.session_state.readme_content = ""
        if "selected_provider" not in st.session_state:
            st.session_state.selected_provider = "OPENAI"
        if "selected_model" not in st.session_state:
            st.session_state.selected_model = "gpt-3.5-turbo"

    def setup_page_config(self) -> None:
        """Configure Streamlit page settings."""
        st.set_page_config(
            page_title="README-AI",
            # page_icon="📚",
            layout="wide",
            initial_sidebar_state="expanded",
            menu_items={
                "Get Help": "https://github.com/eli64s/readme-ai/discussions",
                "Report a bug": "https://github.com/eli64s/readme-ai/issues",
                "About": "https://eli64s.github.io/readme-ai/",
            },
        )

    def render_header(self) -> None:
        """Render application header."""
        col1, _ = st.columns([0.99, 0.01])
        with col1:
            st.image(
                "assets/logo.svg",
                width=600,
            )
            st.markdown(DESCRIPTION)

    def render_sidebar(self) -> tuple[str, str, dict]:
        """Render sidebar with configuration options."""
        with st.sidebar:
            st.title("Configuration")
            st.subheader("Repository Settings")
            repo_path = st.text_input(
                "Repository URL/Path",
                value="https://github.com/eli64s/readme-ai",
                help="Enter a GitHub repository URL or local path",
            )

            st.subheader("LLM Provider")
            selected_provider = st.radio(
                "Select Provider",
                options=list(SUPPORTED_MODELS.keys()),
                horizontal=True,
            )
            st.session_state.selected_provider = selected_provider

            api_key = st.text_input("API Key", type="password")

            model = st.selectbox(
                "Model",
                options=SUPPORTED_MODELS[selected_provider],
                index=0,
                key="model_selection",
            )
            st.subheader("Quick Links")
            st.markdown(
                """
                <style>
                    .link-box {
                        display: inline-flex;
                        align-items: center;
                        padding: 8px 12px;
                        margin: 4px;
                        border-radius: 8px;
                        background: #f8f9fa;
                        border: 1px solid #dee2e6;
                        text-decoration: none;
                        color: #495057;
                        transition: all 0.2s ease;
                    }

                    .link-box:hover {
                        background: #e9ecef;
                        transform: translateY(-2px);
                        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                    }

                    .link-box svg {
                        width: 20px;
                        height: 20px;
                        margin-right: 8px;
                    }

                    .link-container {
                        display: flex;
                        flex-direction: column;
                        gap: 8px;
                        margin-bottom: 20px;
                    }
                </style>
                <div class="link-container">
                    <a href="https://eli64s.github.io/readme-ai/" class="link-box" target="_blank">
                        <svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><title>Material for MkDocs</title>
                            <path d="m17.029 18.772.777 1.166-5.417 2.709L0 16.451V4.063l5.417-2.709 5.298 7.948 7.867-5.24L24 1.354V16.84l-5.417 2.709zm2.023-13.827v13.253l3.949-1.975V2.97zM5.076 2.642 1.458 4.45 12.73 21.358l3.618-1.809z"/>
                        </svg>
                        Documentation
                    </a>
                    <a href="https://github.com/eli64s/readme-ai" class="link-box" target="_blank">
                        <svg fill="#181717" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12" />
                        </svg>
                        GitHub
                    </a>
                    <a href="https://pypi.org/project/readmeai/" class="link-box" target="_blank">
                        <svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><title>Python</title>
                            <path d="M14.25.18l.9.2.73.26.59.3.45.32.34.34.25.34.16.33.1.3.04.26.02.2-.01.13V8.5l-.05.63-.13.55-.21.46-.26.38-.3.31-.33.25-.35.19-.35.14-.33.1-.3.07-.26.04-.21.02H8.77l-.69.05-.59.14-.5.22-.41.27-.33.32-.27.35-.2.36-.15.37-.1.35-.07.32-.04.27-.02.21v3.06H3.17l-.21-.03-.28-.07-.32-.12-.35-.18-.36-.26-.36-.36-.35-.46-.32-.59-.28-.73-.21-.88-.14-1.05-.05-1.23.06-1.22.16-1.04.24-.87.32-.71.36-.57.4-.44.42-.33.42-.24.4-.16.36-.1.32-.05.24-.01h.16l.06.01h8.16v-.83H6.18l-.01-2.75-.02-.37.05-.34.11-.31.17-.28.25-.26.31-.23.38-.2.44-.18.51-.15.58-.12.64-.1.71-.06.77-.04.84-.02 1.27.05zm-6.3 1.98l-.23.33-.08.41.08.41.23.34.33.22.41.09.41-.09.33-.22.23-.34.08-.41-.08-.41-.23-.33-.33-.22-.41-.09-.41.09zm13.09 3.95l.28.06.32.12.35.18.36.27.36.35.35.47.32.59.28.73.21.88.14 1.04.05 1.23-.06 1.23-.16 1.04-.24.86-.32.71-.36.57-.4.45-.42.33-.42.24-.4.16-.36.09-.32.05-.24.02-.16-.01h-8.22v.82h5.84l.01 2.76.02.36-.05.34-.11.31-.17.29-.25.25-.31.24-.38.2-.44.17-.51.15-.58.13-.64.09-.71.07-.77.04-.84.01-1.27-.04-1.07-.14-.9-.2-.73-.25-.59-.3-.45-.33-.34-.34-.25-.34-.16-.33-.1-.3-.04-.25-.02-.2.01-.13v-5.34l.05-.64.13-.54.21-.46.26-.38.3-.32.33-.24.35-.2.35-.14.33-.1.3-.06.26-.04.21-.02.13-.01h5.84l.69-.05.59-.14.5-.21.41-.28.33-.32.27-.35.2-.36.15-.36.1-.35.07-.32.04-.28.02-.21V6.07h2.09l.14.01zm-6.47 14.25l-.23.33-.08.41.08.41.23.33.33.23.41.08.41-.08.33-.23.23-.33.08-.41-.08-.41-.23-.33-.33-.23-.41-.08-.41.08z"/>
                        </svg>
                        PyPI
                    </a>
                    <!--Docker Hub-->
                    <a href="https://hub.docker.com/r/zeroxeli/readme-ai" class="link-box" target="_blank">
                        <svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <title>Docker</title>
                            <path
                                d="M13.983 11.078h2.119a.186.186 0 00.186-.185V9.006a.186.186 0 00-.186-.186h-2.119a.185.185 0 00-.185.185v1.888c0 .102.083.185.185.185m-2.954-5.43h2.118a.186.186 0 00.186-.186V3.574a.186.186 0 00-.186-.185h-2.118a.185.185 0 00-.185.185v1.888c0 .102.082.185.185.185m0 2.716h2.118a.187.187 0 00.186-.186V6.29a.186.186 0 00-.186-.185h-2.118a.185.185 0 00-.185.185v1.887c0 .102.082.185.185.186m-2.93 0h2.12a.186.186 0 00.184-.186V6.29a.185.185 0 00-.185-.185H8.1a.185.185 0 00-.185.185v1.887c0 .102.083.185.185.186m-2.964 0h2.119a.186.186 0 00.185-.186V6.29a.185.185 0 00-.185-.185H5.136a.186.186 0 00-.186.185v1.887c0 .102.084.185.186.186m5.893 2.715h2.118a.186.186 0 00.186-.185V9.006a.186.186 0 00-.186-.186h-2.118a.185.185 0 00-.185.185v1.888c0 .102.082.185.185.185m-2.93 0h2.12a.185.185 0 00.184-.185V9.006a.185.185 0 00-.184-.186h-2.12a.185.185 0 00-.184.185v1.888c0 .102.083.185.185.185m-2.964 0h2.119a.185.185 0 00.185-.185V9.006a.185.185 0 00-.184-.186h-2.12a.186.186 0 00-.186.186v1.887c0 .102.084.185.186.185m-2.92 0h2.12a.185.185 0 00.184-.185V9.006a.185.185 0 00-.184-.186h-2.12a.185.185 0 00-.184.185v1.888c0 .102.082.185.185.185M23.763 9.89c-.065-.051-.672-.51-1.954-.51-.338.001-.676.03-1.01.087-.248-1.7-1.653-2.53-1.716-2.566l-.344-.199-.226.327c-.284.438-.49.922-.612 1.43-.23.97-.09 1.882.403 2.661-.595.332-1.55.413-1.744.42H.751a.751.751 0 00-.75.748 11.376 11.376 0 00.692 4.062c.545 1.428 1.355 2.48 2.41 3.124 1.18.723 3.1 1.137 5.275 1.137.983.003 1.963-.086 2.93-.266a12.248 12.248 0 003.823-1.389c.98-.567 1.86-1.288 2.61-2.136 1.252-1.418 1.998-2.997 2.553-4.4h.221c1.372 0 2.215-.549 2.68-1.009.309-.293.55-.65.707-1.046l.098-.288Z" />
                        </svg>
                        Docker
                </div>
                """,
                unsafe_allow_html=True,
            )
            return (
                repo_path,
                api_key,
                self.get_model_config(selected_provider, model),
            )

    def render_main_options(self) -> dict:
        """Render main configuration options."""
        st.subheader("Customization Options")
        st.markdown("Customize the README output with the following options:")

        col1, col2, col3 = st.columns(3)
        with col1:
            header_style = st.selectbox("Header Style", HEADER_STYLES)
            badge_style = st.selectbox("Badge Style", BADGE_STYLES)
            image = st.selectbox("Project Logo", LOGO_OPTIONS)
        with col2:
            toc_style = st.selectbox("Table of Contents Style", TOC_STYLES)
            align = st.selectbox(
                "Content Alignment", ["center", "left", "right"]
            )
            badge_color = st.color_picker("Badge Color", "#0080ff")

        col1, col2, col3 = st.columns(3)
        with col1:
            context_window = st.number_input("Context Window", 1, 99999, 3900)
        with col2:
            temperature = st.slider("Temperature", 0.0, 2.0, 0.1)
        with col3:
            tree_depth = st.slider("Directory Tree Depth", 1, 5, 2)

        emojis = st.checkbox("Enable Emojis")

        return {
            "badge_style": badge_style,
            "header_style": header_style,
            "image": image,
            "toc_style": toc_style,
            "align": align,
            "badge_color": badge_color,
            "tree_depth": tree_depth,
            "context_window": context_window,
            "temperature": temperature,
            "emojis": emojis,
        }

    def render_output_section(self) -> None:
        """Render README output section."""
        if st.session_state.readme_generated:
            tabs = st.tabs(["Preview", "Markdown", "Download"])

            with tabs[0]:
                st.markdown(
                    st.session_state.readme_content, unsafe_allow_html=True
                )

            with tabs[1]:
                st.code(st.session_state.readme_content, language="markdown")

            with tabs[2]:
                st.download_button(
                    "Download README.md",
                    st.session_state.readme_content,
                    file_name="README.md",
                    mime="text/markdown",
                    use_container_width=True,
                )

    def get_model_config(self, provider: str, model: str) -> dict:
        """Get model configuration based on provider."""
        return {
            "provider": provider.lower(),
            "model": model,
        }

    def build_command(
        self, repo_path: str, output_path: str, config: dict, options: dict
    ) -> list[str]:
        """Build command for readme-ai CLI."""
        cmd = [
            "readmeai",
            "--repository",
            repo_path,
            "--output",
            output_path,
            "--api",
            config["provider"],
            "--model",
            config["model"],
        ]

        for key, value in options.items():
            if isinstance(value, bool):
                if value:
                    cmd.extend([f"--{key.replace('_', '-')}"])
            else:
                if key == "badge_color" and isinstance(value, str):
                    value = value.lstrip("#")  # Remove # from hex color
                cmd.extend([f"--{key.replace('_', '-')}", str(value)])

        return cmd

    async def generate_readme(
        self, repo_path: str, api_key: str, config: dict, options: dict
    ) -> None:
        """Generate README using provided configuration."""
        try:
            with tempfile.NamedTemporaryFile(
                suffix=".md", mode="w+", delete=False
            ) as tmp:
                command = self.build_command(
                    repo_path, tmp.name, config, options
                )
                await self.execute_command(command, api_key, tmp.name)

                with open(tmp.name) as f:
                    st.session_state.readme_content = f.read()
                    st.session_state.readme_generated = True

        except Exception as e:
            st.error(f"Error generating README: {e!s}")
            logger.error(f"README generation failed: {e!s}", exc_info=True)

    async def execute_command(
        self, command: list[str], api_key: str, output_path: str
    ) -> None:
        """Execute the command and handle its output."""
        with st.spinner("Generating README..."):
            env = os.environ.copy()
            if api_key:
                if st.session_state.selected_provider == "OPENAI":
                    env["OPENAI_API_KEY"] = api_key
                elif st.session_state.selected_provider == "ANTHROPIC":
                    env["ANTHROPIC_API_KEY"] = api_key
                elif st.session_state.selected_provider == "GEMINI":
                    env["GOOGLE_API_KEY"] = api_key

            process = await asyncio.create_subprocess_exec(
                *command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                env=env,
            )

            output_container = st.empty()
            stderr_accumulated = ""

            while True:
                try:
                    stderr_line = await process.stderr.readline()
                    if not stderr_line:
                        break

                    if line := stderr_line.decode().strip():
                        stderr_accumulated += line + "\n"
                        output_container.text_area(
                            "Generation Logs",
                            value=stderr_accumulated,
                            height=150,
                        )
                except Exception as e:
                    logger.error(f"Error reading process output: {e}")
                    break

            returncode = await process.wait()
            if returncode != 0:
                raise subprocess.CalledProcessError(
                    returncode, command, stderr_accumulated
                )

    def run(self) -> None:
        """Run the Streamlit application."""
        self.render_header()

        repo_path, api_key, model_config = self.render_sidebar()
        options = self.render_main_options()

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Generate README", use_container_width=True):
                self.loop.run_until_complete(
                    self.generate_readme(
                        repo_path, api_key, model_config, options
                    )
                )
        with col2:
            if st.button("Reset", use_container_width=True):
                st.session_state.readme_generated = False
                st.session_state.readme_content = ""
                st.rerun()

        self.render_output_section()

    def __del__(self):
        """Cleanup the event loop on deletion."""
        if hasattr(self, "loop") and self.loop is not None:
            try:
                self.loop.close()
            except Exception as e:
                logger.error(f"Error closing event loop: {e}")


if __name__ == "__main__":
    app = ReadmeAIApp()
    app.run()
