from sql_alchemy import save
from app.domains.hoteis.model import HotelModel


def get():
    return HotelModel.query.filter_by(deleted_at=None)


def create(data: dict):
    data_hoteis = save(HotelModel(
        nome=data['nome'],
        estrelas=data['estrelas'],
        diaria=data['diaria'],
        cidade=data['cidade']
    ))
    return data_hoteis
