# Riley Flanagan - 2011275 
# COSC312 Assignment 1
# 14/08/2023

# Program to determine possible key lengths from Cryptonian ciphertext

# At any index within the key length, for all multiples of the key length (i.e. index 0 of every multiple of the keylength);
# if every possible key neighbour difference results in an invalid output, across any index repeated over the ciphertext in multiples of the key length,
# then the key length specified is not possible.

def derive_key_length(ciphertext, min_len, max_len):
    clen = len(ciphertext)-1
    for klen in range(min_len, max_len+1):
        i = 0
        valid_len = True
        # For every index of a keylength
        diffs = []
        while i < klen and valid_len: 
            x = i
            valid_diffs = [0,1,2,3,4,5,6,7,8,9]
            # For every keylength repetition within the ciphertext
            while x < clen and valid_len:
                # Find invalid key value difference
                invalid_diff = (int(ciphertext[x]) - int(ciphertext[x+1]))
                # Cannot use modulo due to cyclic nature of Vigneres
                if invalid_diff < 0:
                    invalid_diff += 10
                if invalid_diff in valid_diffs:
                    valid_diffs.remove(invalid_diff)
                x += klen
                if not valid_diffs:
                    valid_len = False
            if valid_diffs:
                diffs.append(valid_diffs)
            i+=1
        if valid_diffs:
            print(klen, diffs)
    return


print(derive_key_length("3533417796556389436161124078508958715029955677257458827883108401002464034055011585735012213975196298046797672133876903333020629414330684419751448764324148830901502424394312176140164325849400617671834594624641228755742894729133874040662100627113839838065679431194880917335338594495789472601233325534127954254233135496601593920966979856653529267774727809345694199267712815265149440829554159843003340687", 
                        1, 20))

# Valid key differences remaining for key length 11:
#   {[2, 7], [7], [3], [6], [6], [7], [6], [1], [2], [8], [2]}
# i:  0       1    2    3    4    5    6    7    8    9    10
