from pydantic import BaseModel, EmailStr, Field
from datetime import date, datetime
from typing import Optional

class ClienteSchema(BaseModel):
    idCliente: Optional[int] = Field(None, description="ID del cliente (opcional)")
    nombre: str = Field(..., description="Nombre del cliente")
    apellidoPaterno: str = Field(..., description="Apellido paterno del cliente")
    apellidoMaterno: str = Field(..., description="Apellido materno del cliente")
    correo: EmailStr = Field(..., description="Correo electrónico del cliente")
    dni: str = Field(..., min_length=8, max_length=8, description="DNI del repartidor (8 caracteres)")
    telefono: Optional[str] = Field(None, pattern=r'^\d{9}$', description="Número de teléfono del cliente (opcional, 9 dígitos)")
    direccion: Optional[str] = Field(None, max_length=100, description="Dirección del cliente (opcional, hasta 100 caracteres)")
    fechaNacimiento: Optional[date] = Field(None, description="Fecha de nacimiento del cliente (sin hora)")
    sexo: Optional[str] = Field(None, description="Sexo del cliente")
    created_at: Optional[datetime] = Field(None, description="Fecha de creación del cliente")

    class Config:
        title = "Esquema de Cliente"
        description = "Modelo para representar un cliente"
        json_schema_extra = {
            "examples": [
                {
                    "apellidoMaterno": "Gómez",
                    "apellidoPaterno": "Pérez",
                    "correo": "juan@example.com",
                    "direccion": "Calle Principal 456 - San Isidro",
                    "dni": "76543219",
                    "fechaNacimiento": "1990-12-15",
                    "nombre": "Juan",
                    "sexo": "masculino",
                    "telefono": "987654321"
                }

            ]
        }
