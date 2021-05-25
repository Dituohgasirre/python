#!/usr/bin/env python3

import win
import pygame

def run(key, args):
    print(key, args)

def main():
    p = win.Win()
    p.key(pygame.K_a, run, "test key")
    p.mouse(lambda b, p, d: print("点击: ", b, p, d), (0, 0, 100, 100))
    p.fill((0, 255, 0), (0, 0, 100, 100)).flip().loop()



    p = win.create()
    win.key(p, pygame.K_a, run, "test key")
    win.mouse(p, lambda b, p, d: print("点击: ", b, p, d), (0, 0, 100, 100))
    win.screen().fill((0, 255, 0), (0, 0, 100, 100))
    win.flip()
    win.loop(p)

if __name__ == "__main__":
    main()
