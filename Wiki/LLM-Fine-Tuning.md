LLM Fine-Tuning is the process of adapting a pre-trained Large Language Model to a specific dataset or task, significantly improving its performance on niche requirements. This guide covers practical workflows for fine-tuning models like [[Gemma-4]] using cloud-based tools like Unsloth on Google Colab or local hardware via PEFT (Parameter-Efficient Fine-Tuning). By utilizing techniques like LoRA (Low-Rank Adaptation) and [[Quantization]], developers can refine models on consumer-grade hardware, including Apple Silicon (MPS) and NVIDIA GPUs (CUDA), to create specialized assistants or reasoning engines.

# LLM Fine-Tuning Guide

## Overview
A practical guide to fine-tuning LLMs (TinyLlama-1.1B & Llama-3.1-8B) using two distinct approaches:
1. **Fast cloud training:** Using Unsloth on Google Colab.
2. **Local adaptation:** On Mac (MPS) & Windows/Linux (CUDA) using PEFT.

## Tech Stack
- **IDE:** Visual Studio Code
- **Language:** Python 3.10+
- **Frameworks:** PyTorch 2.0, Transformers, TRL, PEFT, LoRA

## Key Features
- **Workflows:** Ready-to-use notebooks for Google Colab, macOS, and Windows/Linux.
- **Dataset:** Ready-to-use basketball dataset included in the `data/` folder.
- **Training Setups:**
    - Unsloth on Colab
    - Hugging Face's SFTTrainer on macOS (Apple Silicon)
    - Windows/Linux (CUDA)
- **Logging:** Accelerator, bitsandbytes, and safetensors for efficient experimentation.

## Project Structure
```
data/                # Supervised fine-tuning corpora (JSON + raw text)
google_colab/
  fine-tuning.ipynb  # Colab workflow (setup + training + evaluation)
imgs/                # Notebook figures and configuration screenshots
mac/
  fine-tuning.ipynb  # Local M-series workflow with Accelerate + LoRA
  requirements.txt   # Exact Python dependencies for local runs
windows-linux/
  fine-tuning.ipynb  # Local Windows/Linux workflow with PEFT + CUDA
  requirements.txt   # Exact Python dependencies for local runs
README.md            # You are here
```

## Quick Start Options

### Option A: Google Colab (Cloud GPU)
- Open `google_colab/fine-tuning.ipynb` and connect to a T4 GPU or better.
- Run setup cells for Transformers, TRL, PEFT, bitsandbytes, and Unsloth.
- Load datasets directly from `data/`.

### Option B: Local macOS (Apple Silicon or CPU)
1. Create and activate a Python 3.10+ environment (uv, conda, or venv).
2. Install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r mac/requirements.txt
   ```
3. Launch `mac/fine-tuning.ipynb` and run cells sequentially.

### Option C: Local Windows/Linux (CUDA GPU or CPU)
1. Create and activate a Python 3.10+ environment.
2. Install dependencies:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r windows-linux/requirements.txt
   ```
3. Ensure CUDA drivers are installed and a compatible GPU is available.
4. Open `windows-linux/fine-tuning.ipynb` in VS Code or Jupyter.

## Data Expectations
- **Raw Text:** Paragraphs separated by blank lines in `data/data.txt`.
- **Supervised Pairs:** JSON schema in `data/atomic_train.json`:
  ```json
  {
    "question": "What type of sport is basketball?",
    "answer": "Basketball is a team sport played on a rectangular court."
  }
  ```
