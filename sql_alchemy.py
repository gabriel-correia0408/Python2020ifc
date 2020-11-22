from flask_sqlalchemy import SQLAlchemy

banco = SQLAlchemy()

_session = banco.session


def save(model: banco.Model):
    _session.add(model)
    commit()
    return model


def commit():
    _session.commit()
