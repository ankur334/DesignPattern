import json
import xml.etree.ElementTree as et


class Serializer:

    @staticmethod
    def _get_serializer(_format):
        if _format == "json":
            return JsonSerializer
        elif _format == "xml":
            return XMLSerializer
        else:
            raise ValueError(_format)

    def serializer(self, song, _format):
        serializer = self._get_serializer(_format)
        return serializer.serializer(song)


class JsonSerializer:
    @staticmethod
    def serializer(song):
        song_info = {
            'id': song.id,
            'title': song.title,
            'artist': song.artist
        }
        return json.dumps(song_info)


class XMLSerializer:
    @staticmethod
    def serializer(song):
        song_info = et.Element('song', attrib={'id': song.id})
        title = et.SubElement(song_info, 'title')
        title.text = song.title
        artist = et.SubElement(song_info, 'artist')
        artist.text = song.artist
        return et.tostring(song_info, encoding='unicode')
