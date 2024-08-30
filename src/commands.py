"""
CLI commands for the README-AI Streamlit web app.
"""

import os
import subprocess

import streamlit as st


def build_command(
    repo_path: str,
    output_path: str,
    api_key: str,
    use_emojis: bool,
    badge_style: str,
    project_logo: str,
    header_alignment: str,
    context_window: int,
    model: str,
    api_service: str,
    header_style: str,
    toc_style: str,
    badge_color: str,
    tree_depth: int,
    llm_image: bool,
) -> list[str]:
    command = ["readmeai", "--repository", repo_path, "--output", output_path]

    command.extend(["--api", api_service])

    if model != "offline-mode":
        command.extend(["--model", model])

    if use_emojis:
        command.extend(["--emojis"])

    command.extend(["--align", header_alignment])
    command.extend(["--badge-color", badge_color.lstrip("#")])
    command.extend(["--badge-style", badge_style])
    command.extend(["--image", "llm" if llm_image else project_logo])
    command.extend(["--header-style", header_style])
    command.extend(["--toc-style", toc_style])
    command.extend(["--tree-depth", str(tree_depth)])
    command.extend(["--context-window", str(context_window)])

    return command


def execute_command(command: list[str], api_key: str, path: str) -> None:
    """
    Execute the command and handle its output.
    """
    with st.spinner(f"Processing repository - {path}"):
        env = os.environ.copy()
        if api_key:
            env["OPENAI_API_KEY"] = api_key

        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env,
        )
        output_container = st.empty()
        stderr_accumulated = ""

        while True:
            stderr_line = process.stderr.readline()
            if stderr_line:
                stderr_accumulated += stderr_line
                output_container.text_area(
                    "readme-ai logs",
                    value=stderr_accumulated,
                    height=150,
                )
            if process.poll() is not None:
                break

        if process.returncode != 0:
            raise subprocess.CalledProcessError(
                process.returncode, command, stderr_accumulated
            )
