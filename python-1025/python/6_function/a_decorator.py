#!/usr/bin/env python3

def tag(tagStr="p"):
    def _tag(callback):
        def inner(*args, **kwargs):
            s = str(callback(*args, **kwargs))
            return "<" + tagStr + ">" + s + "</" + tagStr + ">"
        return inner
    return _tag


def p(f):
    def inner():
        return "<p>" + f() + "</p>"
    return inner

def div(f):
    def inner():
        return "<div>" + f() + "</div>"
    return inner

def li(f):
    def inner():
        return "<li>" + f() + "</li>"
    return inner

@tag("html")
@tag("body")
@tag("ul")
@tag("li")
@tag("a")
@tag("p")
def test(testStr="hello"):
    return testStr

tag = tag("p")(test)
test = tag(tag(tag(tag(test))))

def main(fro, end, func):
    return fro + func() + end

@p
def test1():
    return "world"

if __name__ == "__main__":
    #  test = decro(test)
    print("test: ", test("python"))
    print("test1: ", test1())
    print("main: ", main("<p>", "</p>", lambda : "mainTest"))

