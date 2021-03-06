from rest_framework import routers
from produto.views import ProdutoViewSet
from memoria_ram.views import MemoriaRamViewSet
from placa_mae.views import PlacaMaeViewSet
from placa_video.views import PlacaVideoViewSet
from processador.views import ProcessadorViewSet
from pedido.views import PedidoViewSet

router = routers.DefaultRouter()
router.register('memoriaram',MemoriaRamViewSet, base_name='memoriaram')
router.register('produto',ProdutoViewSet, base_name='produto')
router.register('placa_mae',PlacaMaeViewSet, base_name='placa_mae')
router.register('placa_video',PlacaVideoViewSet, base_name='placa_video')
router.register('processador',ProcessadorViewSet, base_name='processador')
router.register('pedido',PedidoViewSet, base_name='pedido')
