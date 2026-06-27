# variable length arguments 

def test(*agrs):
    print(args) # type: ignore
    print(len(args)) # type: ignore
    print(type(args)) # type: ignore

    test()