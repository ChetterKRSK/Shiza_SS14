import keyboard


def block():
    for i in range(150):
        keyboard.block_key(i)


def unblock():
    for i in range(150):
        keyboard.unblock_key(i)  # type: ignore
