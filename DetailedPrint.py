
def sumaStringRecursiva(String, arg):
    if not String:
        return ""
    elif String[0] == "x":
        return str(arg) + String[1:]
    else:
        return String[0] + sumaStringRecursiva(String[1:], arg)

def imprimirDetalladamente(String, num):
    """
    E: String that will be formatted into line viewing print
    S: An array for easy management
    R: String and integers only
    """
    beginning_of_line = "ln[x]: "
    empty_list = []
    empty_str = ""
    for i in range(len(String)):
        if i == 0:
            beginning_of_line = sumaStringRecursiva(beginning_of_line, num)
            empty_str += beginning_of_line
            empty_str += String[0]
            beginning_of_line = "ln[x]: "
        elif String[i] == ",":
            num += 1
            beginning_of_line = sumaStringRecursiva(beginning_of_line, num)
            empty_list.append(empty_str)
            empty_str = beginning_of_line
            beginning_of_line = "ln[x]: "
        else:
            empty_str += String[i]
    
    if empty_str:
        empty_list.append(empty_str)
    
    return empty_list

def imprimirBonito(Lista):
    for linea in Lista:
        print(linea)
    print("<<<>>>") 

         
