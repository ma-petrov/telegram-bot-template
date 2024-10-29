import os

name = input("bot name? ") or "bot"
description = input("bot description? ") or "a telegram bot"

with open("pyproject.toml", "r") as f:
    template = f.read()

file = (
    template
    .replace(r"{{ name }}", f'"{name}"')
    .replace(r"{{ description }}", f'"{description}"')
)

with open("pyproject.toml", "w") as f:
    f.write(file)

os.system("poetry install")

if input("delete create.py? (y/n) ") == "y":
    os.system("rm create.py")
