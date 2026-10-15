from .add_pet_error import AddPetErrorBody, add_pet_error_mapper
from .delete_order_error import DeleteOrderErrorBody, delete_order_error_mapper
from .delete_pet_error import DeletePetErrorBody, delete_pet_error_mapper
from .delete_user_error import DeleteUserErrorBody, delete_user_error_mapper
from .find_pets_by_status_error import FindPetsByStatusErrorBody, find_pets_by_status_error_mapper
from .find_pets_by_tags_error import FindPetsByTagsErrorBody, find_pets_by_tags_error_mapper
from .get_order_by_id_error import GetOrderByIdErrorBody, get_order_by_id_error_mapper
from .get_pet_by_id_error import GetPetByIdErrorBody, get_pet_by_id_error_mapper
from .get_user_by_name_error import GetUserByNameErrorBody, get_user_by_name_error_mapper
from .login_user_error import LoginUserErrorBody, login_user_error_mapper
from .place_order_error import PlaceOrderErrorBody, place_order_error_mapper
from .update_pet_error import UpdatePetErrorBody, update_pet_error_mapper
from .update_pet_with_form_error import UpdatePetWithFormErrorBody, update_pet_with_form_error_mapper
from .update_user_error import UpdateUserErrorBody, update_user_error_mapper
from .upload_file_error import UploadFileErrorBody, upload_file_error_mapper

__all__ = [
    "AddPetErrorBody",
    "DeleteOrderErrorBody",
    "DeletePetErrorBody",
    "DeleteUserErrorBody",
    "FindPetsByStatusErrorBody",
    "FindPetsByTagsErrorBody",
    "GetOrderByIdErrorBody",
    "GetPetByIdErrorBody",
    "GetUserByNameErrorBody",
    "LoginUserErrorBody",
    "PlaceOrderErrorBody",
    "UpdatePetErrorBody",
    "UpdatePetWithFormErrorBody",
    "UpdateUserErrorBody",
    "UploadFileErrorBody",
    "add_pet_error_mapper",
    "delete_order_error_mapper",
    "delete_pet_error_mapper",
    "delete_user_error_mapper",
    "find_pets_by_status_error_mapper",
    "find_pets_by_tags_error_mapper",
    "get_order_by_id_error_mapper",
    "get_pet_by_id_error_mapper",
    "get_user_by_name_error_mapper",
    "login_user_error_mapper",
    "place_order_error_mapper",
    "update_pet_error_mapper",
    "update_pet_with_form_error_mapper",
    "update_user_error_mapper",
    "upload_file_error_mapper",
]
