class PrimaryKey:
    def __enter__(self):
        print("вход")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(exc_type)
        return True


with PrimaryKey() as pk:
    raise ValueError