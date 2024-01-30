import abc
from typing import List

from wtp import common


class BaseStep(common.IndexableObject, metaclass=abc.ABCMeta):
    """Base class for an action step"""


class BaseAction(common.IndexableObject, metaclass=abc.ABCMeta):
    """Base class for an action"""
    def __init__(self, pk_id: common.PkId):
        super().__init__(pk_id)

        #: Ordered list of steps
        self._steps: List[BaseStep] = []

    def add_step(
            self,
            step: BaseStep,
            index: common.GlobalIndex
    ):
        """Add a step to this action"""
        index.add_object(step, BaseStep)
        self._steps.append(step)
