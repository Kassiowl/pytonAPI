

from core.domain.entity.product import Product
from core.domain.repositories.save_product import SaveProductDefinition

class SaveProduct():
    def __init__(self, save_product_impl: SaveProductDefinition):
        self.save_product_impl = save_product_impl
    
    def run(self, product: Product):
        return self.save_product_impl.save_product()