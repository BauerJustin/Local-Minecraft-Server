import subprocess, os, urllib.request, csv, socket       

# Connection variables
port = 25565
path = r'{}\start-server.bat'.format(os.getcwd())
external_ip_address = urllib.request.urlopen('https://ident.me').read().decode('utf8')
local_ip_address = socket.gethostbyname(socket.gethostname()) 

# Launch text for server operator
def launch_instructions():
       new_ip = False
       # Open ip_address text file to see if external ip address has change
       with open("ip_address.txt") as file:
          ip = next(csv.reader(file))
          new_ip = ip[0] != external_ip_address
       # Text displayed to user
       print("/---------------------------------------/")
       print("Launch Instructions:\n")
       print("To launch from your PC type localhost in \ndirect connect\n")
       print("For local players on the same network \nlaunch using {}\n".format(local_ip_address))
       if new_ip:
              print("***WARNING NEW EXTERNAL IP ADDRESS***\n")
              # Update text file with new ip address
              with open("ip_address.txt", "w") as file:
                     file.write(external_ip_address)
       print("For external players launch using \n{}:{}\n".format(external_ip_address,port)) 
       print("/---------------------------------------/")

launch_instructions()

# Start server
subprocess.call([path])
