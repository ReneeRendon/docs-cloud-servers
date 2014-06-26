#!/usr/bin/env python

import os, fnmatch
import git
from sys import argv
import shutil

PREFIX = "PREFIX"
PRODUCTNAME = "PRODUCTNAME"
VERSION = "v1.0"
prompt = '> '

print "Enter the product name (for example, \"Cloud CDN\"): " 
PRODUCTNAME = raw_input(prompt)

print "Enter the product name prefix (for example \"cdn\"): "
PREFIX = raw_input(prompt)

print "Enter the product version (for example \"v1.0\"): "
VERSION = raw_input(prompt)

def findReplace(directory, find, replace, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
            s = s.replace(find, replace)
            with open(filepath, "w") as f:
                f.write(s)

scriptdir = os.path.dirname(os.path.realpath(__file__))

findReplace(scriptdir, "PREFIX", PREFIX, "*.xml")
findReplace(scriptdir, "PRODUCTNAME", PRODUCTNAME, "*.xml")
findReplace(scriptdir, "VERSION", VERSION, "*.xml")

os.rename( scriptdir + '/src/docbkx/PREFIX-gettingstarted.xml', scriptdir + '/src/docbkx/' + PREFIX + '-gettingstarted.xml')
os.rename( scriptdir + '/src/docbkx/PREFIX-releasenotes.xml', scriptdir + '/src/docbkx/' + PREFIX + '-releasenotes.xml')
os.rename( scriptdir + '/src/docbkx/PREFIX-devguide.xml', scriptdir + '/src/docbkx/' + PREFIX + '-devguide.xml')

README = open( scriptdir + '/README.md', "w")
README.write( PRODUCTNAME + " README") 
README.write( "======================") 
README.close

g = git.cmd.Git( scriptdir ) 
g.add( scriptdir + '/src/docbkx/' + PREFIX + '-gettingstarted.xml' )
g.add( scriptdir + '/src/docbkx/' + PREFIX + '-releasenotes.xml' )
g.add( scriptdir + '/src/docbkx/' + PREFIX + '-devguide.xml')

print "============================"
print "Now run:"
print "git init ."
print "git remote add origin git@github.com/rackerlabs/docs-cloud-" + PREFIX + ".git"
print "git push origin master"
print "Be sure to create the corresponding repo first."

os.remove( scriptdir + '/initialize.py')
shutil.rmtree( scriptdir + '/.git')
