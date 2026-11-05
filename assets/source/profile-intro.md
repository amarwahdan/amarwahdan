<!-- Source-controlled profile. Rebuild with: python3 tools/build_readme.py -->
<div align="center">
  <img src="./assets/header.svg" width="100%" alt="Amar Ahmed Hamed — AI Engineer / Machine Learning Engineer. Agentic workflows, visual intelligence, and model-based planning." />
</div>

<div align="center">
  <a href="https://www.linkedin.com/in/amar-ahmed-hamed-25b676302"><img src="https://img.shields.io/badge/LinkedIn-CONNECT-43E8E1?style=for-the-badge&labelColor=101B2D" alt="Connect on LinkedIn" /></a>
  <a href="https://www.kaggle.com/amarahmedhamed"><img src="https://img.shields.io/badge/Kaggle-RESEARCH-6FB8FF?style=for-the-badge&labelColor=101B2D&logo=kaggle&logoColor=6FB8FF" alt="Explore my Kaggle profile" /></a>
  <a href="mailto:aammaarrah10@gmail.com"><img src="https://img.shields.io/badge/Email-LET'S_TALK-A78BFA?style=for-the-badge&labelColor=101B2D" alt="Email Amar" /></a>
</div>

<p align="center">
  <a href="#system-profile">System Profile</a> &nbsp; / &nbsp;
  <a href="#tech-stack">Tech Stack</a> &nbsp; / &nbsp;
  <a href="#featured-projects">Featured Projects</a> &nbsp; / &nbsp;
  <a href="#research-and-recognition">Research & Recognition</a> &nbsp; / &nbsp;
  <a href="#connect">Connect</a>
</p>

## System Profile

I'm **Amar Ahmed Hamed**, an **AI Engineer / Machine Learning Engineer** based in Cairo, Egypt. I work across agentic AI, computer vision, NLP, and model-based reinforcement learning—with a particular interest in systems whose decisions can be inspected, not just displayed.

My portfolio connects **autonomous tool orchestration**, **multimodal medical safety**, **predictive vision research**, **tactical feature engineering**, and **source-aware RAG**. The common thread is the engineering around the model: what it sees, what it retrieves, which tools it calls, how state is preserved, and what evidence supports its output.

```yaml
identity:
  name: Amar Ahmed Hamed
  role: AI Engineer / Machine Learning Engineer
  location: Cairo, Egypt

engineering_focus:
  agents: orchestration, tool calling, evidence, sandbox boundaries
  perception: computer vision, multimodal evidence extraction
  planning: state estimation, world models, Monte Carlo Tree Search
  language: NLP, retrieval-augmented generation, LLM adaptation
  analytics: feature engineering, team-shape dynamics, sequence intelligence
```

**Portfolio signals:** a **49-feature / 9-cluster** tactical framework; **15 regression checks** around a medical-safety agent; and an authored **vision-based RL research paper**. The project cards below distinguish experimental results from test coverage and dataset scope.

## Tech Stack

### An AI capability pipeline—not an icon wall

<a href="./docs/tech-stack.md"><img src="./assets/tech-pipeline.svg" width="100%" alt="AI capability pipeline: signals and data → representation → training or retrieval/orchestration → inference → validation and inspection." /></a>

The graph maps my documented tools and areas of work. It is a capability map, not a claim that every project uses every component. **Open a stage to inspect the engineering role of the tools.**

<details>
<summary><b>01 / Signals — acquire, clean, and understand the data</b></summary>

**Python, SQL / MySQL, NumPy, and pandas** support data preparation, exploratory analysis, and feature construction. **Matplotlib and Seaborn** make data quality and behavior visible. My PathLine training included imbalance handling, outliers, skewness, and feature engineering.

The relevant engineering question is not only “Can I load the data?” but “What does a row represent, what is repeated, and what will an aggregation accidentally count twice?” That distinction matters in the Tactical Intelligence Framework.

