import unittest
from CreationalPattern.Factory.song.songs import Song
from CreationalPattern.Factory.song.serializers import Serializer


class TestSum(unittest.TestCase):

    def test_songs(self):
        song = Song(
            _id=1,
            title="All is not well",
            artist="Me"
        )
        serializer = Serializer()
        json_format = serializer.serializer(
            song=song,
            _format="json"
        )
        assert json_format == '{"id": 1, "title": "All is not well", "artist": "Me"}'


if __name__ == "__main__":
    unittest.main()
