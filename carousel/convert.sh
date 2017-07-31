#!/bin/bash

# mkdir posters_png
cd posters
for pdfile in *.pdf ; do
  convert "${pdfile}" ../posters_png/"${pdfile%.*}".png
done
cd ../posters_png/
prefix="2048_"
for pngfile in *.png ; do
	echo $pngfile
	convert -resize "2048x2048" "${pngfile}" "$prefix$pngfile"
done