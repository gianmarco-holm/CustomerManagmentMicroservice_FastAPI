# Arquitectura de Microservicios para Empresa de Delivery

## Microservicios

### 1. ProductManagmentMicroservice_FastAPI

- Base de Datos: [Nombre de la base de datos]

### 2. ServicioUsuarios-FastAPI

- Base de Datos: [Nombre de la base de datos]

### 3. CustomerManagmentMicroservice_FastAPI

- Base de Datos: [Nombre de la base de datos]

### 4. DeliveryManManagmentMicroservice_FastAPI

- Base de Datos: [Nombre de la base de datos]

### 5. OrderManagmentMicroservice_FastAPI

- Base de Datos: [Nombre de la base de datos]

## Tecnologías Utilizadas

- **FastAPI**: Framework base para el desarrollo de microservicios.
- **Uvicorn**: Framework usado para el servidor.
- **Starlette**: Librería para manejar errores en el middleware.
- **Pydantic**: Librería para validar datos en esquema.
- **SQLalchemy**: ORM utilizado para comunicarse con la base de datos.
- **PyJWT**: Librería para generar el token del API.

## Flujo de Creación de Orden

1. **OrderManagmentMicroservice_FastAPI** recibe los datos del repartidor, producto y usuario.
2. Se conecta a los demás microservicios para validar la existencia de los datos.
   - Consulta **ProductManagmentMicroservice_FastAPI** para validar el producto.
   - Consulta **ServicioUsuarios-FastAPI** para validar el usuario.
   - Consulta **CustomerManagmentMicroservice_FastAPI** para validar el cliente.
   - Consulta **DeliveryManManagmentMicroservice_FastAPI** para validar el repartidor.
3. Si todas las validaciones son exitosas, crea la orden en su propia base de datos.

## Diagrama de Arquitectura

```plaintext
+----------------------------------------+
|            Order Management            |
|          Microservice_FastAPI          |
+-------------------+--------------------+
                    |
                    | Consulta
                    v
+-------------------+--------------------+
|        Product Management             |
|        Microservice_FastAPI           |
+-------------------+--------------------+
                    |
                    | Consulta
                    v
+-------------------+--------------------+
|        Servicio Usuarios               |
|        Microservice_FastAPI           |
+-------------------+--------------------+
                    |
                    | Consulta
                    v
+-------------------+--------------------+
|    Customer Management                |
|    Microservice_FastAPI               |
+-------------------+--------------------+
                    |
                    | Consulta
                    v
+-------------------+--------------------+
| Delivery Management                   |
| Microservice_FastAPI                   |
+-------------------+--------------------+
