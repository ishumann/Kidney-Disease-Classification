# Kidney-Disease-Classification-MLflow-DVC


## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py



## How to run?

### STEP 01: Clone the repository

```bash
https://github.com/ishumann/Kidney-Disease-Classification
```
### STEP 02: Create a conda environment after opening the repository

```bash
conda create -n kidney python=3.8 -y
```
```bash
conda activate kidney
```

### OR

### STEP 02: Create a conda Virtual environment (venv) after opening the repository

```bash
conda create -p kidney python=3.8 -y
```



### STEP 03: install the requirements

```bash
pip install -r requirements.txt
```


## Perform MLOps

### STEP 01: MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)


```bash
mlflow ui
```
### STEP 02:  Dagshub
[dagshub](https://dagshub.com/)
```

export MLFLOW_TRACKING_URI=https://dagshub.com/ishumann/Kidney-Disease-Classification.mlflow
export MLFLOW_TRACKING_USERNAME=ishumann
export  MLFLOW_TRACKING_PASSWORD=15495e98cd344df629c4d470b95d7bac88585699
python script.py \
```




> note: this credintials are not real. Create your own account and get the credintials from dagshub.


### STEP 03: Run this to export as env variables.

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/ishumann/Kidney-Disease-Classification.mlflow

export MLFLOW_TRACKING_USERNAME=ishumannnn

export MLFLOW_TRACKING_PASSWORD=756f1a4bbd0ec7f0738d710bb309a2e89d0b11cf 
```

