"""
FROM EXAMPLE PACKAGE:
In Python packages, this file called __main__.py is run when the package is run
directly from command line, as opposed to importing it into another program.
"""

import packagepackage.package as package


def main():
    """
    flip a coin
    """
    coin = package.coin()  # get a line of text
    print(coin)  # print it out


if __name__ == "__main__":
    # run the main function
    main()