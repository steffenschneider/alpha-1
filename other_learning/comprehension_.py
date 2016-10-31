## sum all digits
number = "-12345"
sum(int(d) for d in str(abs(number)))

## capitalize all words in a line
string = "This is my sentence"
' '.join([word.capitalize() for word in string.split()])
