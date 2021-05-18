#!/bin/bash

filename=${1:-$(mktemp).py}

enter() {
    cat > $filename << EOF
#!/usr/bin/env python3


if __name__ == '__main__':
    def main():
        pass

    main()

EOF
}

test -e $filename || enter

vim $filename +6

# rm $filename -f
