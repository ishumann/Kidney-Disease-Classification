
from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_pipeline import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline 
from cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline


STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f"\n\n>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<\n\n")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(
        f'\n\n>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<<\n\n<=========x')
except Exception as e:
    raise e


STAGE_NAME = "Prepare base model"
try:
   logger.info(f"*******************")
   logger.info(f"\n\n>>>>>> stage {STAGE_NAME} started <<<<<<\n\n")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(
       f"\n\n>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training"


try:
    logger.info(f"*******************")
    logger.info(f"\n\n>>>>>> stage {STAGE_NAME} started <<<<<<\n\n")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(
        f"\n\n>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Evaluation stage" 
try:
   logger.info(f"*******************")
   logger.info(f"\n\n>>>>>> stage {STAGE_NAME} started <<<<<<\n\n")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(
       f"\n\n>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e
