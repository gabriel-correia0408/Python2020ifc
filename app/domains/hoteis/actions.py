from app.domains.hoteis.model import HotelModel
from sql_alchemy import save


def get():
    return HotelModel.query.all()


def create(data: dict):
    data_hoteis = save(HotelModel(
        nome=data['nome'],
        estrelas=data['estrelas'],
        diaria=data['diaria'],
        cidade=data['cidade']
    ))
    return data_hoteis
