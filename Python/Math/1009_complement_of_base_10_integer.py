class Solution:
    def bitwiseComplement(self, N: int) -> int:
        '''
        0: 0 >> 1: 1 = 2 - 0 - 1
        
        1: 1 >> 0: 0 = 2 - 1 - 1
        
        2: 10 >> 01: 1 = 4 - 2 - 1
        3: 11 >> 00: 0 = 4 - 3 - 1
        
        4: 100 >> 011: 3 = 8 - 4 - 1
        5: 101 >> 010: 2 = 8 - 5 - 1
        6: 110 >> 001: 1 = 8 - 6 - 1
        7: 111 >> 000: 0 = 8 - 7 - 1
        
        8: 1000 >> 0111: 7 = 16 - 8 - 1
        9: 1001 >> 0110: 6 = 16 - 9 - 1
        10: 1010 >> 0101: 5 = 16 - 10 - 1
        11: 1011 >> 0100: 4 = 16 - 11 - 1
        12: 1100 >> 0011: 3 = 16 - 12 - 1
        13: 1101 >> 0010: 2 = 16 - 13 - 1
        14: 1110 >> 0001: 1 = 16 - 14 - 1
        15: 1111 >> 0000: 0 = 16 - 15 - 1
        
        16: 10000 >> 01111: 15 = 32 - 16 - 1
        '''
        
        def powerTwo(two: int, N: int) -> int:
            # Nearest multiple of 2
            while (two <= N):
                two *= 2
            return two
        
        return powerTwo(2, N) - N - 1
        
        '''
        # Without function
        compl = 2
        
        # Nearest multiple of 2
        while (compl <= N):
            compl = compl * 2
        
        return compl - N - 1
        '''
