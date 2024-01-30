import abc
from typing import List

from wtp import agent_def
from wtp import common
from wtp import entity_def


class BaseWorldModel(abc.ABC):
    """Base class for a world model"""
    def __init__(self):
        self._index = common.GlobalIndex()

        #: List of agents
        self._agents: List[agent_def.BaseAgent] = []

        #:  List of entities
        self._entities: List[entity_def.BaseEntity] = []

    @property
    def pk_id_generator(self):
        """Return unique ID generator"""
        return self._index.generator

    def add_agent(self, agent: agent_def.BaseAgent):
        """Add an agent to this world model"""
        self._index.add_object(agent, agent_def.BaseAgent)
        self._agents.append(agent)

    def add_entity(self, entity: entity_def.BaseEntity):
        """Add an entity to this world model"""
        self._index.add_object(entity, entity_def.BaseEntity)
        self._entities.append(entity)
