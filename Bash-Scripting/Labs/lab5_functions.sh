#!bin/bash
#
# Lab 5 - Functions and Libraries
#
# Revision History
#  - 2016-02-15 - Kayden Althen <kayden.althen@rackspace.com>
#   * Initial version
#

# Source library
source ./library.sh

# Argument processing

# LIMIT - how many times to print out the time/date
LIMIT=${1:-0}

# PRINTDATE - whether to show the date or not when printing out the time
#           - yes or no
PRINTDATE=${2:-yes}

# COUNTER - counter the amount of chimes
COUNTER=0

date '+It is currently %r'

while true ; do

    SECONDS=`date +%S`
    DELAY=$((60-$SECONDS))      # or DELAY=`expr 60 - $SECONDS`

    sleep $DELAY

    printdate $PRINTDATE        # moved this function into ./library

    limitcheck $LIMIT $COUNTER  # moved this function into ./library

done
