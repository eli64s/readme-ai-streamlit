import streamlit as st
import subprocess
import os

from utils import get_readme_file_content, get_readme_file_download_link


st.title("README-AI")
st.write("🚀 Generate beautiful README.md files, powered by OpenAI's GPT LLMs 💫")

generate_readme = False

with st.sidebar:
    st.header("README-AI Inputs")
    api_key = st.text_input("OpenAI API Key:", type="password")
    output_path = st.text_input("Output Path for README.md:", "readme-ai.md")
    repository_url = st.text_input("Repository URL or local path:", "")
    
    if st.button("Generate README", key="sidebar_button"):
        generate_readme = True

if generate_readme:
    st.header("Status")

    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
    
    command = ["readmeai"]
    if output_path:
        command.extend(["--output", output_path])
    if repository_url:
        command.extend(["--repository", repository_url])

    with st.spinner('Generating your README.md 🙂...'):
        try:
            completed_process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            
            st.success("README generated successfully!")

            if os.path.exists(output_path):
                with open(output_path, 'r') as file:
                    readme_content = file.read()

                st.header("README.md Content")
                
       
                file_content = get_readme_file_content(output_path)
                st.markdown(get_readme_file_download_link(file_content), unsafe_allow_html=True)

                with st.container():
                    st.code(readme_content, language='markdown')
                
        except subprocess.CalledProcessError as e:
            st.error("Failed to generate README")
            st.write("Command failed with error:", e.stderr)
