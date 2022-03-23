from fastapi import APIRouter

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
    return [
            {
                "id": -1,
                "name": "item test"
            }
        ]
