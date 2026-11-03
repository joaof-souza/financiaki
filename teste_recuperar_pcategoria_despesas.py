from src.model.despesa_model import Despesas

resultado = Despesas().recuperar_por_categoria('neymar', 5)
print(resultado)