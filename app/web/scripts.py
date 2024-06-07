# scripts.py


def black_format():
    import os

    os.system("black .")


def lint():
    import os

    os.system("flake8 . && isort . && pylint **/*.py")


if __name__ == "__main__":
    black_format()
    lint()
