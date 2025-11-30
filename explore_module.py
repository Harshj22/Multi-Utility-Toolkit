def explore_module_attributes():
    module_name = input("Enter module name to explore: ")
    try:
        module = __import__(module_name)
        attributes = dir(module)
        print("Available attributes in", module_name, "module:")
        print(attributes)
    except ModuleNotFoundError:
        print("Module not found.")

