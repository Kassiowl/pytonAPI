from core.domain.entity.product import Product
from core.domain.repositories.get_product import GetProductDefinition
import requests

class GetProductImpl(GetProductDefinition):
    def get_product(self):
        URL = 'https://dummyjson.com/products' 
        resp = requests.get(url=URL)
        data = resp.json()
        data_products = data['products']
        product_list = []
        for product in data_products:
            product_entity = Product(product['id'], product['category'], product['price'], product['title'])
            product_list.append(product_entity)
        
        self.product_list = product_list
        return product_list
    def get_average_price(self):
        total = 0
        sum = 0
        for product in self.product_list:
            if(product.category == 'smartphones'):
                total+=1
                sum += product.price
        
        return sum/total