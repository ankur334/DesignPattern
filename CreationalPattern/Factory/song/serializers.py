class Serializer:
    def serializer(self, song, _format):
        if _format == "json":
            pass
        elif _format == "xml":
            pass
        else:
            raise NotImplementedError(
                "For now we only support serializing the json and xml type."
            )