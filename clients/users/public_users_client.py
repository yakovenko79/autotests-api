from typing import TypedDict

from httpx import Response

from clients.api_clients import APIClient


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на создание нового пользователя
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


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
