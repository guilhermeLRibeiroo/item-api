from fastapi import APIRouter
from src.services import items_service

router = APIRouter(
    prefix='/items',
    tags=['items'],
    responses={
        404: {
            "description": "Not found"
        }
    }
)


@router.get('/', status_code=200, summary="get all items")
async def get_items():
    return items_service.get_all()
