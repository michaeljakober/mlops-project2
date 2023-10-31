import json

import torch
import wandb
import pytorch_lightning.loggers
from pytorch_lightning.callbacks import LearningRateMonitor
from pytorch_lightning import Trainer, seed_everything

from model import GLUEDataModule, GLUETransformer


def train(learning_rate, weight_decay, warmup_steps):
    # Logger
    with open("./config/config.json", "r") as jsonfile:
        data = json.load(jsonfile)
        subscription_key = data['wandb']['subscription_key']

    wandb.login(key=subscription_key)

    wandb_logger = pytorch_lightning.loggers.WandbLogger(project="mlops-project2")

    seed_everything(42)
    dm = GLUEDataModule(
        model_name_or_path="distilbert-base-uncased",
        task_name="mrpc",
    )
    dm.setup("fit")
    model = GLUETransformer(
        model_name_or_path="distilbert-base-uncased",
        num_labels=dm.num_labels,
        eval_splits=dm.eval_splits,
        task_name=dm.task_name,
        learning_rate=learning_rate,
        weight_decay=weight_decay,
        warmup_steps=warmup_steps,
        adam_epsilon=1e-8,
        train_batch_size=128,
        eval_batch_size=128,
    )

    lr_monitor = LearningRateMonitor(logging_interval='step')

    trainer = Trainer(
        logger=wandb_logger,
        max_epochs=3,
        accelerator="auto",
        devices=1 if torch.cuda.is_available() else None,
        callbacks=[lr_monitor]
    )
    trainer.fit(model, datamodule=dm)

    wandb.finish()
