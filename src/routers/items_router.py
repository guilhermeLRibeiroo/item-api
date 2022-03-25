from fastapi import APIRouter, Response, status
from src.services import items_service
from src.services.models.item_model import ItemRequestModel

router = APIRouter(
    prefix='/items',
    tags=['items'],
    responses={
        status.HTTP_404_NOT_FOUND: {
            'description': 'Not found'
        }
    }
)


@router.get('/',
            status_code=status.HTTP_200_OK)
async def get_items():
    return items_service.get_all()


@router.post('/',
             status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemRequestModel):
    return items_service.create(item)


@router.delete('/{item_id}',
               status_code=status.HTTP_200_OK)
async def delete_item(item_id, response: Response):
    service_result = items_service.delete_by_id(item_id)
    if service_result:
        response.status_code = status.HTTP_200_OK
        return {
            'description': 'Deleted'
        }
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            'description': 'Not found'
        }


@router.get('/{item_id}',
            status_code=status.HTTP_200_OK)
async def get_item_by_id(item_id):
    item = items_service.get_by_id(item_id)
    return item


@router.put('/{item_id}',
            status_code=status.HTTP_204_NO_CONTENT)
async def update_item(item_id, item: ItemRequestModel, response: Response):
    update_result = items_service.update(item_id, item)
    if not update_result:
        response.status_code = status.HTTP_304_NOT_MODIFIED
