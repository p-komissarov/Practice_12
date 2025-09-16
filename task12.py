from keyword import iskeyword

def python_name(name):
    
    if iskeyword(name):
        return False
    
    if name[0].isdigit():
        return False
    
    allowed = "abcdefghijklmnopqrstuvwxyz\
        ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"\
        
    for i in name:
        if i not in allowed:
            return False
    
    return True

name = input()
print(python_name(name))