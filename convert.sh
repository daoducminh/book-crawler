#!/bin/bash

ebook-convert books/$1/$2.html books/$1/$2.$3 --level1-toc "//h:h1" $4 && cp -rf books/$1 ../gdrive/My\ Drive/Ebook/