How to set up the poster carousel:

1. Clear the `posters` directory. Clear the `posters_png` directory.

2. Download all PDF poster files in the `posters` directory. Optionally, rename them with the last name of the first author (easier to keep them straight). 

3. Make the convert.sh script executable: `chmod u+x convert.sh`. Run the script (./convert.sh). Check the `posters_png` directory - now you should have 2 png files for each PDF. This is not a smart script - only run it once.

4. Create the submissions list `submissions.csv` in a text editor or in Excel. Keep the columns the same and do not put extra commas anywhere.

5. Open the `header` file and change the conference title and the link to the conference page.

6. Run the `posters.py` script: `python posters.py`. This requires Python 3.5. The output is written to `index.html`. You can now open this file in your browser and test the page. 

7. Rsync the contents of the carousel directory to the location where you want to host the your site: `rsync -avz carousel/ user@host.astro.edu:/conference_site/posters/`

8. Ta-da!

(The carousel code itself provided by [OwlCarousel2](https://owlcarousel2.github.io/OwlCarousel2/))
 
