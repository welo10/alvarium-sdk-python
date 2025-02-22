from abc import ABC, abstractmethod

from alvarium.contracts.annotation import Annotation
from alvarium.utils import PropertyBag

class Annotator(ABC):
    """A unit responsible for annontating raw data and producing an Annotation object"""

    @abstractmethod
    def execute(self, data:bytes, ctx: PropertyBag = None) -> Annotation:
        pass