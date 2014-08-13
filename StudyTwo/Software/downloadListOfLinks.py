#akthom - 12 april 2014
# generic script to download a list of links

def dlLinks(linkList): 
        import re #import regex module
        import urllib #request #import url request module
        counter=0
        linklinks=open(linkList,"r") #opens list of links
        for line in linklinks:

                        infile=urllib.urlopen(str(line))
                        fileName=str(counter)+".html"
                        webpageSaved=open(fileName,'wb')
                        pageText=infile.read()
                        webpageSaved.write(pageText)

                        counter=counter+1

                        webpageSaved.close()
 
                        
        linklinks.close()

        print("done")
