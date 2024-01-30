from typing import Dict, Set, Tuple


#: Primary Key type, unique per given world model
PkId = int


def pk_id_generator(start: PkId = 0):
    """Simple generator for creating IDs"""
    i = start
    while True:
        yield i
        i = i + 1


class IndexableObject:
    """Represents any indexable object in a model"""
    def __init__(self, pk_id: PkId):
        self._pk_id = pk_id

    @property
    def pk_id(self) -> PkId:
        """Return ID for this object, unique for a given world model"""
        return self._pk_id


class GlobalIndex:
    """Manages all indexable information in a model"""
    def __init__(self, start: PkId = 0):
        self._index: Dict[PkId, IndexableObject] = {}
        self._class_index: Set[Tuple[PkId, str]] = set()
        self._generator = pk_id_generator(start)

    @property
    def generator(self):
        return self._generator

    def add_object(self, obj: IndexableObject, cls: type):
        """Add object for given class to index"""
        pk_id = obj.pk_id
        if pk_id is None:
            raise ValueError("Cannot index object with no id")

        if pk_id in self._index:
            raise ValueError("Object already indexed")

        self._index[pk_id] = obj
        self._class_index.add((pk_id, cls.__name__))

    def has_object(self, pk_id: PkId, cls: type) -> bool:
        """Return true iff object with given ID exists"""
        return (
            pk_id in self._index
            and (pk_id, cls.__name__) in self._class_index
        )

    def get_object(self, pk_id: PkId, cls: type) -> IndexableObject:
        """Get object by ID"""
        if self.has_object(pk_id, cls):
            return self._index[pk_id]
        raise KeyError(f"No object for {pk_id} available")
