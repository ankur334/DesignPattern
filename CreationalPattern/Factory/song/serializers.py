import json
import xml.etree.ElementTree as et


class Serializer:

    @staticmethod
    def _serialization_to_json(song):
        song_info = {
            'id': song.id,
            'title': song.title,
            'artist': song.artist
        }
        return json.dumps(song_info)

    @staticmethod
    def _serialization_to_xml(song):
        song_info = et.Element('song', attrib={'id': song.song_id})
        title = et.SubElement(song_info, 'title')
        title.text = song.title
        artist = et.SubElement(song_info, 'artist')
        artist.text = song.artist
        return et.tostring(song_info, encoding='unicode')

    def _get_serializer(self, _format):
        if _format == "json":
            return self._serialization_to_json
        elif _format == "xml":
            return self._serialization_to_xml
        else:
            raise ValueError(_format)

    def serializer(self, song, _format):
        serializer = self._get_serializer(_format)
        return serializer(song)
