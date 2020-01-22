# SHPE at UCI Member Portal

We will be using Flasks project tutorial found [here](http://flask.palletsprojects.com/en/1.1.x/tutorial/).

## Installation

#### [Python3](https://www.python.org/downloads/) & [pip](https://pip.pypa.io/en/stable/)

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies of the project.

Clone this project.

```bash
$ clone https://github.com/SHPE-at-UCI/clubs.uci.edu.shpe.git
$ cd clubs.uci.edu.shpe
$ python3 -m venv venv
$ . venv/bin/activate
```

Create a virtualenv and activate it:

```bash
$ python3 -m venv venv
$ . venv/bin/activate
```

Or on Windows cmd:

```
$ py -3 -m venv venv
$ venv\Scripts\activate.bat
```

Install Flaskr:

```
$ pip install -e .
```

For Linux and Mac:

```
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
$ flask run
```

For Windows cmd, use set instead of export:

```
> set FLASK_APP=flaskr
> set FLASK_ENV=development
> flask run
```

For Windows PowerShell, use \$env: instead of export:

```
> $env:FLASK_APP = "flaskr"
> $env:FLASK_ENV = "development"
> flask run
```

You’ll see output similar to this:

```
* Serving Flask app "flaskr"
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


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
