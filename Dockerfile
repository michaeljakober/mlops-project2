FROM python:3.10-slim


RUN pip install wandb torch pytorch_lightning==1.9.5 datasets transformers scipy scikit-learn

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run the script with the hyperparameters
CMD ["python", "main.py", "--lr", "2e-5", "--wd", "1e-2", "--warmup-steps", "100"]