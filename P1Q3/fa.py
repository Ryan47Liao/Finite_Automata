import goody


def read_fa(file : open) -> {str:{str:str}}:
    """ 
    returns the dictionary representing the finite automaton; 
    hint: I used splicing and the zip function to build the inner dictionaries. (body is 6 lines).
    INPUT: even;0;even;1;odd
    OUTPUT: {'even' : {'0':'even','1':'odd'} }
    """
    pass


def fa_as_str(fa : {str:{str:str}}) -> str:
    """
    Returns a multi-line string (each line is ended by '\n'), 
    which when printed shows the contents of the FA in the appropriate textual form:
    sorted alphabetically by state, with a state's transitions sorted by their input value
    """
    pass

    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    pass


def interpret(fa_result : [None]) -> str:
    pass




if __name__ == '__main__':
    # Write script here
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
