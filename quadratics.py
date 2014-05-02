def quadratic():

    exp=input('Enter a quadratic expression in the form x^2+bx+c:  ')

   #determines if input is a valid quadratic expression 
    exponents=''
    for i in range(len(exp) - 1):
        if exp[i] == "^":
            exponents=exponents+exp[i+1]

    if "2" in exponents and len(exponents)==1:
        factored(exp)
        
    #rejects invalid expression and prompts user for another
    else:
        print ("This is not a valid quadratic expression.")
        quadratic()


#split takes the string input, splits into terms, finds the b and c coefficients
def split(exp):
    global b
    global c
    
    expression = exp.replace(" ", "")
    
    terms_list = expression.replace("-","+-")
    terms_list = terms_list.split('+')

    del terms_list[0]

    #deals with the case of b=0
    if len(terms_list)==1:
        terms_list.insert(0, '0x')
        
    
    b_term=terms_list[0]
    b_term=b_term[:-1]
    
    b = int(b_term)
    c = int(terms_list[1])
    






def factored(exp):
    
    import math

    split(exp)
    
    #makes a list of all positive factors of c
    c_factors=[]
    if c>0:
        for i in range(1,c+1):
            if c%i==0:
                c_factors.append(i)

    #makes a list of all factors of c, positive and negative
    elif c<0:
        for i in range(c,0):
            if c%i==0:
                c_factors.append(i)
                c_factors.append(i*-1)
                


    #remaining section pairs and adds corresponding factors to find the pair that adds to b

    n=len(c_factors)-1

    #this loop is for the difference of two squares
    if b==0:
        factor1=int(math.sqrt(abs(c)))
        print('(x+' + str(factor1) + ')(x-' + str(factor1) + ')')
        
     #this loop is for all other cases
     #adds first factor in the list with the last factor, compares to |b|,then goes to next factor
            #and penultimate factor and so on, then determines the right pair of factors
    else:
        final=[]
        for i in c_factors:
            if i+c_factors[n] == abs(b):
                factor1 = i
                factor2 = c_factors[n]
                final.append(factor1)
                final.append(factor2)
            n=n-1

        #asking if final list is empty tells us if the expression can be factored
        if len(final)==0:
            print('This quadratic expression cannot be factored. Try the quadratic formula.')
            quadratic()

        if c>0:
            
            if b>0 and factor1 != factor2:
                print('(x+' + str(factor1) +')(x+' + str(factor2) + ')')
            elif b>0 and factor1==factor2:
                print('(x+' + str(factor1) + ')^2')

        
            elif b<0 and factor1 != factor2:
                print('(x-' + str(factor1) +')(x-' + str(factor2) + ')')
            elif b<0 and factor1==factor2:
                print('(x-' + str(factor1) + ')^2')

        if c<0:

            if b<0:
                print('(x' + str(-1*factor2) +')(x+' + str(abs(factor1)) + ')')
            if b>0:
                print('(x+' + str(abs(factor2)) +')(x-' +str(-1*factor1) + ')')  
        
 



    
