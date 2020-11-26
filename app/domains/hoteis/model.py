from sql_alchemy import banco


class HotelModel(banco.Model):
    __tablename__ = 'hoteis'

    hotel_id = banco.Column(banco.String, primary_key=True)
    nome = banco.Column(banco.String(80))
    estrelas = banco.Column(banco.Float(precision=1))
    diaria = banco.Column(banco.Float(precision=2))
    cidade = banco.Column(banco.String(40))

    def serialize(self):
        return {
            'id': self.hotel_id,
            'street': self.nome,
            'number': self.estrelas,
            'complement': self.diaria,
            'neighborhood': self.cidade,
        }

