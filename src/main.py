from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from src.routers import ping, items

app = FastAPI()
app.include_router(ping.router)
app.include_router(items.router)


@app.get('/', include_in_schema=False)
async def root():
    return RedirectResponse(url='/docs')
