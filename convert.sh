#!/bin/bash

ebook-convert books/$1/$1.html books/$1/$1.$2 --level1-toc "//h:h1" $3 && cp -rf books/$1 ../gdrive/My\ Drive/Ebook/