#!/bin/bash

ebook-convert books/$1.html books/$1.$2 --level1-toc "//h:h1" $3 && cp books/$1.* ../gdrive/My\ Drive/Ebook/