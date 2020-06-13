import subprocess, os, urllib.request, csv

# Connection variables
port = 25565
path = r'{}\start-server.bat'.format(os.getcwd())
ip_address = urllib.request.urlopen('https://ident.me').read().decode('utf8')

# Launch text for server operator
def launch_instructions():
       new_ip = False
       # Open ip_address text file to see if external ip address has change
       with open("ip_address.txt") as file:
          ip = next(csv.reader(file))
          if ip[0] != ip_address:
                 new_ip = True
       # Text displayed to user
       print("/----------------------------------------/")
       print("Launch Instructions:\n")
       print("To launch from your PC type localhost in \ndirect connect within multiplayer in game\n")
       if new_ip:
              print("***WARNING NEW IP ADDRESS***\n")
              # Update text file with new ip address
              with open("ip_address.txt", "w") as file:
                     file.write(ip_address)
       print("For external players launch using \n{}:{}\n".format(ip_address,port)) 
       print("/----------------------------------------/")

launch_instructions()

# Start server
subprocess.call([path])
