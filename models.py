from pydantic import BaseModel, Field

class Producto(BaseModel):
    nombre: str = Field(..., min_length=2)
    categoria: str = Field(..., min_length=2)
    precio: float = Field(..., gt=0)
    cantidad: int = Field(..., ge=0)
