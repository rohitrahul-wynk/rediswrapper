# RedisWrapper
RedisWrapper is a Python package that provides a wrapper around Redis, adding a namespace to the keys to prevent collisions with other keys in the Redis database. It simplifies the process of working with Redis by automatically instantiating an instance of Redis within the wrapper, eliminating the need to provide a separate Redis instance.

Usage
To use RedisWrapper, follow these steps:

Import the RemoteRedis class from the rediswrapper module.
Instantiate a RemoteRedis object, providing the Redis hostname, port, project, and app as parameters.
Use the RemoteRedis object to interact with the Redis database, automatically namespacing the keys.
Here's an example of how to use RedisWrapper:

from redis_connector import RemoteRedis

# Instantiate a RemoteRedis object
redis = RemoteRedis(host='localhost', port=6379, project='myproject', app='myapp')

# Set a key-value pair
redis.set_key('mykey', 'myvalue')

# Get the value for a key
value = redis.get_key('mykey')
print(value)  # Output: 'myvalue'

# Delete a key
redis.delete_key('mykey')
In this example, the keys are automatically namespaced using the provided project and app information. For example, the key 'mykey' is stored as 'myproject:myapp:mykey' in the Redis database.

Contributing
Contributions to RedisWrapper are welcome! If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository.

License
RedisWrapper is licensed under the MIT License.

Acknowledgements
RedisWrapper was inspired by the need for an easy-to-use wrapper around Redis, providing namespace support. Special thanks to the Redis community for their excellent work on Redis.