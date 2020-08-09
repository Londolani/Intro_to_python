def welcome():
    print("Welcome to the automated technical support system.")
    print("Please describe your problem:")
    
def get_input():
    return input().lower()

def support():
    dict = {'crashed':'Are the drivers up to date?','blue':'Ah, the blue screen of death. And then what happened?','hacked':'You should consider installing anti-virus software.','bluetooth':'Have you tried mouthwash?','windows':'Ah, I think I see your problem. What version?','apple':'You do mean the computer kind?','spam':'You should see if your mail client can filter messages.','connection':'Contact Telkom.'}
    
    welcome()
    prob = get_input()
    
    while prob != 'quit':
        if prob == 'crashed':
            prob = input(dict['crashed']+'\n')
        elif prob == 'blue':
            prob = input(dict['blue']+'\n')
        elif prob == 'hacked':
            prob = input(dict['hacked']+'\n')
        elif prob == 'bluetooth':
            prob = input(dict['bluetooth']+'\n')
        elif prob == 'windows':
            prob = input(dict['windows']+'\n')
        elif prob == 'apple':
            prob = input(dict['apple']+'\n')
        elif prob == 'spam':
            prob = input(dict['spam']+'\n')
        elif prob == 'connection':
            prob = input(dict['connection']+'\n')
        else:
            prob = input("Curious, tell me more.\n")
            
def main():
    support()
if __name__=="__main__":
    main()