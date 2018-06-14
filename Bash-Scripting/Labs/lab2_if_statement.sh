#!bin/bash
#
# Lab 2 - Tells me when it is payday (1st and 15th of the month)
#
# Revision History
#  - 2016-02-15 - Kayden Althen <kayden.althen@rackspace.com>
#   * Initial version
#

DAYOFMONTH=`date +%d`  # remember to not have any spaces when setting variables, else it will set to blank

# if [ $DAYOFMONTH -eq 1 ] || [ $DAYOFMONTH -eq 15 ]    # can also write each conditional as separate commands this way
if [ $DAYOFMONTH -eq 1 -o $DAYOFMONTH -eq 15 ]          # checks to see if it is the 1st or the 15th of the month
    then                                                # '-eq' is numeric comparison, '=' is string comparison
        echo 'YAY! Payday!'
        exit 0
    else
        echo 'Boo.. Not yet payday..'   # Don't need to use quotes unless there are symbols that could
        exit 1                          # be confused by the interpreter
fi
