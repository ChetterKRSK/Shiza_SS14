from typing import Union
import keyboard


def block():
    for i in range(150):
        keyboard.block_key(i)


def unblock():
    for i in range(150):
        keyboard.unblock_key(i)  # type: ignore


class keyboard_fetcher:
    def __init__(self) -> None:
        self.toggle = False
        self.key_list = []

    def change_toggle(self, status: Union[bool, None] = None):
        if status is None:
            self.toggle = not self.toggle
        else:
            self.toggle = status
        if self.toggle:
            self.handler_all()
        else:
            self.stop_handler_all()

    def _hander_all_press(self, event):
        print("press - " + event.name)
        key = event.name.lower()
        if key not in self.key_list:
            self.key_list.append(key)

    def _hander_all_release(self, event):
        print("release - " + event.name)
        key = event.name.lower()
        if key in self.key_list:
            self.key_list.pop(self.key_list.index(key))

    def handler_all(self):
        self.toggle = True
        self.handler_hook_on_press = keyboard.on_press(
            lambda event: self._hander_all_press(event), suppress=True
        )
        self.hander_hook_on_release = keyboard.on_release(
            lambda event: self._hander_all_release(event), suppress=True
        )

    def stop_handler_all(self):
        self.toggle = False
        keyboard.unhook_all()
        # keyboard.unhook(self.handler_hook_on_press)
