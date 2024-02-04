from . import commodity_controller as CommodityController
from . import commodity_type_controller as CommodityTypeController
from . import manufacturer_controller as ManufacturerController
from . import commodity_inbound_controller as CommodityInboundController

def register_controllers(app):
    app.register_blueprint(CommodityController.bp)
    app.register_blueprint(CommodityTypeController.bp)
    app.register_blueprint(ManufacturerController.bp)
    app.register_blueprint(CommodityInboundController.bp)