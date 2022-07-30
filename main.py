from dotenv import load_dotenv
import os
 
# Use load_env to trace the path of .env:
load_dotenv('.env') 
 
# Get the values of the variables from .env using the os library:
password = os.environ.get("App_password")
languageVersion = os.environ.get("Python_version")
random = os.environ.get("privatekey")
print(password)
print(random)
print(languageVersion)

