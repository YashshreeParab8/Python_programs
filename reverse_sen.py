def reverse_words(input_string):
    words = input_string.split()
    reversed_words = words[::-1]
    reversed_string = ' '.join(reversed_words)
    return reversed_string
input_string = "This is a sample sentence"
reversed_string = reverse_words(input_string)
print(reversed_string) 
