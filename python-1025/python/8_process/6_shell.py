#!/usr/bin/env python3


import os


if __name__ == "__main__":
    def main():
        while True:
            cmd = input("<自己的SHELL>: ")
            if cmd == "exit":
                break
            elif cmd.startswith("cd "):
                os.chdir(cmd[3:])
            else:
                os.system(cmd)

    main()
