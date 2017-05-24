#!/usr/bin/python3

import beautifulScrap
import xlsGenerate

#Generate PHPUnit cheatsheet assertions

rslt = []

rslt.append(("PHPunit CheatSheet Assert",))
rslt.append(("",))
rslt.append(("https://phpunit.de/",))
rslt.append(("https://github.com/sebastianbergmann/phpunit",))
rslt.append(("",))
rslt.append(("Support for PHPUnit 5 ends on February 2, 2018.","PHPUnit 5.7 is supported on PHP 5.6, PHP 7.0, and PHP 7.1.","https://phar.phpunit.de/phpunit-5.7.phar"))
rslt.append(("Support for PHPUnit 6 ends on February 8, 2019.","PHPUnit 6.1 is supported on PHP 7.0 and PHP 7.1.","https://phar.phpunit.de/phpunit-6.1.phar"))
rslt.append(("",))

rslt = rslt + beautifulScrap.beautifulScrap()

xlsGenerate.scrapXls(rslt, "PHPUnit", "PHPUnit.xls")
