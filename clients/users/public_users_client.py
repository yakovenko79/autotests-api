from typing import TypedDict

from httpx import Response

from clients.api_clients import APIClient
from clients.authentication.authentication_client import AuthenticationClient
from clients.public_http_builder import get_public_http_client
from tools.fakers import get_random_email


class User(TypedDict):
    """
    Описание структуры пользователя
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на создание нового пользователя
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ответа создания пользователя
    """
    user: User


class PublicUsersClient(APIClient):
    """
    Клиент для работы с  /api/v1/users
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод создает нового пользователя

        :param request: словарь с email, password, lastName, firstName, middleName
        :return: ответ от сервера в виде httpx.Response
        """
        return self.post("/api/v1/users", json=request)

    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        response = self.create_user_api(request)
        return response.json()


def get_public_users_client() -> PublicUsersClient:
    """
    Функция создает экземпляр PublicUsersClient с уже настроенными HTTP-клиентом
    :return:Готовый к использованию PublicUsersClient
    """
    return PublicUsersClient(client=get_public_http_client())
