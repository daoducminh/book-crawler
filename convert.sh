#!/bin/bash

ebook-convert $1.html $1.azw3 --level1-toc "//h:h1" --no-inline-toc && cp $1.azw3 gdrive/My\ Drive/Ebook/