
from cnnClassifier import logger

from cnnClassifier.pipeline.stage_01_data_pipeline import DataIngestionTrainingPipeline


STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<<\n\n<=========x')
except Exception as e:
    raise e