# mt-keywords2tags

A simple CGI script for converting entry keywords into native tags in MT 3.3+

## Changes

 * 0.01 (2006.06.05):
   * Initial Release.

## Overview

Tagging Plugins including Tags Plugin, Tagwire Plugin and Tags.App employ keywords fields of entries as tag inputs, which are not compatible with MT 3.3+ native tags.

To resolve this issue and happily shift to the newer version of MT, mt-keywords2tags script allows you to convert entry keywords into native tags in MT 3.3+.

## Usage

To install this script, upload or copy "mt-keywords2tags.cgi" into your Movable Type directory and set the permission of the script to 0755 (be executable).

To use it, just acccess it with your Web browser.  You'll see messages as like the following:

    mt-keywords2tags
    
    1: About
    4: Housing, Moving
    12: Research, Trip, Hokkaido
    23: Research, Trip, Paris
    ...
    
    Successfully added tags.

After running this script, I strongly recommend to delete it

## See Also

## License

This code is released under the Artistic License. The terms of the Artistic License are described at [http://www.perl.com/language/misc/Artistic.html](http://www.perl.com/language/misc/Artistic.html).

## Author & Copyright

Copyright 2006, Hirotaka Ogawa (hirotaka.ogawa at gmail.com)
