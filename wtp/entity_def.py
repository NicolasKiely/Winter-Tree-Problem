import abc

from wtp import common


class BaseEntity(common.IndexableObject, metaclass=abc.ABCMeta):
    """Base class for an entity"""
