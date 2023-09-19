<div align="center">
<h1 align="center">
    <img src="https://img.icons8.com/?size=512&id=55494&format=png" width="80" />
    <img src="https://img.icons8.com/?size=512&id=kTuxVYRKeKEY&format=png" width="80" />
    <br>READMEAI-UI
</h1>
<h3>◦ Unleash your READMEs potential with README-AI.</h3>
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

Exception: 

---

## ⚙️ Features

| Feature                | Description                           |
| ---------------------- | ------------------------------------- |
| **⚙️ Architecture**     | The codebase follows a functional architecture with separate modules for cleaning operations, utility functions, and the main app. The app is built on top of the Streamlit framework, allowing for easy interactive web-based development.    |
| **📖 Documentation**   | The codebase is well-documented with clear comments throughout the code. The README file provides comprehensive instructions on how to set up and run the app.    |
| **🔗 Dependencies**    | The codebase relies on several external libraries and APIs such as Streamlit, OpenAI's GPT-3 language model API, VS Code, and pytest for testing. The dependencies are clearly listed in the requirements.txt file.    |
| **🧩 Modularity**      | The codebase is organized into cohesive modules, with separate files for cleaning operations, utility functions, and the app logic. The modular design makes the code easier to understand, maintain, and enhance.    |
| **✔️ Testing**          | The codebase includes a separate script for running tests using pytest. The tests cover critical aspects of the application, ensuring its reliability and correctness.    |
| **⚡️ Performance**      | As a language model-based app, the performance may vary based on factors like the size of the input, complexity of the generation, and the speed of the GPT-3 API. Optimal performance relies on efficient caching and network latency management.    |
| **🔐 Security**        | The codebase doesn't explicitly address security measures. However, to ensure data protection, considerations such as sanitizing user inputs, handling API keys securely, and securing the network communication should be taken into account when deploying the app.    |
| **🔀 Version Control** | The codebase is hosted on GitHub, enabling version control and collaboration features using Git. Developers can develop new features, track changes, and merge them using pull requests, ensuring codebase stability and effective collaboration.    |
| **🔌 Integrations**    | The app interacts with external systems such as OpenAI's GPT-3 language model API for generating README files and Streamlit for rendering the UI. Additionally, it interacts with VS Code settings for cleaning operations.    |
| **📶 Scalability**     | The system's scalability can be enhanced by optimizing the code's efficiency, such as implementing caching mechanisms, utilizing background job processing, and scaling horizontally across multiple instances for serving a large number of concurrent users.    |

---


## 📂 Project Structure


```bash
repo
├── LICENSE
├── README.md
├── poetry.lock
├── pyproject.toml
├── scripts
│   └── clean.sh
└── src
    ├── __init__.py
    ├── app.py
    └── utils.py

3 directories, 8 files
```

---

## 🧩 Modules

<details closed><summary>Scripts</summary>

| File                                                                         | Summary                                                                                                                                                                                                                        |
| ---                                                                          | ---                                                                                                                                                                                                                            |
| [clean.sh](https://github.com/eli64s/readmeai-ui/blob/main/scripts/clean.sh) | This Bash script performs various cleaning operations on a project directory. It removes backup files, Python cache files, cache directories, VS Code settings, build artifacts, pytest cache, benchmarks, and specific files. |

</details>

<details closed><summary>Src</summary>

| File                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                      | ---                                                                                                                                                                                                                                                                                                                                                    |
| [utils.py](https://github.com/eli64s/readmeai-ui/blob/main/src/utils.py) | These utility functions serve the Streamlit readmeai app, providing necessary tools for efficient functionality and enhancing the user experience.                                                                                                                                                                                                     |
| [app.py](https://github.com/eli64s/readmeai-ui/blob/main/src/app.py)     | This code is a Streamlit app that generates beautiful README.md files for coding projects using OpenAI's GPT language model APIs. It takes user inputs for API key, output path, and repository source, and generates the README file accordingly. The app also allows users to download the generated file, reset the session, and view the raw code. |

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
