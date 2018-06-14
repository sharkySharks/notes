printdate() {
    if [ $PRINTDATE = 'yes' ]; then
        date '+It is %l:%M %p, %B %d, %Y!'
    else
        date '+It is %r!'
    fi
}

limitcheck() {
    if [ $LIMIT -ne 0 ]; then          # if the default is given, 0, then no need to check the limit
        COUNTER=$(($COUNTER + 1))
        if [ $COUNTER -eq $LIMIT ]; then  # if we reach our limit, then exit
            exit
        fi
    fi
}
