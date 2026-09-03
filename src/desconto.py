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

def aplicar_desconto(desconto: IDesconto, valor : float) -> float:  
    return desconto.calcular(valor)

def aplicar_cupom(cupom: ICupom, codigo : str) -> bool:
    return cupom.aplicar_cupom(codigo)

def main():
    valor = 100

    normal = Normal()
    vip = Vip()

    print(f"Desconto normal: R$ {aplicar_desconto(normal, valor):.2f}")
    print(f"Desconto vip: R$ {aplicar_desconto(vip, valor):.2f}")
    print("Cupom VIP:", aplicar_cupom(vip, "DESC10"))    # porque recebe vip nessa função??

if __name__ == "__main__":
    main()
