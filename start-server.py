import subprocess, os, urllib.request, csv, socket       

# Connection variables
port = 25565
path = r'{}\start-server.bat'.format(os.getcwd())
local_ip_address = socket.gethostbyname(socket.gethostname())
external_ip_address = urllib.request.urlopen('https://ident.me').read().decode('utf8') 

# Launch text for server operator
def launch_instructions():
       new_local_ip = False
       new_external_ip = False
       # Open ip_address text file to see if external ip address has change
       with open("ip_address.txt") as file:
          local_ip, external_ip = next(csv.reader(file))
          new_local_ip = local_ip != local_ip_address
          new_external_ip = external_ip != external_ip_address
       # Text displayed to user
       print("/---------------------------------------/")
       print("Launch Instructions:\n")
       print("To launch from your PC type localhost in \ndirect connect\n")
       if new_local_ip:
              print("***WARNING NEW LOCAL IP ADDRESS***\n")
       print("For local players on the same network \nlaunch using {}\n".format(local_ip_address))
       if new_external_ip:
              print("***WARNING NEW EXTERNAL IP ADDRESS***\n")
       print("For external players launch using \n{}:{}\n".format(external_ip_address,port)) 
       print("/---------------------------------------/")
       # Update text file with new ip addresses
       with open("ip_address.txt", "w") as file:
              file.write("{},{}".format(local_ip_address, external_ip_address))

launch_instructions()

# Start server
subprocess.call([path])
