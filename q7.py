#Part 7 with Bonus Question included

inputFile = raw_input("Enter the source file name: ")

try:
	f = open(inputFile)
except IOError:
	print ('No File Exist')

notes = []
notes_href = {}
postDivStartTxt = "div class=\"post "
searchText = "data-notes=\""
searchTextLength = len(searchText)

hrefs = []
postDiv = False
href = None
for line in f:
	if line.find(postDivStartTxt) >= 0:
		href_start = line.find("href=\"")+6
		href = line[href_start:line.find("\"", href_start)]
		hrefs.append(href)

	if line.find(searchText) >= 0:
		notesStart = line.find(searchText) + searchTextLength
		note = line[notesStart:line.find("\"", notesStart)]
		notes.append(int(note))
		if href:
			notes_href[href] = int(note)
			href = None

print "Number of notes", len(notes)
notes.sort(reverse=True)
print "Top 5 notes", notes[:5]
print "Extra Credit HTML"
idx = 0
top_hrefs = []
for href in sorted(notes_href, key=lambda x: notes_href[x], reverse=True)[:5]:
	idx = idx + 1
	top_hrefs.append("#%d: <a href=\"%s\">%d</a>" % (idx, href,  notes_href[href])) 

print "<html><body>\n%s</body/<html>" % "<br><br>\n".join(top_hrefs)
	

