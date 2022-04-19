import ormar
from db import metadata, database


class Video():
    class Meta:
        metadata = metadata
        database = database