# SHPE at UCI Member Portal

We will be using Flasks project tutorial found [here](http://flask.palletsprojects.com/en/1.1.x/tutorial/).

## Installation

#### 1) Docker

We will be using Docker containers. You will need to install it before you proceed.

https://www.docker.com/products/docker-desktop

To check if you installed it correctly, run this command in the terminal or GitBash.

```
$ docker
```

You should see a list of docker commands

#### 2) Build & Run Docker container 

On the root directory, run the following commands

###### Windows
Build
```
$ docker build -t shpeapp:latest .
```
Run
```
$ docker run -p -i 5000:5000 shpeapp:latest //bin/bash -c "flask create_tables; flask run --host=0.0.0.0"
```

???

Profit.

---
###### Linux & Mac
Build
```
$ docker build -t shpeapp:latest .  
```

Run 
```
docker run -i -t -p 5000:5000 shpeapp:latest /bin/bash -c "flask create_tables; flask run --host=0.0.0.0"
```
???

Profit.

#### 3) Exiting Docker Container

Control C method
```
Crtl-c
```

To see if your container is still running do
```
docker ps
```

If you see the "shpeapp:latest" image listed, use this command to shut down the container.

```
$ docker container kill $(docker ps | grep "shpeapp" | awk '{print $1}')
```


### Important: Whenever you pull from master, always build the container, there may be changes to the image!

### Contributing

We use a feature branch workflow.

Step 1: Create a new branch

```
git checkout -b <feature_milestone#>
Examples: git checkout -b Login_Feature_1.1
```

Step 2: Update, add, commit, and push changes

```
git status
git add <some-file> or git add .
git commit
```

Step 3: Push feature branch to remote

```
git push -u origin new-feature
Step 4: Create a pull request
```

## Development

Create a pull request(PR) on the master branch.
Once the PR is approved, the owner of the PR merges the pull request into master branch.
In the future we will have continuous deployments.

## Tutorial

Made by Guillermo Hernandez - SHPE Technical Program Manager
[Link](https://www.youtube.com/watch?v=T0Ml5WnQbJY&feature=youtu.be)

## Resources
http://flask.palletsprojects.com/en/1.1.x/tutorial/
https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application


## License

[MIT](https://choosealicense.com/licenses/mit/)
