from typing import TypedDict

from httpx import Response

from clients.api_clients import APIClient


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий
    """
    courseId: str


class CreateExerciseDict(TypedDict):
    """
    Описание структуры запроса на создание задания
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseDict(TypedDict):
    """
    Описание структуры запроса на обновление задания
    """
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка заданий
        :param query: словарь с courseId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def create_exercise_api(self, request: CreateExerciseDict) -> Response:
        """
        Метод создание задания
        :param request: словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def get_exercise_by_exercise_id_api(self, exercise_id: str) -> Response:
        """
        Метод получения информации о задании
        :param exercise_id: идентификатор задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises{exercise_id}")

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseDict) -> Response:
        """
        Метод обновления задания
        :param exercise_id: идентификатор задания
        :param request: словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания
        :param exercise_id:
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises{exercise_id}")
