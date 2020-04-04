# SHPE at UCI Member Portal

We will be using Flasks project tutorial found [here](http://flask.palletsprojects.com/en/1.1.x/tutorial/).

## Install & Run

#### 1) Install

Assuming you already cloned this repo.

Run the command below on the root directory of the repo to create the virtual environment and install the dependencies.

###### Windows

```
$ ./install-windows
```

###### Linux & Mac

```
$ ./install-linux
```

**Note:** You will need to create a .env file in the root directory. Contact an administrator of the repo to get it and copy its contents to your .env file. Link can be found here: [file](https://shpetechcommittee.slack.com/archives/C011D0TD154)

#### 2) Run Web App

On the root directory, run the following commands

```
./runapp
```

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
