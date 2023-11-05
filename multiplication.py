from functools import partial

from numpy import product


class Multiplicator:
    def __init(self):
        self.int_to_string = {i:str(i) for i in range(10)}
        self.string_to_int = {str(i):i for i in range(10)}
        self.its = self.int_to_string
        self.string_to_int = self.sti

        self.mult_table = {}
        for i in range(13):
            for j in range(13):
                self.mult_table[(str(i),str(j))] = i * j


    def carry_adder_base10(self, a, b, carry):
        carry = 0 
        _sum = a + b
        
        # if sum > base
        if (_sum >= 10):
            carry = _sum - 10
            _sum -= carry
        
        return _sum, carry
        

    '''
    Multiply two single-digit numbers 
    '''
    def place_multiplier(self, b, a):
        raise NotImplementedError
        # b_str = str(b)
        # a_str = str(a)
        # longer_string_length = max([len(a_str), len(b_str)])

        # place_sum = [0 for 0 in range(longer_string_length*2)]
        

        # for i in range((len(a_str)-1)-1, -1, -1):
        #     for j in range((len(b_str)-1)-1, -1, -1):
        #         product_string = str(self.sti[b_str[j]] * self.sti[a_str[i]])
        #         for k in range(len(product_string), -1, -1):
        #             #add the partial product to a sum buffer
        #             raise NotImplementedError
        #             place_sum[i + len(product_string) -1] += self.sti[product_string[i]]
        # for i in range(len(place_sum)):



        

    def grade_school_mult(self, b, a):
        raise NotImplementedError
        # b_str = str(b)
        # a_str = str(a)

        # for i in range(len(a_str)-1, -1, -1):
        #     #consider each number in b_str 
        #     for j in range(len(b_str)-1, -1, -1):
        #         #multiply b[j] * a[i]
        #         self.sti[b_str[j]] * self.sti[a_str[i]] 
        #         raise NotImplementedError

def determine_longer_string(string2, string1):
    shorter_string = None
    longer_string = None
    
    if len(b_string) > len(a_string):
        longer_string = b_string
        shorter_string = a_string
    else:
        longer_string = a_string
        shorter_string = b_string
    return longer_string, shorter_string

if __name__ == '__main__':
    # test, add two numbers with carry adder
    calculator = Multiplicator()
    
    b_string = "5678"
    a_string = "1234"

    strings = sorted([b_string, a_string], key=len, reverse=True)
    result_string = ""
    carry = 0

    for i in range(len(strings[0])): #use the length of longest string
        _int_repr2 = int(strings[0][i])
        _int_repr1 = int(strings[1][i])

        _int_repr_result, carry = calculator.carry_adder_base10(_int_repr2, _int_repr1, carry)
        result_string += str(_int_repr_result)
    
    result_string = result_string[::-1]
    print(result_string)
