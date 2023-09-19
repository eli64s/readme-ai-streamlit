"""Utility functions for the Streamlit readmeai app."""

import base64


def get_readme_file_content(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    return content.encode('utf-8')

def get_readme_file_download_link(file_content, file_name="README.md"):
    b64 = base64.b64encode(file_content).decode()
    return f'<a href="data:application/octet-stream;base64,{b64}" download="{file_name}">Download README.md</a>'
