__all__ = ["alias"]


def alias(name: str) -> str:
    parts = name.split(".")
    other = parts[1:]
    match parts[0]:
        case "c":
            return ".".join(["context", *other])
        case "q":
            return ".".join(["query", *other])
        case "t":
            return ".".join(["temp", *other])
        case "v":
            return ".".join(["variable", *other])
    return name
