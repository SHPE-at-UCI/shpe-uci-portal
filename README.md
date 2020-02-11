# SHPE at UCI Member Portal

We will be using Flasks project tutorial found [here](http://flask.palletsprojects.com/en/1.1.x/tutorial/).

## Installation

#### [Python3](https://www.python.org/downloads/) & [pip](https://pip.pypa.io/en/stable/)

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies of the project.

Clone this project.

```bash
$ git clone https://github.com/SHPE-at-UCI/clubs.uci.edu.shpe.git
$ cd clubs.uci.edu.shpe
```

Create a virtualenv

```bash
$ python3 -m venv venv
```

Activate the virtualenv

```bash
$ . venv/bin/activate
```

Or on Windows cmd:

```
$ py -3 -m venv venv
$ . venv/Scripts/activate
```

Install Dependencies:

```
$ pip3 install -r requirements.txt
```

Run Flask
```
./runapp
```

You’ll see output similar to this:

```
* Serving Flask app "app"
* Environment: development
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 855-212-761
```

Stop Virtual Environment

```
$ deactivate
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

## License

[MIT](https://choosealicense.com/licenses/mit/)
