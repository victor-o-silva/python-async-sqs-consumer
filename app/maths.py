def get_semester(*, month: int) -> int:
    if month <= 6:
        return 1

    return 2
