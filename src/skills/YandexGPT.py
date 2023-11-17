from src.skills.BaseSkill import BaseSkill


class YandexGPTSummarizeSkill(BaseSkill):
    def __init__(self):
        super().__init__(['text'], 'YandexGPT')

    def __call__(self, *args, **kwargs):
        raise NotImplementedError