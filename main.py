from Wine_Quality_Prediction_Project import logger
from Wine_Quality_Prediction_Project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline  

STAGE_NAME = "Data Ingestion stage"

try:
        logger.info(f"Running {STAGE_NAME}!")
        pipeline = DataIngestionTrainingPipeline()
        pipeline.main()
        logger.info(f"Finished {STAGE_NAME}!")
        
except Exception as e:
        logger.exception(e)
        raise e
