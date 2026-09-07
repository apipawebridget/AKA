def long_name_check(func):
    def wrapper(name):
        name_len=len(name)
        if name_len>4:
            return f"{name}is long!"
        else:
            return func(name)
    return wrapper
@long_name_check
def greeting (name):
    return f"hello {name}" 
print(greeting( "Bridget")) 
print( greeting("Pal")) 