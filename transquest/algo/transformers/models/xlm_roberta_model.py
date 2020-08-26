
from transformers.configuration_xlm_roberta import XLMRobertaConfig
from transformers.modeling_xlm_roberta import XLM_ROBERTA_PRETRAINED_MODEL_ARCHIVE_LIST

from transquest.algo.transformers.models.roberta_model import RobertaForSequenceClassification, Roberta


class XLMRobertaForSequenceClassification(RobertaForSequenceClassification):
    config_class = XLMRobertaConfig
    pretrained_model_archive_map = XLM_ROBERTA_PRETRAINED_MODEL_ARCHIVE_LIST

class XLMRobertaModel(Roberta):
    config_class = XLMRobertaConfig
    pretrained_model_archive_map = XLM_ROBERTA_PRETRAINED_MODEL_ARCHIVE_LIST



