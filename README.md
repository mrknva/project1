# project1
A check digit for a sequence of digits or letters is “a form of redundancy check used for error detection on identification numbers, such as bank account numbers, which are used in an appli- cation where they will at least sometimes be input manually”1. It consists of one or more digits computed by an algorithm from the other digits (or letters) in the sequence. With a check digit, one can detect simple errors in a sequence of characters (usually digits) such as a single mistyped digit or some permutations of two successive digits.
The NorthStar College implements also a check digit algorithm for student numbers. A student number has exactly four digits. The smallest student number is "0001" . The zeros are part of the number and are not omitted. Given such four digits as a student number, a check digit is calculated, and appended with a dash sign to the four digits to form the student ID.
Let us denote a student number as:
d1d2d3d4
Then, the check digit for the NorthStar College is computed as:
CheckDigit=(2×d1+3×d2+5×d3+7×d4) mod11 An uppercase ‘X’ is used for a value of 10 of the CheckDigit.
Take as example the student number 6792:
CheckDigit = (2×6+3×7+5×9+7×2) mod 11 = 92 mod 11
=4
The check digit of the student number 6792 is found to be 4. Therefore, similar to your
student IDs, this is written as 6792-4. 1Definition taken from Wikipedia.
 
PROBLEM & SPECIFICATIONS
Your mission, should you choose to accept it, is to determine the digit that is missing from a student-id or, if no digit is missing, to determine whether it is valid or not. A student ID will be read from the standard input as:
####-#
where each # is a decimal digit or a ‘?’ (question mark). There will be at most one question mark. It is also possible that no question mark appears in the input. You will be printing a single line of output which strictly follows the following specifications:
• There is no question mark: Print VALID if the check digit is correct. Otherwise, print INVALID.
• CheckDigit position has question mark: Compute the check digit and print the whole student ID (with the correct check digit present).
• One of the first six digit positions has question mark: Compute the digit position that has question mark and print the whole student ID (with the correct digit present).
You are not allowed to:
• Define functions.
• Use any kind of repetitive constructs.
• Insert-digit-and-test until you find the correct digit. This is not allowed. We will look into your code! You have to find one (or a group of) formula(s) for determining what the ‘?’ mark stands for.
