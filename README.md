# CMSC 491
 Developed By,  
 Joshua Standiford, Daniel Kelly, Malik Jackson

Baltimore Crime Data Analysis
-
This project is for CMSC491.  The purpose of this project is to provide visual representation of crime data in baltimore.  As well as find various predictors of crime in baltimore. 

Prerequisites
-
* Oracle Virtualbox - https://www.virtualbox.org/wiki/Downloads
* (Windows only) GitBash - https://git-scm.com/downloads
* Vagrant -     https://www.vagrantup.com/downloads.html
* Vagrant Plugins
* GitHub - https://github.com
* Python 3 - https://www.python.org/download/releases/3.0/

    (These links we're the most recent versions as of 10/13/2017)
    If you're unfamiliar with the Git tools.  A handy learning tool is available here.
    https://try.github.io/levels/1/challenges/1
    
Installation
-
* VirtualBox 

    <b>NOTE</b> before installing <u>Virtualbox</u>.  Enable virtualization within your BIOS or OS.
    Installing virtualbox should be straight forward.  
    
* GitBash 

    GitBash client is only necessary for Windows users.  If you are on a Mac or Linux device you can skip
    this step.  Otherwise navigate through the link above.  The steps as well should be pretty straight forward.
    <b>Note: </b> On windows you may encounter issues with GitBash unless you operate as Administrator.
    This can be achieved by right-clicking on the program before running and hitting
    "Run as Administrator".  
    
* Vagrant
    
    Again, installation should be rather straight forward.  However all machines are different so pay attention
    as you install in case any errors should occur.  
    
* GitHub

    Most importantly having a github account will be the means of cloning and allowing you to
    use this project.
    On the website, create an account.  This will be essential for being able to clone and use the code. 
    
    In the GitBash you will want to now clone this repository.  You can achieve that by running the command:
    
        "git clone git@github.com:linkvetern64/CMSC491.git" for ssh
        "git clone https://github.com/linkvetern64/CMSC491.git" for https
        
    
* Vagrant Plugins

    Once you have Vagrant and GitBash installed.  Open the GitBash CLI and type in
        
        "vagrant plugin install vagrant-hostsupdater" 
        "vagrant plugin install vagrant-hostmanager"
    
    -- hostsupdater is at (version. 1.0.2) as of 9/30/2017
    
    -- hostmanager is at (version. 1.8.7) as of 9/30/2017

* Python 3
    
    Installing Python 3 should be very simple as well.  Just follow the installer until the end.
    
Executing
-
Now that we have all the dependencies installed.  through the GitBash or CLI enter the cloned git-repo
you cloned above.  

This can be accomplished using the "cd" command.  Once you enter the folder, you should now be able to run
    
    "vagrant up"
    
If this does not work.  Make sure you see a file called Vagrantfile.  This file is how vagrant knows how to initialize itself.
now wait until Vagrant finishes filling up the terminal with output.

you can now open up your web browser and in the navigation bar enter "crime-data.dev".
This will take you to the local server Vagrant initialized with the git project loaded.

In order to turn off the Vagrant VM and shutdown the server simply run.

    "vagrant destroy"
    

Project Specifications
-

This project (CMSC491) was created using:
 * Php5 backend
 * Prototype AJAX framework
 * BootStrap CSS Framework
 * Javascript ES6 
 * HTML5
 * Intellij IDE 2017.2.2
 * PyCharm IDE
 * Google Maps API
 * OpenBaltimore Data
 

How to Operate
-
-- Index.php --     
    To be written.

-- PreProcessor.py --
    To be written.

Description
-
This project is written in Python3 with a web interface currently using a LAMP stack.
The purpose of this project is to attempt to find correlations with crime in baltimore and external factors.
Contained in the project is a data pre-processing framework which will clean noisy data from the sources.
The information after it is processed will be loaded into the main python file which will
process the information.  The data will be correlated and a snapshot will be exported and loaded
into the web interface for visualized results and heat-map generation. 

Data Sources
-
OpenBaltimore Data Center - https://data.baltimorecity.gov
OpenBaltimore Crime Data - https://data.baltimorecity.gov/browse?category=Crime
OpenBaltimore Vacant Housing Data - https://data.baltimorecity.gov/Housing-Development/Vacant-Buildings/qqcv-ihn5
AccuWeather JSON Stream & API - https://downloads.accuweather.com


Testing
-
To be written.


Known Bugs / Fixes
-
Content unavailable.

Authors
-
Joshua Standiford
Daniel Kelly
Malik Jackson


    
  