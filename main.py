import module1
import module2
import module3


##################
# Helper functions
def get_ctx(varname):
    return globals()[varname]


def set_ctx( varname, val):
    globals().update({varname:val} )

###########################

############################
# Create Global Contexts
# There is a way to add property+getter+setter 
# to a class dynamicly, but COVID brain figure out 
# how make it dynamic at runtime
# so, we get getter and setter inserted in the modules

module1.get_globaldemo = lambda:get_ctx("globaldemo") # Assign to module namespace
module1.set_globaldemo = lambda val:set_ctx("globaldemo",val) # Assign to module namespace

module2.get_globaldemo = lambda:get_ctx("globaldemo") # Assign to module namespace
module2.set_globaldemo = lambda val:set_ctx("globaldemo",val) # Assign to module namespace
################################



###########################
# Demo / test
###########################


globaldemo = "Defined In Main"
print("GO****************************")
print(f"Value accessed from main : {globaldemo=}")
module1.printglobaldemo()
print("Changing value in module1" )
module1.setglobaldemo()
module1.printglobaldemo()

print(f"Value accessed from main after updatodule1.printglobaldemo()e in module1: {globaldemo=}")
module2.printglobaldemo()
print("Changing value in module2" )
module2.setglobaldemo()
module2.printglobaldemo()

print(f"Value accessed from main after update in module2: {globaldemo=}")


module3.printglobaldemo()
print("Changing value in module3" )
module3.setglobaldemo()
module3.printglobaldemo()

print(f"Value accessed from main after update in module3: {globaldemo=}")

module1.printglobaldemo()