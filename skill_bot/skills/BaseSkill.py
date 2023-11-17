from typing import NamedTuple
from collections import namedtuple


class BaseSkill:
    def __init__(self, output_fields: [str], name: str | None):
        self.name = name or self.__class__.__name__
        self._output_fields = output_fields
        self._output_class = namedtuple(f'{name}_output', output_fields)

    def __call__(self, *args, **kwargs) -> NamedTuple:
        raise NotImplementedError
