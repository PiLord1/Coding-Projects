input_string = input('Enter a string without spaces: ')
s = [*input_string]
counter = 1
max_counter = 1
new = []
longest = []

if len(s)==len(set(s)):
    s_to_string = ''.join(s)
    print('The answer is "' + s_to_string + '" with the length of ' + str(len(s)))

else:
    for i in range(len(s)):
        if s[i] in new:
            counter=1
            if len(longest)<len(new):
                longest = new
            new = []
            new.append(s[i])
        else:
            if len(new)!=0:
                counter+=1
            new.append(s[i])  
            if max_counter < counter:
                max_counter=counter
    if len(longest)<len(new):
                longest = new

    s_to_string = ''.join(longest)
    print('The answer is "' + s_to_string + '" with the length of ' + str(max_counter))



