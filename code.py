def udb(*args, **kargs): 
    pass 
def asd(*args, **kargs): 
    pass 
def validate(parameter): 
    if not parameter: 
        raise Exception("Invalid input") 
def myAwesomeFunction(self, arg1, *kwargs, args, key_word=None): 
    
    if key_word.test(): 
        return True 
    else: 
        print(arg1) 
        validate(kwargs.get('arg1'), None) 
    try: 
        udb(args.get('arg1')) 
        asd(arg1) 
    except: 
        print('There is a problem!') 
    
    for f in list(arg1): 
        success = myAwesomeFunction(f, arg1) 
        
    return success