[![NumPy upstream release](https://img.shields.io/pypi/v/numpy?label=NumPy%20upstream&color=43E8E1&labelColor=101B2D)](https://pypi.org/project/numpy/)
[![pandas upstream release](https://img.shields.io/pypi/v/pandas?label=pandas%20upstream&color=43E8E1&labelColor=101B2D)](https://pypi.org/project/pandas/)

</details>

<details>
<summary><b>02 / Representation — convert pixels and text into useful signals</b></summary>

**OpenCV and vision transformers** cover visual preprocessing and representation. **spaCy, NLTK, and Gensim** belong to my NLP toolkit; **TF-IDF and dense embeddings** provide different representations for different retrieval and classification problems.

In QORAbot, normalized **MPNet embeddings** feed FAISS retrieval. In the custom sentiment classifier, sparse unigram/bigram features feed Naive Bayes. In Health Guardian, image evidence is recorded separately from the model's interpretation.

[![Transformers upstream release](https://img.shields.io/pypi/v/transformers?label=Transformers%20upstream&color=6FB8FF&labelColor=101B2D)](https://pypi.org/project/transformers/)

</details>

<details>
<summary><b>03A / Learning and adaptation — fit, estimate, and plan</b></summary>

**PyTorch, TensorFlow / Keras, and scikit-learn** support model development. My research interests include **model-based RL, learned dynamics, Kalman filtering, and MCTS**. My documented LLM-adaptation skill set includes **LoRA / QLoRA** and parameter-efficient fine-tuning.

**Quantization** and low-rank adaptation are distinct parts of the efficiency discussion; neither implies a measured latency improvement without a hardware-specific evaluation. The profile does not assign a quantization benchmark to a project that has not published one.

[![PyTorch upstream release](https://img.shields.io/pypi/v/torch?label=PyTorch%20upstream&color=A78BFA&labelColor=101B2D)](https://pypi.org/project/torch/)
[![scikit-learn upstream release](https://img.shields.io/pypi/v/scikit-learn?label=scikit--learn%20upstream&color=A78BFA&labelColor=101B2D)](https://pypi.org/project/scikit-learn/)

</details>

<details>
<summary><b>03B / Agentic reasoning — retrieve, coordinate, and call tools</b></summary>

**LangChain, CrewAI, and Google ADK** are part of my agentic toolkit. **RAG, source metadata, tool schemas, and structured outputs** connect generation to external evidence rather than treating an LLM response as ground truth.

Mooox-Agent emphasizes recursive agent coordination and state continuity. Health Guardian emphasizes function-call normalization and deterministic safeguards. QORAbot emphasizes retrieval and source provenance. These are different engineering contracts—not interchangeable “chatbot” implementations.

[![LangChain upstream release](https://img.shields.io/pypi/v/langchain?label=LangChain%20upstream&color=43E8E1&labelColor=101B2D)](https://pypi.org/project/langchain/)

</details>

<details>
<summary><b>04 / Inference and execution — connect models to usable systems</b></summary>

**LiteLLM and Ollama** support provider abstraction and local-model workflows in the documented security-agent stack. **Gradio** exposes interactive model interfaces; **Docker** isolates execution. **C / C++** and Linux are part of my broader programming/tooling background.

Inference is more than a model invocation: the input contract, loaded artifacts, tool environment, output schema, and state-handling behavior all affect whether a system is usable. **Latency and throughput should be measured**, not inferred from a demo or an animated dashboard.

[![Gradio upstream release](https://img.shields.io/pypi/v/gradio?label=Gradio%20upstream&color=F5C76B&labelColor=101B2D)](https://pypi.org/project/gradio/)

</details>

<details>
<summary><b>05 / Evidence and observability — validate before asserting</b></summary>

**Pytest, Pydantic contracts, OpenTelemetry, and explicit audit trails** make failures and outputs inspectable. My project documentation also includes **Poetry**, **Git / GitHub**, and **PostHog** in the engineering toolchain.

I separate regression coverage from model quality, corpus size from training size, and public-leaderboard placement from final ranking. The portfolio uses existing artifacts and clearly scoped results rather than invented benchmark percentages.

[![Pytest upstream release](https://img.shields.io/pypi/v/pytest?label=Pytest%20upstream&color=59E3B4&labelColor=101B2D)](https://pypi.org/project/pytest/)

</details>

<sub>Release badges query current upstream package versions; they are not my pinned dependency versions or proof of deployment. SVG motion illustrates data flow—it is not live inference telemetry.</sub>

## Featured Projects

### Inspect the systems behind the outputs

Each model card is clickable. Open its engineering brief for the idea, challenge, numeric evidence, technologies, and limitations; follow **Architecture Spec** for the deeper data-flow diagram and original artifacts. Repository-update badges use GitHub data, while notebook and video links are labeled according to what they actually open.

<p align="center">
  <a href="#mooox-agent">Agentic Security</a> &nbsp; / &nbsp;
  <a href="#health-guardian">Medical Safety</a> &nbsp; / &nbsp;
  <a href="#amarzero">Vision + RL</a> &nbsp; / &nbsp;
  <a href="#tactical-intelligence-framework">Tactical Intelligence</a> &nbsp; / &nbsp;
  <a href="#qorabot">Scientific RAG</a> &nbsp; / &nbsp;
  <a href="#sentiment-analysis-app">Applied NLP</a>
</p>

