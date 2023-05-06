from core.infraestructure.get_product_impl import GetProductImpl

from core.application.use_cases.get_product import GetProduct
from core.application.use_cases.get_average_price import GetAveragePrice


get_product_impl = GetProductImpl()

get_product_use_case = GetProduct(get_product_impl)
get_average_price_use_case = GetAveragePrice(get_product_impl)

all_products = get_product_use_case.run()
average_price = get_average_price_use_case.run()

print(all_products)

print("Preço médio dos smartphones: $",average_price)