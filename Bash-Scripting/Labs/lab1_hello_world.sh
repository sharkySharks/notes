#!/bin/bash
#
# Lab 1 - Simple hello world example
#         Testing basic output concepts
#
# Revision History
#  - 2016-02-15 - Kayden Althen <kayden.althen@rackspace.com>
#   * Initial version
#

echo "Hello $LOGNAME.  Welcome to the world of scripting."  # grab the environment variable for the user
echo -n "The current date is "

date '+%A, %B %d, %Y.'  # custom format for the date
