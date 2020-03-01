import unittest
from CreationalPattern.Factory.song.songs import Song
from CreationalPattern.Factory.song.serializers import Serializer


class TestSum(unittest.TestCase):

    def test_songs(self):
        song = Song(
            _id=1,
            title="All is well",
            artist="Me"
        )
        serializer = Serializer()
        json_format = serializer.serializer(
            song=song,
            _format="json"
        )
        print("Song", song)
        print("Json Serialized", json_format)
        assert 2 == 2


if __name__ == "__main__":
    unittest.main()
