from abc import ABC, abstractmethod
from core.domain.entity.joke import Joke

class GetJokeDefinition(ABC): 
    @abstractmethod
    def get_product() -> Joke:
        pass