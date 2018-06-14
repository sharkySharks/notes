#!bin/bash
#
# Lab 4 - Looping, announce every minute as it strikes, accepts a parameter for the amount of times
#         to run before exiting
#
# Synopsis:
#   lab4_looping_with_parameters.sh [COUNT]
#   lab4_looping_with_parameters.sh [COUNT] [SHOWDATE]
#
# Revision History
#  - 2016-02-15 - Kayden Althen <kayden.althen@rackspace.com>
#   * Initial version
#

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
    DELAY=`expr 60 - $SECONDS`  # or DELAY=$((60-$SECONDS))

    sleep $DELAY
    if [ $PRINTDATE = 'yes' ]; then
        date '+It is %l:%M %p, %B %d, %Y!'
    else
        date '+It is %r!'
    fi

    if [ $LIMIT -ne 0 ]; then          # if the default is given, 0, then no need to check the limit
        COUNTER=$(($COUNTER + 1))
        if [ $COUNTER -eq $LIMIT ]; then  # if we reach our limit, then exit
            exit
        fi
    fi
done
