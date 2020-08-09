def welcome():
    print("Welcome to the automated technical support system.")
    print("Please describe your problem:")
    
def get_input():
    return input().lower()


def techsupport():
    dict = {'crashed':'Are the drivers up to date?','blue':'Ah, the blue screen of death. And then what happened?','hacked':'You should consider installing anti-virus software.','bluetooth':'Have you tried mouthwash?','windows':'Ah, I think I see your problem. What version?','apple':'You do mean the computer kind?','spam':'You should see if your mail client can filter messages.','connection':'Contact Telkom.'}
    
    welcome()
    prob = get_input()
    
    while prob != 'quit':
        p = prob.split()
        counter = 1
        for i in p:
            if i in dict.keys():
                print(dict[i])
                break
            elif(i not in dict.keys() and counter == len(p)):
                print('Curious, tell me more.')
                break
            counter +=1
        prob = get_input()
                              
def main():
    techsupport()
if __name__=="__main__":
    main()