from skill_bot.skills.base_skill import BaseSkill


class YandexGPTSummarizeSkill(BaseSkill):
    """Yandex GPT-3 Summarization skill"""

    def __init__(self, iam_token: str | None = None, folder_id: str | None = None):
        self.iam_token = iam_token
        self.folder_id = folder_id
        super().__init__(['text'], 'YandexGPT')

    def __call__(self, text: str):
        """Summarize text using Yandex GPT-3 Summarization skill
        :param text: text to summarize
        :output: namedtuple with field 'text' containing the summary
        """
        prompt = 'Суммаризируй этот текст'
        return self._output_class(text=prompt)
