import random
from .models import PlacaMae 
from produto.factories import ProdutoFactory
from processador.factories import ProcessadorFactory
from processador.models import Processador
 
from model_mommy import mommy

class PlacaMaeFactory():
    def create_placa_mae(self):
        processadores =  Processador.objects.all()
        if not processadores.first():
            ProcessadorFactory().create_processador()
        placa_mae = mommy.make(
            PlacaMae,
            processador=[random.choice(processadores)],
            qtd_memoria_ram_slots=random.choices([2,4])[0],
            qtd_memoria_ram_total=random.choices([16,64])[0],
            produto=ProdutoFactory().create_produto(),
            )
        return placa_mae
