def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    

def even(n):
    return n % 2 == 0

# print(factorial(5))

# git --version
# git init 
# git config --global user.name "Your Name"
# git config --global user.email "youremail@example.com"
# git add new.py
# git status
# git commit -m "Version -1"    
# git log