def romanToInt(s):
    alien_numerals = {
        'A': 1, 'B': 5, 'Z': 10, 'L': 50, 'C': 100, 'D': 500, 'R': 1000
    }
    
    result = 0
    prev_value = 0  
    for char in s[::-1]:
        value = alien_numerals[char]
        
        if value < prev_value:
            result -= value  
        else:
            result += value
        
        prev_value = value
    
    return result


# Function to get user input and display the result
def convert_alien_numeral():
    alien_numeral = input("Enter an Alien numeral: ")
    result = romanToInt(alien_numeral)
    print(f"The integer value of {alien_numeral} is: {result}")

# Run the conversion
convert_alien_numeral()


