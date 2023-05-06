from abc import ABC, abstractmethod
from core.domain.entity.product import Product


class GetProductInterface(ABC): 
    @abstractmethod
    def get_product() -> Product:
        pass