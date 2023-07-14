from typing import Any
import redis


class RemoteRedis(object):
    """
    This is a wrapper over redis. The sole purpose of its existance is to
    put namespace over the keys so that they don't conflict
    """

    def __init__(self, hostname: str, port: str, password: str, app: str, project: str):
        self.hostname = hostname
        self.port = port
        self.password = password
        self.project = project
        self.app = app

        self.redis_client = redis.Redis(
            host=self.hostname, port=self.port, password=self.password
        )

    def __create_key(self, key: str) -> str:
        """
        Internal function to create the namespace
        """
        formatted_key = str(self.app) + "." + str(self.project) + "." + key
        return formatted_key

    def set_key(self, key, value) -> bool:
        """
        Set a Key
        """
        if key is None or value is None:
            return False

        formatted_key: str = self.__create_key(key)
        ret_code: bool = self.redis_client.set(formatted_key, value)
        return ret_code

    def get_key(self, key) -> Any:
        """
        Retrieve a key
        """
        formatted_key: str = self.__create_key(key)
        return self.redis_client.get(formatted_key)


if __name__ == "__main__":
    from redis_config import hostname, port, password, project, app

    hostname = hostname
    port = port
    password = password
    project = project
    app = app

    key1 = "test_key"
    value1 = "test_successful"
    redis = RemoteRedis(hostname, port, password, app, project)
    redis.set_key(key1, value1)
