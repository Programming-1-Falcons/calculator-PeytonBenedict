while True:   
    operation = input("Enter operation (+, -, *, /, **, //, %): ")      
      
    num1 = float(input("Enter the first number: "))      
    num2 = float(input("Enter the second number: "))      
      
    if operation == '+':      
        result = num1 + num2      
    elif operation == '-':      
        result = num1 - num2      
    elif operation == '*':      
        result = num1 * num2      
    elif operation == '/':      
        if num2 == 0:      
            print("Can't divide by zero.")      
  
        result = num1 / num2      
    elif operation == '**':      
        result = num1 ** num2  
    elif operation == '//':
        result = num1 // num2
    elif operation == '%':
        result = num1 % num2
    else:    
        print("Choose a valid operation.")    

  
    print("Your equation is " + str(num1) + " " + operation + " " + str(num2) + " = " + str(result))