#!/usr/bin/python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen

# Scrap for PHPUnit

def beautifulScrap(printFlag=False):
    webPage = urlopen(
        "https://phpunit.de/manual/current/en/appendixes.assertions.html")

    soup = BeautifulSoup(webPage, "lxml")

    resultat = []

    cpt = 1
    # Remove réference
    tab = [1]

    for section in soup.find_all('div', class_='section'):
        methode = ""
        inverse = ""
        arguments = ""

        if cpt not in tab:

            if printFlag:
                print("Ref :", cpt)

            methode = section.h2.get_text()

            if printFlag:
                print("--------------- Méthode")
                print(methode)

            arguments = section.code.get_text()

            if printFlag:
                print("-------------- Arguments")
                print(arguments)

            for strSec in section.contents:
                if("is the inverse" in strSec.get_text()):

                    inverse = strSec.code.get_text()
                    if printFlag:
                        print("--------------- Méthode inverse")
                        print(inverse)

            resultat.append((methode, inverse, arguments))

        cpt = cpt + 1

        if printFlag:
            print("--------------------------------------------------")

    return resultat


if __name__ == '__main__':
    beautifulScrap(True)
