from fastapi import APIRouter

router = APIRouter(
    prefix='/items',
    tags=['items'],
    responses={404: {"description": "Not found"}}
)


@router.get('/')
async def get_items():
    return [
            {
                "id": -1,
                "name": "item test"
            }
        ]
