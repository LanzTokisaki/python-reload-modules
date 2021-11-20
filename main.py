import importlib, sys
import my_module


# call this method to reload all modules (including submodules) without restarting the program
def reload_modules():

    # sys.modules changes value while looping which causes problem so we're doing it this way instead
    modules = [i for i in sys.modules] 

    for module in modules:
        try:
            if "importlib" in module: # reloading importlib causes trouble so we should ignore that module
                continue
            
            importlib.reload(sys.modules[module])
            
        except:
            pass
        
        
my_module.module_func()

input("Press enter to continue...") # prevent from continuing unless we wanted so
reload_modules()

my_module.module_func()