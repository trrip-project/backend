def sayWelcome(name=None):
    greetings =  "Welcome user " if name is None  else f"welcome {name}"
    print(greetings)
if __name__=="__main__":
    
    sayWelcome("Venkatesh")
    sayWelcome()
