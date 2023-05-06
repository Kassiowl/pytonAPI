from abc import ABC, abstractmethod
from core.domain.entity.product import Product


class GetProductDefinition(ABC): 
    @abstractmethod
    def get_product() -> Product:
        pass
    @abstractmethod
    def get_average_price() -> float:
        pass