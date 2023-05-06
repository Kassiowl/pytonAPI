from core.application.use_cases.get_joke import GetJoke
from core.infraestructure.get_joke_impl import GetJokeImpl
from core.infraestructure.get_product_impl import GetProductImpl

from core.application.use_cases.get_product import GetProduct
from core.application.use_cases.get_average_price import GetAveragePrice


get_product_impl = GetProductImpl()

get_product_use_case = GetProduct(get_product_impl)
get_average_price_use_case = GetAveragePrice(get_product_impl)

all_products = get_product_use_case.run()
average_price = get_average_price_use_case.run()


get_joke_impl = GetJokeImpl()
get_joke_use_case = GetJoke(get_joke_impl)
chuck_norris_joke = get_joke_use_case.run()


print("## Resultado da coleta de dados ##")
print("Preço médio dos smartphones: $",average_price)

print("_______________________________________")
print("Chuck Norris")
print(chuck_norris_joke.value)