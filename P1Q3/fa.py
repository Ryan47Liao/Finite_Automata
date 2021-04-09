import goody


def read_fa(file : open) -> {str:{str:str}}:
    """ 
    returns the dictionary representing the finite automaton; 
    hint: I used splicing and the zip function to build the inner dictionaries. (body is 6 lines).
    INPUT: even;0;even;1;odd
    OUTPUT: {'even' : {'0':'even','1':'odd'} }
    """
    Dict = {}
    
    for line in file: 
        inner_Dict = {}
        LST = line.rstrip("\n").split(";")
        inner =  LST[1:]
        for index in range(0, len(inner), 2): 
            inner_Dict[str(inner[index])] = str(inner[index+1])
        Dict[LST[0]] = inner_Dict
    return Dict
            


def fa_as_str(fa : {str:{str:str}}) -> str:
    """
    Returns a multi-line string (each line is ended by '\n'), 
    which when printed shows the contents of the FA in the appropriate textual form:
    sorted alphabetically by state, with a state's transitions sorted by their input value
    """
    STR = ''
    for state in sorted(fa): 
        LST_temp = list()
        for input, destination in sorted(zip(fa[state].keys(), fa[state].values())):
            LST_temp.append((input, destination)) 
        STR += "  " + str(state) + ' transitions: ' +  str(LST_temp) + "\n"
    print(STR)
    return STR

    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    '''
        ['even', ('1', 'odd'), ('0', 'odd'), ('1', 'even'), ('1', 'odd'), ('0', 'odd'), ('1', 'even')]

    '''
    LST = [state]
    for input in inputs: 
        LST.append((input, fa[state].get(str(input))))
        if fa[state].get(str(input)) is not None: 
            state = fa[state].get(str(input)) 
    return LST 
        


def interpret(fa_result : [None]) -> str:
    STR = ""
    STR += 'Start state = ' + str(fa_result[0]) + "\n"
    for element in fa_result[1:]:
        current_state = element[1]
        if element[1] is not None: 
            
            STR += f"  Input = {element[0]}; new state = {current_state}\n" 
        else: 
            STR += f"  Input = {element[0]}; illegal input: simulation terminated\n"
    STR += f"Stop state = {current_state}\n"
    return STR 




if __name__ == '__main__':
    # Write script here
    
    file = None
    while file is None:
        try:
            file = open(input("Input the file name detailing the Finite Automaton:"))
            FA = read_fa(file)
        except FileNotFoundError:
            print("Error, file not found...")
    print('The details of the Finite Automaton')
    fa_as_str(FA)
    file = open(input('Input the file name detailing groups of start-states and their inputs: '))
    for line in file: 
        line = line.rstrip("\n").split(";")
        state = line[0]
        inputs = line[1:]
        print('FA: the trace from its start-state')
        print(interpret(process(FA, state, inputs)))
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
