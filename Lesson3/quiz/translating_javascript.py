# Valid Statements

# Translate the following JavaScript code to Python:

#        function mymin(a, b){
#            if (a < b){
#                return a;
#            } else {
#                return b;
#            };
#        }
#        
#        function square(x){
#            return x * x;
#        }
#        
#        write(mymin(square(-2), square(3)));


def mymin(a, b):
    if a < b:
        return a
    else:
        return b

def square(x):
    return x * x
    
print(mymin(square(-2), square(3)))