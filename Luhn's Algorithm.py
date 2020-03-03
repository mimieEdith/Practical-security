def creditcard():
    card_num = input ("Enter credit card number :") #prompts user for credit card input
    lcard_num = list(card_num)
    u_num = 0 # counting variable to verify number > 10
    cal_num = []

    check = 0
    if len(lcard_num)!= 16: # checks whether the card length is 16 
        print("This is an invalid credit card number") 
        
        quit()
        
    else:
            for i in range (len (lcard_num)):
                if ((i%2)==0):
                    num= int ((lcard_num[i]))*2
                    if num>=10:
                        u_num=num%10 +1
                        cal_num.append(num)#cal_num is sort of an array of variables for storing calculated values
                    else:
                        
                        cal_num.append(num) #.append means adding an element to an arrayor list

                else:

                    cal_num.append(int(lcard_num[i]))

    for n in range (len(cal_num)):
            check = check + cal_num[n]
            
            if (check%10==0): #checks if the remainder under modulo 10 is 0 i.e is the total divisible by 10
                print("This is a valid credit card")
                return("valid card number")
            else:
                print("This is an invalid card number")
                return("Invalid card number")



creditcard()



#output
#4137 8947 1175 5904 is invalid card number
#6499 8024 5027 3568 is invalid card number
#8504 1721 9127 3888 is invalid card number
#0043 6687 8348 5480 is valid card number
