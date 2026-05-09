#!/bin/bash

# ==============================================================================
# SLURM RESOURCE REQUESTS
# These lines (prefixed with #SBATCH) tell the cluster what hardware you need.
# ==============================================================================

# A descriptive name for your job in the queue (visible via 'squeue -u [YOUR_USERNAME]')
#SBATCH --job-name="granite_run"

# Maximum wall-clock time (Hours:Minutes:Seconds). 
# Your job will be terminated if it exceeds this.
#SBATCH --time=02:00:00

# This requests 2x NVIDIA A100 GPUs.
#SBATCH --gres=gpu:a100:2 

# Specifies the queue/partition. 'gpu' is standard for AI tasks.
#SBATCH --partition=gpu

# CPU RAM request to load the model weights into memory before they are transferred to the GPUs.
#SBATCH --mem=240G

# Where the console output (also errors) will be saved. 
# %j is a placeholder that SLURM replaces with the unique Job ID.
#SBATCH --output=/scratch/n/narges/logs/granite_%j.log
#SBATCH --error=/scratch/n/narges/logs/granite_%j.err


# ==============================================================================
# 1. ENVIRONMENT SETUP
# ==============================================================================

# Clears any modules loaded by default on the login node to prevent conflicts.
module purge 

# Loads the specific Python version. GCCcore indicates the compiler used to build it.
# search available Python versions in the HPC doc.
module load lang/Python/3.10.4-GCCcore-11.3.0

# Loads the CUDA toolkit (Compiler and Libraries). 
# This is essential for PyTorch to communicate with the A100 GPUs.
# search the available CUDA versions in the HPC doc.
module load system/CUDA/12.4.0

# Activates your pre-built Virtual Environment.
# Remember: Always build your venv on the login node BEFORE submitting this script.
source /pc2/users/n/narges/dsse/dsse-assigment-1/narges/W2/slurm_sample/.venv/bin/activate


# ==============================================================================
# 2. OPTIMIZATIONS & SECRETS
# ==============================================================================

# Hugging Face cache: use cluster scratch (large quota). $HOME is often small/full on /pc2/users.
export HF_HOME="${HOME}/scratch/huggingface_cache"
mkdir -p "$HF_HOME"

# Memory optimization for PyTorch. 
# 'expandable_segments' helps prevent "Out of Memory" (OOM) errors by managing 
# how the GPU memory is allocated more efficiently.
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

# Your Hugging Face Access Token. 
# Required for downloading models.
#export HF_TOKEN="[UR_HUGGING_FACE_TOKEN]"


# ==============================================================================
# 3. EXECUTION
# ==============================================================================

echo "Starting..."

# Run from the directory you submitted in (so results/ and imports resolve).
cd "${SLURM_SUBMIT_DIR:-.}"

# One process: load model once, run all prompting techniques, save under results/job_<JOBID>/
python run_all_techniques.py

# --- IMPORTANT ---
# Submitting: Run 'sbatch sample.sh' to put this in the queue.
# Checking Job Details: Run 'scontrol show job [JOBID]'
# Checking Job Start Time: Run 'scontrol show job [JOBID] | grep StartTime'
# Checking Progress: Run 'tail -f [UR_LOG_FILE_NAME]_[JOBID].log' to watch the log file in real-time.
# Cancel a Job: If you see an error in the log, run 'scancel [JOBID]' immediately to free up the GPUs.
