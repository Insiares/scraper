# 1- Install the CLI client

# 2- Set up your account

# 3- Write your Acornfile

# 4- Deploy your app

# 5- Monitor your app

# Notebook
shell command must have 
```sh
acorn ps #list of running apps
acorn login index.docker.io #login to a registry
acorn run index.docker.io/blable/image:version . #run tagged image from working directory

acorn build -t index.docker.io/insiares/scaper:main . #build tagged image from working directory
acorn push index.docker.io/insiares/scaper:main #push the imagine to registry
```

### running the acorn from dockerhub and ask for update notification
```sh
acorn run -n scraper --notify-upgrade index.docker.io/insiares/scaper:main
```
this does not work....

but i can run it ok from the image 
```sh 
acorn run index.docker.io/insiares/scaper:main 
```
it works ...

this works in CLI: 
```sh
acorn update --auto-upgrade damp-thunder index.docker.io/insiares/scaper:main
```

Will it work automatically if I push a new image? 
if i push the image in the cli it works
but the image pushed inside the GH workflows seems to cause a crashloop
simply because there was a bug :
- logs files exist in the working directory, and are pushed to the image when 
pushed from the CLI
- logs files are in the gitignore, causing a "folder not found" when pushed from GH actions
- problem fixed by adding a folder creation logic inside the logger module 
- hours wasted because of the "i'll do it later" nonsense
- why am i so dumb
- tl,dr it finally works as intended


### New acorn logics with mongodb as a service and a lighter docker env
acorn push index.docker.io/insiares/scraper_corn:main    
- this requires a rework from the ground up, not for this project iaa