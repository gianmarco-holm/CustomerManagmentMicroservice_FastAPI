from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.clienteSchema import ClienteSchema
from services.clienteService import ClienteService
from utils.dependencies import get_db

cliente_router = APIRouter()

@cliente_router.get('/clientes', tags=['Clientes'], response_model=List[ClienteSchema])
def obtener_clientes(db: Session = Depends(get_db)) -> List[ClienteSchema]:
    try:
        resultado = ClienteService(db).obtener_clientes()
        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener clientes: {str(e)}")

@cliente_router.get('/clientes/{id_cliente}', tags=['Clientes'], response_model=ClienteSchema)
def obtener_cliente_por_id(id_cliente: int, db: Session = Depends(get_db)) -> ClienteSchema:
    try:
        resultado = ClienteService(db).obtener_cliente_por_id(id_cliente)
        if resultado:
            return resultado
        else:
            raise HTTPException(status_code=404, detail=f"No se encontró un cliente con el ID {id_cliente}.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener cliente por ID: {str(e)}")

@cliente_router.post('/clientes', tags=['Clientes'], response_model=ClienteSchema, status_code=201)
def crear_cliente(cliente: ClienteSchema, db: Session = Depends(get_db)) -> ClienteSchema:
    try:
        nuevo_cliente = ClienteService(db).crear_cliente(cliente)
        return nuevo_cliente
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear cliente: {str(e)}")

@cliente_router.put('/clientes/{id_cliente}', tags=['Clientes'], response_model=ClienteSchema)
def actualizar_cliente(id_cliente: int, cliente_actualizado: ClienteSchema, db: Session = Depends(get_db)) -> ClienteSchema:
    try:
        resultado = ClienteService(db).actualizar_cliente(id_cliente, cliente_actualizado)
        if resultado:
            return resultado
        else:
            raise HTTPException(status_code=404, detail=f"No se encontró un cliente con el ID {id_cliente}.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar cliente: {str(e)}")

@cliente_router.delete('/clientes/{id_cliente}', tags=['Clientes'], status_code=204)
def eliminar_cliente(id_cliente: int, db: Session = Depends(get_db)):
    try:
        eliminado_exitosamente = ClienteService(db).eliminar_cliente(id_cliente)
        if not eliminado_exitosamente:
            raise HTTPException(status_code=404, detail=f"No se encontró un cliente con el ID {id_cliente}.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar cliente: {str(e)}")
