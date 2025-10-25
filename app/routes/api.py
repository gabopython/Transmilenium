from fastapi import APIRouter, Form, Request
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/api")

@router.post("/contact")
async def contact_form(
    request: Request,
    name: str = Form(None),
    email: str = Form(None),
    phone: str = Form(None),
    message: str = Form(None)
):
    # If JSON body (fallback)
    if not name and request.headers.get("content-type", "").startswith("application/json"):
        data = await request.json()
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        message = data.get("message")

    # Validate required fields
    if not all([name, email, phone, message]):
        return JSONResponse(
            {"status": "error", "error": "Todos los campos son obligatorios."},
            status_code=400
        )

    # (Optional: send email or log the message here)
    print(f"📩 Nuevo mensaje: {name}, {email}, {phone}, {message}")

    return JSONResponse({"status": "ok"})
