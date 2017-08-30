##I don't like Python.

class Practice:

    word = input('Input a word: ')
    table = dict()

    def reverse(self):
        print ("The reverse of this word is: " + Practice.word[::-1])

    def count(self):
        for letter in Practice.word:
            if letter in Practice.table:
                Practice.table[letter] += 1
            else:
                Practice.table[letter] = 1

        print("Letter Count: ")
        print(Practice.table)


    def isPalindrome(self):
        if Practice.word == Practice.word[::-1]:
            print("This word is a palindrome.")
        else:
            print("This word is not a palindrome.")

run = Practice()
print(" ")
run.reverse()
print(" ")
run.count()
print(" ")
run.isPalindrome()


