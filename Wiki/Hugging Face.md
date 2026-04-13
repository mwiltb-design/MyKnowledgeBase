Source: [[Fine_tune_VLM.md]], [[Gemma 4.md]]

## Summary
- **Hugging Face** is the leading model repository and ecosystem for open-weights and proprietary AI.
- **Hugging Face Hub:** A centralized location for storing and sharing **model.safetensors**, config files, and datasets.
- **Spaces:** An interactive demo hosting platform using **Gradio** or Streamlit.

## Core Features
- **Datasets:** A standard data layer for machine learning (e.g., **FoodExtract-1k-Vision**).
- **Inference API:** Scalable hosting for server-side model execution.
- **Version Control:** Uses **Git-LFS** and **Zet Z** (efficient data layer) for model weight management.

## Workflows
1. **Upload Folder:** `API.upload_folder(repo_id, folder_path)` to commit models.
2. **Space Creation:** Deploying an `app.py` with the Gradio SDK to create live, interactable demos.

---
**See also:** [[VLM]], [[SmolVLM2]], [[HuggingFaceHub]].
