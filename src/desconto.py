from abc import ABC, abstractmethod

class IDesconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass

class ICupom:
    def aplicar_cupom(self, codigo):
        raise NotImplementedError
    
class IVIP:
    def validar_usuario_vip(self, usuario):
        raise NotImplementedError


class Normal(IDesconto):
    def calcular(self, valor):
        return valor * 0.1

class Vip(IDesconto, ICupom, IVIP):
    def calcular(self, valor):
        return valor * 0.2
    
    def aplicar_cupom(self, valor):
        return True
    
    def validar_usuario_vip(self, usuario):
        return usuario == "vip"

class Premium(IDesconto):
    def calcular(self, valor):
        return valor * 0.3 

class Pedido:
    def __init__(self, desconto: IDesconto):
        self.desconto = desconto
    def total(self, valor):
        return valor - self.desconto.calcular(valor)


def aplicar_desconto(desconto: IDesconto, valor : float) -> float:  
    return desconto.calcular(valor)

def aplicar_cupom(cupom: ICupom, codigo : str) -> bool:
    return cupom.aplicar_cupom(codigo)


if __name__ == "__main__":
    valor = 100
   
    pedido_normal = Pedido(Normal())
    pedido_vip = Vip()
   
    print("Normal: ", pedido_normal.total(valor))
    print("Vip: ", pedido_vip.total(valor))
