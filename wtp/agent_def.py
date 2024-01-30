import abc
from typing import List

from wtp import action_def
from wtp import common


class BaseAgent(common.IndexableObject, metaclass=abc.ABCMeta):
    """Base class for an agent"""
    def __init__(self, pkid: common.PkId):
        super().__init__(pkid)

        self._actions: List[action_def.BaseAction] = []

    def add_action(
            self,
            action: action_def.BaseAction,
            index: common.GlobalIndex
    ):
        """Add an executable action for this agent"""
        index.add_object(action, action_def.BaseAction)
        self._actions.append(action)
