from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.model_evaluation import Evaluation
from CNNClassifier import logger

STAGE_NAME = 'Evaluation Stage'

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()

        

if __name__ == '__main__':
    try:
        logger.info(f'>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<')
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f'>>>>>>>>>> stage {STAGE_NAME} finished <<<<<<<<<')

    except Exception as e:
        raise e 
