from CNNClassifier import logger
from CNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from CNNClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from CNNClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline

STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f'**********************')
    logger.info(f'>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<')
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>>>>>> stage {STAGE_NAME} finished <<<<<<<<<\n\n')

except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME = 'Prepare Base Model Stage'
try:
    logger.info(f'**********************')
    logger.info(f'>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<')
    data_ingestion = PrepareBaseModelPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>>>>>> stage {STAGE_NAME} finished <<<<<<<<<\n\n')

except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME = 'Training Stage'
try:
    logger.info(f'**********************')
    logger.info(f'>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<')
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f'>>>>>>>>>> stage {STAGE_NAME} finished <<<<<<<<<\n\n')

except Exception as e:
    logger.exception(e)
    raise e 