from sqlalchemy.orm import Session
from models.clienteModel import ClienteModel
from schemas.clienteSchema import ClienteSchema

class ClienteService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def obtener_clientes(self):
        return self.db.query(ClienteModel).all()

    def obtener_cliente_por_id(self, id_cliente: int):
        return self.db.query(ClienteModel).filter_by(idCliente=id_cliente).first()

    def crear_cliente(self, cliente: ClienteSchema):
        nuevo_cliente = ClienteModel(**cliente.dict())
        self.db.add(nuevo_cliente)
        self.db.commit()
        self.db.refresh(nuevo_cliente)  # Para cargar completamente los datos desde la base de datos
        return nuevo_cliente

    def actualizar_cliente(self, id_cliente: int, cliente_actualizado: ClienteSchema):
        cliente_existente = self.obtener_cliente_por_id(id_cliente)
        if cliente_existente:
            for key, value in cliente_actualizado.dict(exclude_unset=True).items():
                setattr(cliente_existente, key, value)
            self.db.commit()
            self.db.refresh(cliente_existente)
            return cliente_existente
        return None

    def eliminar_cliente(self, id_cliente: int):
        cliente_existente = self.obtener_cliente_por_id(id_cliente)
        if cliente_existente:
            self.db.delete(cliente_existente)
            self.db.commit()
            return True
        return False
