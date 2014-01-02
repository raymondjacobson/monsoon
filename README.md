# Monsoon

Unlimited cloud storage.
Automagically infinite space to organize your content.

## Installation

1. Create a "master" dropbox account to run your application.
2. Visit the developer site app console (https://www.dropbox.com/developers/apply?cont=/developers/apps) and create a Dropbox API app with files and datastores (the next option is up to you). Make sure you select all file types.
3. Give your app a name (it doesn't matter)
4. Copy the demo config_demo.py file, rename it to config.py, and replace the
appropriate app key and app secret using the ones provided to your app in the dropbox app console.
5. You'll need an instance of mongodb running. http://docs.mongodb.org/manual/installation/
6. Then, execute the following:

```
git clone git@github.com:raymondjacobson/monsoon.git
cd monsoon
npm install -g phantomjs # requires node.js
pip install -r requirements.txt
python monsoon.py
```

## Usage

Until this project gets built out further, the interface is rather simple.

```
usage: monsoon [-h] action file

positional arguments:
  action      either 'put' or 'grab' a file into the cloud
  file        file to commit action on

optional arguments:
  -h, --help  show this help message and exit
```

Example:

```
python monsoon.py put file.txt # uploads a file (making a new account if necessary)
python monsoon.py grab file.txt # gets the public and downloadable links for the file
```

## Notes

1. Each time monsoon needs to generate a new dropbox account, it takes a little time. Be patient on the first run and every time you use up 2 gigs.
2. There is one caveat -- dropbox links expire January 1, 2030. you'll have to redo everything at that point and you might lose some stuff. Sorry.

## Coming Up

1. Fuzzy search to make finding the right files easier
2. Possible simple front-end interface built around fuzzy search and/or cocoa app, etc.
3. Better folder support

## Thanks

Inspired by a project I worked on called cumulus.af (https://github.com/unblevable/cumulus.af) at hackMIT fall 2013.
Special thanks to Brian Le (@unblevable) and Alex Freska (@alexfreska)

