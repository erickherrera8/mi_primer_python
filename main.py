from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Producto

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

inventario = {}
contador_id = 1


@app.post("/productos")
def crear_producto(producto: Producto):
    global contador_id
    inventario[contador_id] = producto
    contador_id += 1
    return {"mensaje": "Producto creado", "id": contador_id - 1}


@app.get("/productos")
def listar_productos():
    return inventario


@app.get("/productos/{id}")
def obtener_producto(id: int):
    if id not in inventario:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return inventario[id]


@app.put("/productos/{id}")
def actualizar_producto(id: int, producto: Producto):
    if id not in inventario:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    inventario[id] = producto
    return {"mensaje": "Producto actualizado"}


@app.delete("/productos/{id}")
def eliminar_producto(id: int):
    if id not in inventario:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    del inventario[id]
    return {"mensaje": "Producto eliminado"}
