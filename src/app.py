import streamlit as st
import subprocess
import os
import base64

def get_readme_file_content(file_path):
    """Gets the content of the README.md file and encodes it for download."""
    with open(file_path, 'r') as f:
        content = f.read()
    return content.encode('utf-8')

def get_readme_file_download_link(file_content, file_name="README.md"):
    """Generates a link allowing the data in a given string to be downloaded"""
    b64 = base64.b64encode(file_content).decode()
    return f'<a href="data:application/octet-stream;base64,{b64}" download="{file_name}">Download README.md</a>'

st.title("README-AI")
st.write("🚀 Generate beautiful README files, powered by OpenAI's GPT LLMs 💫")

with st.sidebar:
    st.header("README-AI Inputs")
    api_key = st.text_input("OpenAI API Key:", type="password")
    output_path = st.text_input("Output Path for README.md:", "readme-ai.md")
    repository_url = st.text_input("Repository URL or local path:", "")
    
    if st.button("Generate README", key="sidebar_button"):
        generate_readme = True
    else:
        generate_readme = False

st.header("Status")

if generate_readme:
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
    
    command = ["readmeai"]
    if output_path:
        command.extend(["--output", output_path])
    if repository_url:
        command.extend(["--repository", repository_url])

    with st.spinner('Generating README...'):
        try:
            completed_process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            
            st.success("README generated successfully!")
            st.write("Status code:", completed_process.returncode)
            st.write("Output:\n", completed_process.stdout)

            if os.path.exists(output_path):
                with open(output_path, 'r') as file:
                    readme_content = file.read()

                st.header("README.md Content")
                
                # Place Copy and Download buttons here
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write("To copy the README, select the text in the box below and press `Ctrl + C`.")
                
                with col2:
                    file_content = get_readme_file_content(output_path)
                    st.markdown(get_readme_file_download_link(file_content), unsafe_allow_html=True)
                
                # Show README content
                st.code(readme_content, language='markdown')
                
        except subprocess.CalledProcessError as e:
            st.error("Failed to generate README")
            st.write("Command failed with error:", e.stderr)
