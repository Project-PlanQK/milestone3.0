# Milestone 3.0

This milestone focuses on the development of the first functional chatbot version for the PlanQK Assistant project. It includes scripts, notebooks, and resources for building and testing the chatbot.

## Contents

- **PLANQK_service_execution.ipynb**: Jupyter notebook for executing and testing PlanQK services.
- **requirements.txt**: File listing the dependencies required for this milestone.
- **TutorPlanQK/**: Directory containing chatbot-related implementation files.
- **data/**: Directory with PlanQK documentation in PDF format for reference.
- **scripts/**: Contains `update_llamaindex.py` for updating the LlamaIndex.
- **storage/**: Directory with JSON files for vector stores, document stores, and graph stores.
- **.github/workflows/**: Contains `update_embeddings.yml` for automating embedding updates.

## Purpose

The goal of this milestone is to create a functional chatbot that integrates with PlanQK services. Key tasks include:
- Implementing and testing chatbot functionalities.
- Utilizing PlanQK documentation for training and reference.
- Automating updates to embeddings and vector stores.

## Usage

1. **Install Dependencies**:
   - Use `requirements.txt` to install the required Python packages:
     ```bash
     pip install -r requirements.txt
     ```

2. **Run the Notebook**:
   - Open `PLANQK_service_execution.ipynb` in Jupyter Notebook to test PlanQK service execution.

3. **Update LlamaIndex**:
   - Use the `scripts/update_llamaindex.py` script to update the LlamaIndex.

4. **Automate Embedding Updates**:
   - Check the `.github/workflows/update_embeddings.yml` file for GitHub Actions workflow configuration.

5. **Reference Documentation**:
   - Review the PlanQK documentation in the `data/` directory for additional context.

## Notes

- Ensure Python 3.11+ is installed.
- Use the `.env` file (if applicable) to configure API keys and other settings.
- Refer to the `storage/` directory for preprocessed vector and document stores.

---
**Built for the PlanQK Assistant Project**
