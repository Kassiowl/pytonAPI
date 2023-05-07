

from core.domain.repositories.get_product import GetProductDefinition


class GetAveragePriceUseCase():
    def __init__(self, average_price_impl: GetProductDefinition):
        self.average_price_impl = average_price_impl
    
    def run(self):
        return self.average_price_impl.get_average_price()