#!/usr/bin/env python

def make_program(input='submissions.csv', out='index.html', convert=False):

    """
    input is submissions.csv
    """
    import os
    from astropy.table import Table
        
    carousel_output = open(out,'w')
    carousel_header = open('header','r').readlines()
    carousel_output.writelines(carousel_header)
    
    n = 0
    
    sub = Table.read('submissions.csv')
    submissions = {}
    for i in range(len(sub)):
        s = sub[i]
        submissions['%s,%s' %(s['First'],s['Last'])] = s['File']
        
    for i in range(len(sub)):
        
        s = sub[i]
        print(s['First'], s['Last'], s['Title'], s['File'])
        
        ### Carousel
        entry= """
        <div class="item">
          <div class="poster_title"><a href="posters/%s">[PDF]</a> / <a class="boldname">%d) %s %s:</a> "%s"</div>
          <img src="posters_png/2048_%s">
        </div>
        """ %(s['File'], i+1, s['First'], s['Last'], s['Title'], s['File'].replace('.pdf','.png'))
            
        carousel_output.write(entry)
            
    carousel_footer = open('footer', 'r').readlines()
    carousel_output.writelines(carousel_footer)
    carousel_output.close()
                
if __name__ == "__main__":

    make_program()
