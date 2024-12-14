def isPalindromealindrome():
    input = input("Type a input: ")
    
    isPalindrome = True

    for i in range(len(input) // 2):
        if input[i] != input[-(i + 1)]:
            isPalindrome = False
            break

    if isPalindrome:
        print("Yes, it's a palindrome.")
    else:
        print("No, it's not a palindrome.")

isPalindromealindrome()
