"""Utility functions for the Streamlit app."""

import tempfile


def get_readme_tempfile(content: str) -> str:
    """Generate a temporary README file and return its path."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".md", mode="w+") as tmpfile:
        tmpfile.write(content)
        return tmpfile.name
