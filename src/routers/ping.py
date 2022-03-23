from fastapi import APIRouter

router = APIRouter(
    prefix='/ping',
    tags=['ping'],
    responses={
        404: {
            "description": "Not found"
        }
    }
)


@router.get('/', status_code=200, summary="just a ping")
async def ping():
    """
        Returns Pong!
    """
    return {
        "description": "Pong!"
    }
