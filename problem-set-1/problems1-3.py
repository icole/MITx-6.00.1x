s = 'azcbobobegghakl'

count = 0
for char in s:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        count += 1

print "Number of vowels: " + str(count)


s = 'bobobobobobobobob'
start = 0
end = start + 3
count = 0
while end <= len(s):
    if s[start:end] == "bob":
        count += 1
    start += 1
    end = start + 3

print "Number of times bob occurs is: " + str(count)

s = 'tolbtmlqjptx'

sub = s[0]
longest = ""
for char in s[1:]:
    if char >= sub[-1]:
        sub += char
    else:
        if len(sub) > len(longest):
            longest = sub
        sub = char
    if len(sub) > len(longest):
        longest = sub

print "Longest substring in alphabetical order is: " + longest
