from fastapi import FastAPI, Request, Form
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from app.routes import api
import os

ENV = os.environ.get("ENV", "development")
DEBUG = (ENV == "development")

# Si usas bases de datos o lógica que depende del entorno, ajusta aquí.
if not DEBUG:
    print("Running in Production mode")
    # Lógica para producción, ej: deshabilitar documentación
    app = FastAPI(docs_url=None, redoc_url=None)
else:
    print("Running in Development mode")
    app = FastAPI()

app.include_router(api.router)

# --- Static and Templates Configuration ---
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# --- CORS Configuration (allow localhost for dev) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://127.0.0.1"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Page Routes ---
@app.get("/")
def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Inicio"})

@app.get("/services")
def read_services(request: Request):
    return templates.TemplateResponse("services.html", {"request": request, "title": "Servicios"})

@app.get("/contact")
def read_contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request, "title": "Contacto"})

# --- API Endpoint for Contact Form ---
@app.post("/api/contact")
async def submit_contact(
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...)
):
    # No DB for now, just return JSON confirmation
    return JSONResponse(
        content={
            "success": True,
            "message": "Mensaje recibido correctamente.",
            "data": {"name": name, "email": email, "message": message},
        }
    )

