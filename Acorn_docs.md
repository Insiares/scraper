# 1- Install the CLI client

# 2- Set up your account

# 3- Write your Acornfile

# 4- Deploy your app

# 5- Monitor your app

shell command must have 

acorn ps
acorn login index.docker.io
acorn run index.docker.io/blable/image:version .

acorn build -t index.docker.io/insiares/scaper:main .
acorn push index.docker.io/insiares/scaper:main


### running the acorn from dockerhub and ask for update notification
acorn run -n scraper --notify-upgrade index.docker.io/insiares/scaper:main
this does not work....

but i can run it ok from the image 
acorn run index.docker.io/insiares/scaper:main 
it works 

this works in CLI: 
acorn update --auto-upgrade damp-thunder index.docker.io/insiares/scaper:main
Will it work automatically if I push a new image? 
if i push the image in the cli it works
but the image pushed inside the GH workflows seems to cause a crashloop



# New acorn logics with mongodb as a service and a lighter docker env
acorn push index.docker.io/insiares/scraper_corn:main    
