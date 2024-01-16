from time import sleep

from prefect import flow, task


@flow
def print_hi_name(name: str):
    print(f"HIIII {name}")


@flow
def one_time_analysis(study_name: str):
    print(f"Running a one-time analysis of use case: {study_name}")


@task
def train_model(study_name: str):
    print(f"Training model for study {study_name}")
    sleep(5)
    print(f"Trained!")


@task
def validate_model(study_name: str):
    print(f"Validating model for study {study_name}")
    sleep(2)
    print(f"Validated!")


@flow
def train_and_validate_model(study_name: str):
    """Training pipeline

    Args:
        study_name (str): _description_
    """
    train_model(study_name=study_name)
    validate_model(study_name=study_name)


@flow
def infer(study_name: str):
    print(f"Peforming inference for study {study_name}")
