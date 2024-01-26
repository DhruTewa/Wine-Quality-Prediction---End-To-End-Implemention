from Wine_Quality_Prediction_Project import logger
from Wine_Quality_Prediction_Project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Wine_Quality_Prediction_Project.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
STAGE_NAME = "Data Ingestion stage"

try:
        logger.info(f"Running {STAGE_NAME}!")
        pipeline = DataIngestionTrainingPipeline()
        pipeline.main()
        logger.info(f"Finished {STAGE_NAME}!")
        
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataValidationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
