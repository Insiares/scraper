<a name="readme-top"></a>

# Introduction

A guide to run your first acorn app, written with the best of my abilities (or lackthereof).

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="## 1- Install the CLI client">Install the CLI client</a>
            <ul>
        <li><a href="## On macOS and linux
">On macOS and linux
</a></li>
        <li><a href="# On Windows
">On Windows
</a>
</ul>
</li>
    </li>
    <li>
      <a href="# 2- Set up your account">Set up your account</a>
    </li>
    <li><a href="# 3- Write your Acornfile
">Write your Acornfile
</a>
<ul>
        <li><a href="## Prerequisites">Prerequisites
</a></li>
        <li><a href="## The basic Acornfile">The basic Acornfile</a>
</ul>
</li>
    <li><a href="# 4- Deploy your app">Deploy your app
</a></li>
<ul>
        <li><a href="## From your local directory">From your local directory
</a></li>
        <li><a href="## From a docker-hub image">From a docker-hub image</a>
</ul>
</li>
    <li><a href="# 5- Monitor your app">Monitor your app
</a>
<ul>
        <li><a href="## Monitoring running apps">Monitoring running apps</a></li>
        <li><a href="## Access the logs">Access the logs</a>
        </li>
        <li>
        <a href="## Running a shell inside the app">Running a shell inside the app</a></li>
        </ul>
<li><a href="# 6 - Becoming a CI/CD guru">Becoming a CI/CD guru</a>
    <ul>
    <li><a href="## Building and pushing acorn images from GH Actions">Building and pushing acorn images from GH Actions
</a></li>
<li><a href='## Running the app with autoupgrade.
'>Running the app with autoupgrade.
</a></li></ul>

</ol>
</details>
<br>
<br>



# 1- Install the CLI client

## On macOS and linux

you can install the client using Curl : 

```curl
curl https://get.acorn.io | sh
```

## On Windows

We need to install Scoop first : 
- Open a PowerShell terminal and enter:
```ps
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```
- Then install Acorn CLI : 
```ps
scoop install acorn
```
# 2- Set up your account

In a terminal : 
```sh
acorn login
```
Votre navigateur s'ouvre et vous demande une authentification Github.
Done.

# 3- Write your Acornfile
## Prerequisites
You should have written a functionnal Dockerfile for your application. Be avised that most of the issues you will face from now on will be caused by either your app or the Dockerfile declaration.

## The basic Acornfile

At the root of your project, create a file named "Acornfile".
Then fill it with the most basic instance: 

```CUE 
containers: app: {
        build: context: "."
        ports: publish: "{your_port}/http"
}
```
Replace {your_port} with the desired value. 
You can declare as many containers as you may need, and even call services such as database instance and such. Check out the acorn.io doc if you wish to explore more.



# 4- Deploy your app

Now that you have a running app, a well written dockerfile, and a simple acornfile, you can deploy your application inside an acorn sandbox. 
## From your local directory
In a terminal : 
```sh
acorn run -n {choose_a_name_for_your_app} .
```
With will deploy your app, and an online endpoint will be served directly inside the standard output of your terminal.

![App Screen Shot][product-screenshot]

You can check out your app online and share it with your mates! How cool is that?
<br>
Note that this is only temporary, most images stay online only a few hours.

## From a docker-hub image
If you wish to deploy your app from anywhere, you can push an image to your docker-hub (or ghcr) and run it from anywhere with Acorn CLI installed.
First, login to your Docker-Hub account : 
```sh
acorn login index.docker.io
```
You will be prompted to enter your username and dockerhub_token.
<br>
Then, build and tag your image:
```sh
acorn build -t index.docker.io/{your_username}/{your_repo_name}:{tag}
```
Change the value inside {} accordingly.
<br>
You can now push your image to your repo with:
```sh
acorn push index.docker.io/{your_username}/{your_repo_name}:{tag}
```
You can know run it directly from the repo.
```sh
acorn run --name {name_your_app} index.docker.io/{your_username}/{your_repo_name}:{tag}
```


# 5- Monitor your app

Once your app is running, you can monitor it, access its logs, and even access its shell to run commands.

## Monitoring running apps

You can simply access a list of your running apps using:
```sh
acorn ps
```

## Access the logs

You can access the logs of your apps using:

```sh
acorn logs {app_name}
```

If you wish to follow the output _"in real time"_, you can use the `-f` argument:
```sh
acorn logs -f {app_name}
```

## Running a shell inside the app

You can access the app and run commands by using:

```sh
acorn exec {app_name}
```

This will open a shell inside your app.

# 6 - Becoming a CI/CD guru

You can implement powerful automation for integration and deploiement using acorn and github actions.

## Building and pushing acorn images from GH Actions

You can automate the building of your image and push it on your Docker-hub repo each time you push a new version. If you reading this part, I will assume that you are familiar with GitHub Actions.

Add this job to your workflow:
```yml
  publish: 
    runs-on: ubuntu-latest
    permissions:
      packages: write
      contents: read

    steps:
    - name: Checkout repository
      uses: actions/checkout@v4.1.1
    
    - name : set up acorn
      uses: acorn-io/actions-setup@v1

    - name: login
      uses: acorn-io/actions-login@v1
      with: 
        registry : docker.io
        username : ${{ secrets.DOCKERHUB_USERNAME }}
        password : ${{ secrets.DOCKERHUB_TOKEN }}
      
    - name : build  
      run: |
        acorn build -t index.docker.io/${{ secrets.DOCKERHUB_USERNAME }}/[REPO_NAME]:[TAG] .
        acorn push index.docker.io/${{ secrets.DOCKERHUB_USERNAME }}/[REPO_NAME]:[TAG]
```
Modify the `[REPO_NAME]` and `[TAG]` accordingly.
<br>
This will build the image according to your Acornfile and Dockerfile, and push it to your repo.
<br>
NB : For this job to work, your dockerhub credential must be filled inside your Github repo settings. (i.e. Settings>Security>Actions>Repository Secrets)

## Running the app with autoupgrade.

With the proper github actions implemented, you can now run your app with the `--auto-upgrade` argument. This will allow for an automated upgrade of your app each time you push a new image. <br>
If your app is already up and running, you can switch it to auto-upgrade: 

```sh
acorn update --auto-upgrade {App_name} index.docker.io/{Dockerhub_username}/{repo_name}:{tag}
```

Or, you can pass this argument from the run step.
<br>
From your working directory: 
```sh
acorn run -n {App_name} --auto-upgrade index.docker.io/{Dockerhub_username}/{repo_name}:{tag}
```

From a image inside a repository:
```sh
acorn run --name {name_your_app} index.docker.io/{your_username}/{your_repo_name}:{tag} --auto-upgrade  index.docker.io/{your_username}/{your_repo_name}:{tag}
```

# Notebook
### This is just leftovers notes, nothing structured
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



<!-- Balises -->
[product-screenshot]: static/acorn_screen1.png
