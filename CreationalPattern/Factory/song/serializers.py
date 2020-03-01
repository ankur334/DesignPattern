import json
import xml.etree.ElementTree as et


class Serializer:
    def serializer(self, song, _format):
        if _format == "json":
            song_info = {
                'id': song.id,
                'title': song.title,
                'artist': song.artist
            }
            return json.dumps(song_info)
        elif _format == "xml":
            song_info = et.Element('song', attrib={'id': song.song_id})
            title = et.SubElement(song_info, 'title')
            title.text = song.title
            artist = et.SubElement(song_info, 'artist')
            artist.text = song.artist
            return et.tostring(song_info, encoding='unicode')
        else:
            raise NotImplementedError(
                "For now we only support serializing the json and xml type."
            )
