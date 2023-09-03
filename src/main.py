import tok
import loc
import errors

def main():
    print(
        "The python implementation of the Balsa compiler is not yet implemented"
    )
    errors.compiler_error(loc.Loc("file.bs", 1, 2), "this is bad. very bad.")

if __name__ == '__main__':
    main()
