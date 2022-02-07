from datetime import datetime
from pytz import timezone
from sqlalchemy import Column, DATETIME, VARCHAR, INTEGER
from model.base import Base, DBSession
from sqlalchemy.exc import IntegrityError

def cur_datetime():
    return datetime.now(tz=timezone('America/Sao_Paulo'))


class UpdatedCreatedMixin(object):
    created = Column(DATETIME, default=cur_datetime)
    updated = Column(DATETIME, onupdate=cur_datetime)


class DataCorrectionDb(Base, UpdatedCreatedMixin):

    __tablename__ = "006_excel"

    id = Column(VARCHAR(150), primary_key=True, nullable=False, autoincrement=False)
    pedido = Column(VARCHAR(150), nullable=True)
    status_auto = Column(VARCHAR(150), nullable=True)
    status_mind = Column(VARCHAR(150), nullable=True)
    motivo_mind = Column(VARCHAR(150), nullable=True)
    last_auto_id = Column(VARCHAR(150), nullable=True)
    depara_status = Column(VARCHAR(150), nullable=True)
    depara_reason = Column(VARCHAR(150), nullable=True)
    contrato = Column(VARCHAR(150), nullable=True)
    squad = Column(VARCHAR(10), default="AUTOBOTS")
    system = Column(VARCHAR(50), default="PIPEFY")

    @staticmethod
    def insert_all_lines(xlsx):
        for i, row, in tuple(xlsx):
            try:
                collums = DataCorrectionDb(
                    id=row['da_externalid'],
                    pedido=row['pedido'],
                    status_auto=row['status auto'],
                    motivo_mind=row['motivo mind'],
                    last_auto_id=row['lastAuthorId'],
                    depara_status=row['depara_status'],
                    depara_reason=row['depara_reason'],
                    contrato=row['contrato']
                        )
                DBSession.add(collums)
                DBSession.commit()
            except IntegrityError as e:
                print('mysql.connector.errors.IntegrityError) 1062 (23000): Duplicate entry', e.args[0])
            except Exception as e:
                print(e)
        DBSession.close()

