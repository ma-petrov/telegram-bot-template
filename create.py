import os

name = input("bot name? ") or "bot"
description = input("bot description? ") or "a telegram bot"

with open("pyproject.toml", "r") as f:
    template = f.read()

template.replace(r"{{ name }}", f'"{name}"')
template.replace(r"{{ description }}", f'"{description}"')

with open("pyproject.toml", "w") as f:
    f.write(template)

os.system("poetry install")
# os.system("rm create.py")
