#!/bin/bash

# while : ; do
    # read -n 1 ch
    # if test "x$ch" = "xq" ; then
        # break
    # elif test "x$ch" = 'xw' ; then
        # echo -ne "\033[1A"
    # elif test "x$ch" = 'xs' ; then
        # echo -ne "\033[1B"
    # elif test "x$ch" = 'xa' ; then
        # echo -ne "\033[1D"
    # elif test "x$ch" = 'xd' ; then
        # echo -ne "\033[1C"
    # else
        # echo -ne "$ch"
    # fi
# done

init_bg() {
    printf "\033[1;1H"
    for r in $(seq 1 $ROW) ; do
        for c in $(seq 1 $COL) ; do
            if test $r -eq 1 -o $r -eq $ROW -o $c -eq 1 -o $c -eq $COL ; then
                printf "#"
            else
                printf " "
            fi
        done
        echo
    done
}

move() {
    if ((x + x_inc < 1 || x + x_inc > COL)) ; then
        x_inc=$[x_inc * -1]
    fi

    if ((y + y_inc < 1 || y + y_inc > ROW)) ; then
        y_inc=$[y_inc * -1]
    fi

    let x+=x_inc
    let y+=y_inc
}

ROW=20
COL=60
x=3
y=3
x_inc=1
y_inc=1

stty -icanon -echo
printf "\033[2J\033[?25l"
quitfile=$(mktemp)

while : ; do
    read quit < $quitfile
    test "x$quit" = "xquit" && exit 0
    init_bg
    printf "\033[%d;%dH@" $y $x
    move
    sleep 0.1
done &

while : ; do
    read -s -n 1 key
    test "$key" = "q" && break
done

echo 'quit' > $quitfile
wait
rm $quitfile -f

printf "\033[?25h\033[%d;1H" $[ROW + 2]
stty icanon echo

