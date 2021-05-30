# Aapke paas ek list hai. Iss list mein har string ko ek file-question3.txt 
# naam ki file mein nayi line mein daalo. Aapki list yeh rahi:


bank_list=["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"] 
file=open("file_bank","w")
i=0
while i<len(bank_list):
    file.write(bank_list[i])
    file.write("\n")
    i=i+1
file.close()