from fastapi import APIRouter

router = APIRouter(
    prefix='/ping',
    tags=['ping'],
    responses={404: {"description": "Not found"}}
)


@router.get('/')
async def ping():
    return {
            'statusCode': 200,
            'description': 'pong!'
        }
