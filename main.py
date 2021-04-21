def check_ID(id_num):
    sum_check = 0
    weight = 1
    
    if len(id_num) != 9:
        print("length is not valid")
      
    else
        for ch in id_num[0:-1]:
            digit = ord(ch) - ord('0')
            mult = weight * digit

            if mult > 9:  # if mult is two digit, then use the sum of the digits instead
                mult = int(mult / 10) + mult % 10

            sum_check += mult
            weight = 3 - weight  # switching between 1 and 2

        return ord(id_num[-1]) - ord('0') == 10 - (sum_check % 10)


print(check_ID("111111111"))
