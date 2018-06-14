#!bin/bash
#
# Lab 3 - Looping, announce every minute as it strikes
#
# Revision History
#  - 2016-02-15 - Kayden Althen <kayden.althen@rackspace.com>
#   * Initial version
#

LIMIT=$1
date '+It is currently %r'

while true
do
    SECONDS=`date +%S`
    DELAY=`expr 60 - $SECONDS`  # or DELAY=$((60-$SECONDS))

    sleep $DELAY
    date '+It is %r!'           # or date '+It is %l:%M %p!' if you don't want the seconds
done
