from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from src.routers import ping_router, items_router

app = FastAPI()
app.include_router(ping_router.router)
app.include_router(items_router.router)


@app.get('/', include_in_schema=False)
async def root():
    return RedirectResponse(url='/docs')
