#! /usr/bin/env python3.10

import os
import sys
import traceback
from urllib.request import build_opener
import importlib
import datetime

import html2text

opener = build_opener()
opener.addheaders.append(("Cookie", f'session={os.environ["AOC_SESSION"]}'))


def new_py(file, froms=[]):
    if os.path.exists(file):
        return
    head = "\n".join([f"from {f} import *" for f in froms]) + "\n"
    with open(file, "w") as py:
        py.write(
            f"""{head}def aoc(data):
    total = 0
    data = data.split("\\n")
    return total
"""
        )


def html(response):
    page = ""
    for line in html2text.html2text(response.read().decode("utf-8")).split("\n"):
        if "[sponsors]" in line:
            page = ""
        if "Shareon" not in line and "Twitter" not in line and "Mastodon" not in line:
            page += line + "\n"
    return page[:-1]


def answer(id, data):
    mod = importlib.import_module(id)
    importlib.reload(mod)
    ans = mod.aoc(data)
    print(id, "=", ans)
    resp = input("Submit? (or _s_kip) [y]")
    if resp == "s":
        return
    if resp not in ("y", ""):
        raise Exception("Wrong")
    level = 2 if "b" in id else 1
    with opener.open(
        f"https://adventofcode.com/{id[3:7]}/day/{int(id[9:11])}/answer",
        data=f"level={level}&answer={ans}".encode("utf-8"),
    ) as response:
        page = html(response)
        print(page, end="")
        if "That's the right answer!" not in page:
            raise Exception("Incorrect")
    input("[continue]")


def step(id, data):
    while True:
        try:
            input("[Continue]")
            new_py(f"{id}.py", [] if id[-1] == "a" else [f"{id[:-1]}a"])
            os.system(f"{os.environ['EDITOR']} {id}.py")
            answer(id, data)
            break
        except KeyboardInterrupt:
            break
        except:
            traceback.print_exc()


def main(id=None):
    if id == None:
        id = datetime.datetime.now().strftime("%Y%m%d")
    with opener.open(
        f"https://adventofcode.com/{id[:4]}/day/{int(id[6:8])}/input"
    ) as response:
        data = response.read().decode("utf-8")[:-1]
    with opener.open(
        f"https://adventofcode.com/{id[:4]}/day/{int(id[6:8])}"
    ) as response:
        page = html(response)
        print(page, end="")
        print(data[:100])

    step(f"aoc{id}a", data)

    with opener.open(
        f"https://adventofcode.com/{id[:4]}/day/{int(id[6:8])}"
    ) as response:
        print(html(response), end="")

    step(f"aoc{id}b", data)


if __name__ == "__main__":
    main(*sys.argv[1:])
