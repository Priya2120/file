# Iss text ko question3.txt ke naam ki file mein save karo. 
# Iss file mein dhyaan se dekhoge toh ek insaan ka naam aur 
# ek sheher ka naam milegaYeh sheher woh sheher hai jisme woh 
# insaaan rehta hai. Ab aapne ek aisa code likhna hai jo: 1. 
# Delhi mein rehne waale logon ko ek alag file mein daale. 
# Delhi waali file ka naam "delhi.txt" hona chaiye. 2. 
# Shimla mein rehne waale logon ko ek alag file mein daale. 
# Shimla waali file na naam "shimla.txt" hona chaiye 
# 3. Aur saare log jo delhi aur shimla mein nahi rehte, 
# unko ek alag file mein daale. Iss file ka naam "others.txt" hona chaiye

file=open("delhi.txt","w")
file.write("Rohan-yadav\n")
file.write("tarun-saroha\n")
file=open("shimla.txt","w")
file.write("sonu-moun\n")
file.write("lucky=agrawal\n")
file=open("other.txt","w")
file.write("sapana-pandey\n")
file.write("nisha-batar\n")