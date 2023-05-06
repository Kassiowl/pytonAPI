from abc import ABC, abstractmethod


class SaveProductDefinition(ABC): 
    @abstractmethod
    def save_product() -> bool:
        pass
