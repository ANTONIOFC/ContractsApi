from fastapi import Depends
from datetime import date  

from database import get_db
from models import Contract


async def seed_data():

    db_gen = get_db()
    db = next(db_gen)
    if db.query(Contract).count() == 0:
        contract1 = Contract(title='Contrato 1', value = 1200, 
                        due_date=date(2025, 12, 31), category = 'Recorrente',
                        supplier = 'Fornecedor 1', status = 'vigente', user = 'admin')
        contract2 = Contract(title='Contrato 2', value = 1200, 
                due_date=date(2025, 11, 30), category = 'Recorrente',
                supplier = 'Fornecedor 2', status = 'vigente', user = 'admin')
        contract3 = Contract(title='Contrato 3', value = 1200, 
                due_date=date(2025, 12, 15), category = 'Recorrente',
                supplier = 'Fornecedor 3', status = 'vigente', user = 'admin')

        db.add(contract1)
        db.add(contract2)
        db.add(contract3)
        db.commit()
        print('Database initial seed')
    else:
        print('Database already contains data !')