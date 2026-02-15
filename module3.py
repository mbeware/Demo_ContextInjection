import sys

# Access a function or variable defined in the main module
main_module = sys.modules['__main__']

# Create Global Contexts getter/setter
def get_globaldemo():
    return main_module.get_ctx("globaldemo") 
def set_globaldemo(val):
    main_module.set_ctx("globaldemo",val) 



def printglobaldemo():
    print(f"Value accessed from module3 : {get_globaldemo()=}")                  

def setglobaldemo():
    set_globaldemo("Value updated in module3")


