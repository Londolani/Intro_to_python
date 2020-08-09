import random

def welcome():
    print("Welcome to the automated technical support system.")
    print("Please describe your problem:")
    
def get_input():
    return input().lower()

def somehelp():
    Q_A = {1:"Have you tried it on a different operating system?",2:"Did you reboot it?",3:"What colour is it?",4:"You should consider installing anti-virus software.",5:"Contact Telkom.",6:"I should get that looked at if I were you."}
    
    print("Welcome to the automated technical support system.")
    prob = input("Please describe your problem:\n")
    
    while prob != 'quit':
        ran = random.randint(1,6)
        if ran == 1:
            prob = input(Q_A[1]+'\n')
        elif ran == 2:
            prob = input(Q_A[2]+'\n')
        elif ran == 3:
            prob = input(Q_A[3]+'\n')
        elif ran == 4:
            prob = input(Q_A[4]+'\n')
        elif ran == 5:
            prob = input(Q_A[5]+'\n')
        elif ran == 6:
            prob = input(Q_A[6]+'\n')
                    
def main():
    somehelp()
if __name__=="__main__":
    main()