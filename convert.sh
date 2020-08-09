#!/bin/bash

ebook-convert books/$1.html books/$1.azw3 --level1-toc "//h:h1" --no-inline-toc && cp books/$1.* ../gdrive/My\ Drive/Ebook/