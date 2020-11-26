from flask_marshmallow import Marshmallow

from app.domains.hoteis.model import HotelModel

ma = Marshmallow()


class HoteisSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = HotelModel
