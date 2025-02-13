from CNNClassifier import logger
from CNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f'>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<')
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>>>>>> stage {STAGE_NAME} finished <<<<<<<<<\n\n')

except Exception as e:
    raise e 