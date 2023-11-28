num = 38

def sum_digits(n):
    # Convert to string list
    string_list = list(str(n))

    # Convert to integer list
    int_list = [int(each) for each in string_list]
            
    # sum the list
    summary_digits = sum(int_list)

    # Check if n still has > 1 digits.
    if summary_digits >= 10:
        return sum_digits(summary_digits)
    else:
        return summary_digits

# Perform this function
res = sum_digits(num)

# Print result
print(res)