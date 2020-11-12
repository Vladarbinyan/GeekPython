def hello_world(world='World!'):
    """Наведи курсор на имя функции в месте ёё вызова и зажми ctrl чтобы увидеть этот комментарий"""
    return f'Hello, {world}'


print(hello_world())


def hello_world2(world='World!'):
    """
    Вызови Quick documentation (ctrl+q) чтобы увидеть подробности про ф-цию. или просто удерживай курсор над именем ф-ии
    :param world: кого или что приветсвуем
    :return: возвращаем форматированную строку
    :rtype: str
    """
    return f'Hello, {world}'


print(hello_world2())
