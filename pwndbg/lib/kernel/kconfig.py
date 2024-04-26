from __future__ import annotations

import zlib
from collections import UserDict


def parse_config(config_text: bytes) -> dict[str, str]:
    res = {}

    for line in config_text.split(b"\n"):
        if b"=" in line:
            config_name, config_val = line.split(b"=", 1)
            res[config_name.decode("ascii")] = config_val.decode("ascii")

    return res


def parse_compresed_config(compressed_config: bytes) -> dict[str, str]:
    config_text = zlib.decompress(compressed_config, 16)
    return parse_config(config_text)


def config_to_key(name: str) -> str:
    return "CONFIG_" + name.upper()


class Kconfig(UserDict):
    def __init__(self, compressed_config: bytes) -> None:
        super().__init__()
        self.data = parse_compresed_config(compressed_config)

    def get_key(self, name: str) -> str | None:
        # Attempt to lookup the value by key or uppercase name
        key = config_to_key(name)
        if key in self.data:
            return key
        elif name.upper() in self.data:
            return name.upper()
        # Return the original name if not found by key or uppercase name
        return name

        return None

    def __getitem__(self, name: str):
        key = self.get_key(name)
        if key:
            return self.data[key]

        raise KeyError(f"Key {name} not found")

    def __contains__(self, name: str) -> bool:  # type: ignore[override]
        return self.get_key(name) is not None

    def __getattr__(self, name: str):
        return self.get(name)
