from fastapi import Request, Response

# Definimos una función middleware
async def custom_middleware(request: Request, call_next):
    # Aquí puedes hacer cualquier acción antes de que la ruta maneje la solicitud
    print("Middleware: Antes de la solicitud")

    # Llama a la función que maneja la solicitud
    response: Response = await call_next(request)

    is_logged = False

    if not is_logged:
        response.status_code = 401
        response.body = b"Unauthorized"
        return response

    # Aquí puedes hacer cualquier acción después de que la ruta maneje la solicitud
    print("Middleware: Después de la solicitud")

    # Puedes modificar la respuesta aquí si es necesario
    return response


