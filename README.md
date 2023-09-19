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

This repository is a Streamlit app that generates README files for coding projects using OpenAI's GPT language model APIs. With user inputs, commands execution, and generated content previewing, it offers an efficient and seamless user experience. The app's core functionalities include integrating with GPT language model APIs, providing session reset, download options, and utility functions for a streamlined experience. This project aims to automate the process of creating high-quality README files, saving developers time and effort while ensuring beautiful and effective documentation for their projects.

---

## ⚙️ Features

| Feature                | Description                           |
| ---------------------- | ------------------------------------- |
| **⚙️ Architecture**     | The codebase follows a modular architecture with separation of concerns between the Streamlit app, utility functions, and script files. It uses a client-server architecture for generating README files and utilizes the OpenAI GPT language model APIs for content generation.    |
| **📖 Documentation**   | The codebase lacks detailed documentation. Although the filenames provide some insight into the purpose of each file, a more comprehensive overview of the functionality and usage would be beneficial for developers.    |
| **🔗 Dependencies**    | The codebase depends on several external libraries like Streamlit for the app's UI, requests for API communication, and Click for command-line interface handling. It also relies on the OpenAI GPT language model APIs for content generation.    |
| **🧩 Modularity**      | The codebase showcases a good level of modularity. The separation of the Streamlit app, utility functions, and script files into distinct modules contributes to this modularity. Moreover, these components are relatively interchangeable and can be extended or modified independently.    |
| **✔️ Testing**          | The codebase does not have specific tests in place, which is a limitation. Implementing unit tests using frameworks like pytest to validate critical sections, such as utility functions and API interactions, would increase confidence in the application's functionality.    |
| **⚡️ Performance**      | The performance of the system highly depends on the speed and efficiency of the OpenAI GPT language model API for generating README content. Other parts of the application appear to be lightweight, and the absence of complex computations suggests overall satisfactory performance.    |
| **🔐 Security**        | The codebase does not include specific measures for security. While there are no glaring security risks in the provided code, integrating security practices like input sanitization and authorization checks may enhance the system's security profile.    |
| **🔀 Version Control** | The codebase utilizes Git for version control. However, it lacks explicit information about branching, commit practices, and pull request workflows that developers follow. Establishing guidelines for version control processes would improve collaboration and ensure codebase integrity.    |
| **🔌 Integrations**    | The app interacts with the OpenAI GPT language model APIs for generating readme content. The Streamlit framework integrates with various Python ecosystem libraries, providing opportunities for additional integrations to enhance functionality or implement custom features.   |
| **📶 Scalability**     | With the use of external dependencies like Streamlit and OpenAI GPT, the codebase has the potential to scale horizontally as demand grows. Leveraging the APIs' scalability and extending functionalities using modular components, the system can handle increased users and integration requirements with ease.   |

---


## 📂 Project Structure




---

## 🧩 Modules

<details closed><summary>Scripts</summary>

| File                                                                         | Summary                                                                                                                                                                                                             |
| ---                                                                          | ---                                                                                                                                                                                                                 |
| [clean.sh](https://github.com/eli64s/readmeai-ui/blob/main/scripts/clean.sh) | This code is a bash script that removes various types of files and directories, such as backup files, cache files and directories, VS Code settings, build artifacts, pytest cache, benchmarks, and specific files. |

</details>

<details closed><summary>Src</summary>

| File                                                                     | Summary                                                                                                                                                                                                                                                                                                                         |
| ---                                                                      | ---                                                                                                                                                                                                                                                                                                                             |
| [app.py](https://github.com/eli64s/readmeai-ui/blob/main/src/app.py)     | This Streamlit app generates beautiful README files for coding projects. It collects user inputs, executes commands, displays and allows for previewing generated README content. Integration with OpenAI's GPT language model APIs powers the generation process. The app provides session reset and download functionalities. |
| [utils.py](https://github.com/eli64s/readmeai-ui/blob/main/src/utils.py) | The code consists of utility functions designed specifically for the Streamlit readmeai app. These functions facilitate the app's core functionalities, ensuring efficiency and seamless user experience.                                                                                                                       |

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
