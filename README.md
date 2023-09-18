<div align="center">
<h1 align="center">
    <img src="https://img.icons8.com/?size=512&id=55494&format=png" width="80" />
    <img src="https://img.icons8.com/?size=512&id=kTuxVYRKeKEY&format=png" width="80" />
    <br>READMEAI-UI
</h1>
<h3>◦ Unleash your READMEs potential with readmeai's Streamlit app!</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?logo=Streamlit&logoColor=white", alt="Streamlit" />
<img src="https://img.shields.io/badge/OpenAI-412991.svg?logo=OpenAI&logoColor=white" alt="OpenAI" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?logo=Markdown&logoColor=white" alt="Markdown" />
</p>
<img src="https://img.shields.io/github/languages/top/eli64s/readmeai-ui?style&color=5D6D7E" alt="GitHub top language" />
<img src="https://img.shields.io/github/languages/code-size/eli64s/readmeai-ui?style&color=5D6D7E" alt="GitHub code size in bytes" />
<img src="https://img.shields.io/github/commit-activity/m/eli64s/readmeai-ui?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/license/eli64s/readmeai-ui?style&color=5D6D7E" alt="GitHub license" />
</div>

---

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [⚙️ Features](#️-features)
- [📂 Project Structure](#-project-structure)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The readmeai-ui project is a web app built with Streamlit that generates README files based on user input. It provides a user-friendly interface where users can input an API key, output path, and repository URL/local path to generate a README file. The app handles the execution of an external tool to generate the README and displays it to the user, allowing for copying and downloading. Its purpose is to simplify the process of creating README files and streamline documentation for repositories, offering convenience and efficiency to developers.

---

## ⚙️ Features

| Feature                | Description                           |
| ---------------------- | ------------------------------------- |
| **⚙️ Architecture**     | The project follows a simple architecture where there is a Streamlit web app component (src/app.py) that interacts with a bash script (scripts/clean.sh) to generate README files. The app component takes user input, executes a subprocess command, and displays the generated README file. |
| **📖 Documentation**   | The codebase lacks comprehensive documentation. There are comments in individual files explaining their purpose and some usage instructions in the app.py file. However, there is no overall project documentation or guide for developers. |
| **🔗 Dependencies**    | The main dependency is Streamlit, which is used to create the web app. There doesn't seem to be any major external libraries or systems requirements besides basic Python libraries. |
| **🧩 Modularity**      | The codebase is organized into two main components: the web app component (src/app.py) and the bash script component (scripts/clean.sh). These components can be changed or extended independently without affecting the other. |
| **✔️ Testing**          | There is no explicit testing strategy or test suite evident in the codebase. It would be beneficial to implement unit tests for critical components such as the subprocess command execution and the generated README. |
| **⚡️ Performance**      | Since the main functionality involves generating README files, the performance seems to be adequate. However, without further performance benchmarks or scalability considerations, it is challenging to evaluate the overall performance. |
| **🔐 Security**        | The codebase doesn't specifically address security measures or apply any security patterns. It is recommended to implement input parsing and validation to prevent potential security vulnerabilities in user inputs. |
| **🔀 Version Control** | The project utilizes Git for version control, evident by its presence as a public repository on GitHub. It follows the standard Git workflow, allowing multiple contributors to collaborate, track changes, and manage different versions of the codebase. |
| **🔌 Integrations**    | There are no explicit integrations mentioned in the codebase. However, since the project interacts with external tools for generating README files through subprocess commands, it allows integration with such tools. |
| **📶 Scalability**     | It is difficult to assess the scalability of the system based on the available codebase. The web app component can be extended to support additional functionalities easily. However, further scalability considerations would require analyzing the external tool used for README generation and its inherent limitations. |

---


## 📂 Project Structure




---

## 🧩 Modules

<details closed><summary>Scripts</summary>

| File                                                                         | Summary                                                                                                                                                                                                                                                 |
| ---                                                                          | ---                                                                                                                                                                                                                                                     |
| [clean.sh](https://github.com/eli64s/readmeai-ui/blob/main/scripts/clean.sh) | This code is a bash script that removes specific files and directories, such as backup files, cache files, build artifacts, and log files. It also removes specific directories like "__pycache__", ".ipynb_checkpoints", ".ruff_cache", and ".vscode". |

</details>

<details closed><summary>Src</summary>

| File                                                                 | Summary                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                  | ---                                                                                                                                                                                                                                                                                                                                           |
| [app.py](https://github.com/eli64s/readmeai-ui/blob/main/src/app.py) | This code uses Streamlit to create a web app for generating README files. It takes input for an API key, output path, and repository URL/local path. It executes a subprocess command to generate the README using an external tool. The app displays the generated README, allows for copying and downloading, and handles potential errors. |

</details>

---

## 🚀 Getting Started


---


## 🗺 Roadmap

- [ ] Deploy to Streamlit production server.

---

## 🤝 Contributing

[Contributing Guide](./CONTRIBUTING.md)

---

## 📄 License

[Apache License 2.0](./LICENSE)

---

## 👏 Acknowledgments

---
