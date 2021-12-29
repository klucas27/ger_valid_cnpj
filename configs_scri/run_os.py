import os
import sys

list_cmds = {
    'cls': ["clear", "cls"],
    'dir': ["ls", "dir"],
}

systempc = sys.platform


def os_run(cmds):

    if systempc == "linux":
        return os.system(f"{list_cmds.get(str(cmds))[0]}")
    elif systempc == "win32":
        return os.system(f"{list_cmds.get(str(cmds))[1]}")


if __name__ == "__main__":
    os_run("cls")
