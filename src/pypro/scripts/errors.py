class CommandError(Exception):
    pass


class LengthMismatchError(CommandError):
    pass


class CRCError(CommandError):
    pass
