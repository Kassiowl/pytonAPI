from dataclasses import dataclass


@dataclass
class Product:
    id: int
    category: str
    price: float
    title: str
  
    
    