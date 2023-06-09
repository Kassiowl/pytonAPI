from core.application.use_cases.get_joke_use_case import GetJokeUseCase
from core.application.use_cases.save_product_use_case import SaveProductUseCase
from core.infraestructure.get_joke_impl import GetJokeImpl
from core.infraestructure.get_product_impl import GetProductImpl

from core.application.use_cases.get_product_use_case import GetProductUseCase
from core.application.use_cases.get_average_price_use_case import GetAveragePriceUseCase
from core.infraestructure.save_product_impl import SaveProductImpl


get_product_impl = GetProductImpl()

get_product_use_case = GetProductUseCase(get_product_impl)
get_average_price_use_case = GetAveragePriceUseCase(get_product_impl)

all_products = get_product_use_case.run()
average_price = get_average_price_use_case.run()


get_joke_impl = GetJokeImpl()
get_joke_use_case = GetJokeUseCase(get_joke_impl)
chuck_norris_joke = get_joke_use_case.run()


save_product_impl = SaveProductImpl()
save_product_use_case = SaveProductUseCase(save_product_impl)
save_product_impl.create_table()

save_product_use_case = SaveProductUseCase(save_product_impl)
for product in all_products:
    save_product_use_case.run(product)

print("## Resultado da coleta de dados ##")
print("Preço médio dos smartphones: $",average_price)

print("_______________________________________")
print("Chuck Norris")
print(chuck_norris_joke.value)