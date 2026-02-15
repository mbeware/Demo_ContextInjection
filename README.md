Un demo de solution pour injecter un context dans un module. Pas la meilleurs, mais pas la pire. Juste une suggestion ou un modèle pour inspirer d'autres solutions

module1 et module2 accèdent au context avec des fonctions injectées dans les modules. module3 accède au context en appelant les functions de __main__ directement

Resultats: 

```
GO****************************
Value accessed from main : globaldemo='Defined In Main'
Value accessed from module1 : get_globaldemo()='Defined In Main'
Changing value in module1
Value accessed from module1 : get_globaldemo()='Value updated in module1'
Value accessed from main after updatodule1.printglobaldemo()e in module1: globaldemo='Value updated in module1'
Value accessed from module2 : get_globaldemo()='Value updated in module1'
Changing value in module2
Value accessed from module2 : get_globaldemo()='Value updated in module2'
Value accessed from main after update in module2: globaldemo='Value updated in module2'
Value accessed from module3 : get_globaldemo()='Value updated in module2'
Changing value in module3
Value accessed from module3 : get_globaldemo()='Value updated in module3'
Value accessed from main after update in module3: globaldemo='Value updated in module3'
Value accessed from module1 : get_globaldemo()='Value updated in module3' (edited)Saturday, February 14, 2026 at 22:06
```


Avantage : seulement les globals que tu veux partager le sont. 
inconvenihent : Il faut 2 lignes et/ou fonctions par module et par variable pour injecter/definir le code . Il y a certainement moyen de le faire plus facilement avec une classe, 



Ex : Classes avec property : 
```
class MyClass:
    pass

def get_value(self):
    return self._value

def set_value(self, value):
    self._value = value

# Dynamically add property to the class
setattr(MyClass, 'dynamic_prop', property(get_value, set_value))

# Usage
obj = MyClass()
obj.dynamic_prop = 42  # Calls set_value
print(obj.dynamic_prop)  # Calls get_value → Output: 42
```

Idéalement les properties seraient dynamiques 

This is still a hack and not the clean way to do it. Ideally, if you want to use OOP, you would have a KernelInfo object that has all the context and would pass references to the objects containing the values or reference to function allowing to get/set them to other objects that need them in the init so that new object can either dynacly create properties to those values, call the functiion as needed or use the object.attributes directly.  All intanciation would be in main, but could references class that are defined in other modules. The same thing could be done in procedural programming too, by passing the needed values to function in other modules (in dictionnary as they are passed by ref, and not by value). No need for global (local or from other module), but the code is cleanly separated. But with the code base that we have now, I think Global are the way to go. A refactor could be done later.
commentaires. Mais sinon, je vais essayer d'etre la. (c´; est la partie cool de ma journée. ca fait travailler mon cerveau et evite quil se transforme en bouillie a ne pas servir) 
