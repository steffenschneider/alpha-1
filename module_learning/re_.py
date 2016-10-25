import re

## sub
# for replacing elements
string = "Example String"
replaced = re.sub('[ES]', 'a', string)
# print(replaced)  # axample atring
#
#
re.sub(r'\s+$', '', string, flags=re.M)  # re.M steht für re.MULTILINE
#
#
result = re.match(r"\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d", string)
if result is not None:
    pass

## match + search
# Python offers two different primitive operations
# based on regular expressions: re.match() checks for
# a match only at the beginning of the string, while
# re.search() checks for a match anywhere in the string !
re.match("c", "abcdef")  # No match
re.search("c", "abcdef")  # Match
#
#
pattern = r"\d"
string = 'abc222k2kkki3'
a = re.search(pattern, string)
print(a.group())  # 2, first number is 2

## findall
# matches all occurrences of a pattern, not just the first one as search() does
n_measurepoints = len(re.findall(r'<tr', string))

## finditer
text = "He was carefully disguised but captured quickly by police."
for m in re.finditer(r"\w+ly", text):
    print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
# 07-16: carefully
# 40-47: quickly


## group
m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
m.group(0)  # The entire match
# 'Isaac Newton'
m.group(1)  # The first parenthesized subgroup.
# 'Isaac'
m.group(2)  # The second parenthesized subgroup.
# 'Newton'
m.group(1, 2)  # Multiple arguments give us a tuple.
# ('Isaac', 'Newton')

## compile
pattern = r"\d"
string = "ölakdj8asdfnw380we"

prog = re.compile(pattern)
result = prog.match(string)
# is equivalent to
result2 = re.match(pattern, string)
# but if the pattern is used often, compile saves some time


## ?P<some_name>
# regular parentheses accessible via the symbolic group name 'name'
m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
m.group('first_name')  # 'Malcolm'
m.group('last_name')  # 'Reynolds'

## Syntax
r"""
.			Any single character; wildcard; joker
^			Start of string
$			End of string
\n			Newline
\r			Carriage return
\t			Tab
\0			Null character
// Quantifiers
a?			Zero or one of a	// siehe lazy-quatifier
a*			Zero or more of a
a+			One or more of a	// greedy quatifier --> siehe lazy-quantifier
a+?								// siehe lazy-quatifier
a{3}		Exactly 3 of a
a{3,}		3 or more of a					!
a{3,6}		Between 3 and 6 of a
a*			Greedy quantifier
a*?			Lazy quantifier
a*+			Possessive quantifier
// Group construcs
(...)		Capture everything enclosed		!!
(a|b)		Match either a or b		// I love (cats|dogs)
(?:...)		Match everything enclosed		!
(?>...)		Atomic group [possessive]
(?|...)		Duplicate subpattern group		!
(?#...)		Comment
(?'name'...)	Named capturing group
(?<name>...)	Named capturing group
(?P<name>...)	Named capturing group
(?imsxXU)	Inline modifiers
(?(...)|)	Conditional statement
(?R)		Recurse entire pattern
(?1)		Recurse first subpattern
(?+1)		Recurse first relative subpattern
(?&name)	Recurse subpattern `name`
(?P>name)	Recurse subpattern `name`
(?=...)		Positive lookahead	// wie ein Anker / anchor	!!
								// Monday\s(?=Tuesday)
								// --> Monday which is followed by a Tuesday
(?!...)		Negative lookahead	// Negative --> Verneinung
(?<=...)	Positive lookbehind
(?<!...)	Negative lookbehind
(*UTF16)	Verbs
(a(bc))		Capture subgroup
// Character classes
[abc]		A single character of: a, b or c
[^abc]		A character except: a, b or c
[a-z]		A character in the range: a-z
[^a-z]		A character not in the range: a-z
[a-zA-Z]	A character in the range: a-z or A-Z
[[:alnum:]]	Letters and digits
[[:alpha:]]	Letters
[[:ascii:]]	Ascii codes 0-127
[[:blank:]]	Space or tab only
[[:cntrl:]]	Control characters
[[:digit:]]	Decimal digits
[[:graph:]]	Visible characters (not space)
[[:lower:]]	Lowercase letters
[[:print:]]	Visible characters
[[:punct:]]	Visible punctuation characters
[[:space:]]	Whitespace
[[:upper:]]	Uppercase letters
[[:word:]]	Word characters
[[:xdigit:]]	Hexadecimal digits
//Meta sequences
\A			Start of string
\z			Absolute end of string
\s			Any whitespace character			!
\S			Any non-whitespace character
\d			Any digit
\D			Any non-digit
\w			Any word character
\W			Any non-word character
\b			A word boundary
\B			Non-word boundary
\G			Start of match
\X			Any unicode sequences
\C			Match one byte
\R			Unicode newlines
\v			Vertical whitespace character
\V			Negation of \v
\h			Horizontal whitespace character
\H			Negation of \h
\K			Reset match
\A			Start of string
\Z			End of string
\z			Absolute end of string
\n			Match nth subpattern
\pX			Unicode property X
\p{...}		Unicode property
\PX			Negation of \p
\P{...}		Negation of \p
\Q...\E		Quote; treat as literals
\k<name>	Match subpattern `name`
\k'name'	Match subpattern `name`
\k{name}	Match subpattern `name`
\gn			Match nth subpattern
\g{n}		Match nth subpattern
\g{-n}		Match nth relative subpattern
\g'name'	Recurse subpattern `name`
\g<n>		Recurse nth subpattern
\g'n'		Recurse nth subpattern
\g<+n>		Recurse nth relative subpattern
\g'+n'		Recurse nth relative subpattern
\xYY		Hex character YY
\x{YYYY}	Hex character YYYY
\ddd		Octal character ddd
\cY			Control character Y
[\b]		Backspace character					!
\			Makes any character literal
re*	Matches 0 or more occurrences of preceding expression.
re+	Matches 1 or more occurrence of preceding expression.
re?	Matches 0 or 1 occurrence of preceding expression.
ruby? 		Match "rub" or "ruby": the y is optional
ruby* 		Match "rub" plus 0 or more y
ruby+		Match "rub" plus 1 or more y
\d{3}		Match exactly 3 digits
\d{3,}		Match 3 or more digits
\d{3,5}		Match 3, 4, or 5 digits
Python(?=!)	Match "Python", if followed by an exclamation point
Python(?!!)	Match "Python", if not followed by an exclamation point
// my collection
[sS]teffen 				# shows steffen and Steffen in the text-file
^Steffen 				# Sentence starts with Steffen
Steffen$ 				# sentence ends with Steffen
^Steffen$				# only this word in the line
[0-9][0-9][0-9]$		# ends with three numbers
[A-Z]{1,2}				# word begin with one or two big letters
[A-Z][a-z]{2}			# One big letter followed bei to small letters
^$						# empty line
\.						# all items with a point
\?						# contains a question mark
^(file_.+)\.pdf$		# finds: file_hsad.pdf file_28wssj.pdf; just print the name before .pdf
([A-Z][a-z]{2}\s(\d{4}))	# Jan 1987 --> Jan 1987 1987
(\d{4})x(\d{3,4})		# 1280x720 --> 1280 720
<a.*?>.*?</a>			# find link; *? --> lazy-quatifier
\s*<.*?>\s*				# inner tags
href=\""(.*?)\""		# href="abc123"
(?:\d+[a-z]|[a-z]+\d)[a-z\d]*        // string contain numbers and letters
(?<!\|)&(?!\|)			# negative lookahead and lookbehind
-->                             # true if not |& |&| or &|
"""
