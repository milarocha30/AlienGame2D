from abc import ABC, abstractmethod

class Desconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass

class Normal(Desconto):
    def calcular(self, valor):
        return valor * 0.1

class Vip(Desconto):
    def calcular(self, valor):
        return valor * 0.2

class Premium(Desconto):
    def calcular(self, valor):
        return valor * 0.3 

def main():
    valor = 100

    normal = Normal()
    vip = Vip()
    premium = Premium()

    print(f"Desconto normal: R$ {normal.calcular(valor):.2f}")
    print(f"Desconto vip: R$ {vip.calcular(valor):.2f}")
    print(f"Desconto premium: R$ {premium.calcular(valor):.2f}")
