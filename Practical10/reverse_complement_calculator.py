#define the fuction
def reverse_complement_calculator(seq) :
    #turn the string into list
    list_seq=list(seq)
    #creat an empty list to store the result
    complement_seq=""
    #define the priciple to change the seq into the reverse ones
    for i in range(len(seq)):
            if seq[i] == "A" or seq[i] == "a":
                list_seq[i] = "T"
            elif seq[i] == "C" or seq[i] == "c":
                list_seq[i] = "G"
            elif seq[i] == "G" or seq[i] == "g":
                list_seq[i] = "C"
            else:
                list_seq[i] = "A"
    #print the reverse complement sequence
    complement_seq = "".join(list_seq)
    return print(complement_seq)

#set up an example
reverse_complement_calculator("AGGactGCTCGAT")
