phylomemetics
=============

scripts for scraping gcmd and making trees.

full work described in: 
Thomer, A. & Weber, N. (accepted).  The Phylogeny of a Dataset.  Paper to be presented at Annual Meetin of the American Society for Information Science and Technology, 2014.  Seattle, WA.

- most of these scripts are disappointingly a) simple, b) not related to phylogenetics, and c) and saddest of all, probably not necessary had I spent the time to figure out the GCMD API, or at the very least, thought to download the files in ISO 19115.  As it is I had to do a ton of text fussing and formatting after the fact.  Workflow as best I remember it (with screwy workarounds to get Beautiful Soup to work:

     1. search for files and download lists of records from GCMD
     2. clean up text (e.g. just delete the little bits of free text description
     3. extract URLS using method of choice (Text wrangler or this webbased program that no longer seems to work - http://pgl.yoyo.org/urlex/ ) -  save to txt file.  
     4. Run DownLoadListofLinks.py using saved text file from step 3.
     5. Move downloaded files into folder, make back up copy, change relevant lines of code pointing to file in crawlLinks.py
     6. Open all downloaded files in Text Wrangler, and begin text clean up. Because all of the files use html comments to mark fields, and because Beautiful Soup doesn't seem to recognize comments in any useful way, we're going to make some ad hoc xml for BeautifulSoup to work with later
          * replace all `<\!-- ` with `\</metadata><metadata tag="`   <-- this closes the prior section while opening up the new section
          * replace all `-->` with `\>`
          * grep to find and delete repeated filler like =, spaces, etc
          * finally, find and delete all line breaks (this just makes for cleaner output later).
     7. You are finally ready to crawl the text.  Run files through crawlLinks.py
     8. Bask in the glow of your data! Then despair how much more clean up it needs: in excel or open refine, do things like clear out the extra junk python wrote (brackets, mostly), and move text to columns.
     
     A better programmer than I likely could've done this much more simply -- I hope to make this process more better in teh future.  
     
     Next hellish step: converting the GCMD text data into 1s and 0s for PAUP to read.  Again, this is something that could potentially be scripted, but for now I do think it was better to do largely by hand -- character coding is tricky and requires human eyes.  Plus, it'll help you know your data a bit better.
     
     Short explanation of character conversion workflow: use pivot tables.  Longer forthcoming
