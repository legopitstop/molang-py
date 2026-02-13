__all__ = ["MolangError", "MolangSyntaxError"]


class MolangError(Exception):
    pass


class MolangSyntaxError(MolangError):
    pass
