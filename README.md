
# pr-oversight-board-scraper 
 
This work is in support of a PR-based non-profit organization.  
 
## Background 
The Puerto Rico Oversight & Management Board (herein referred to as the Board) posts documents related to their activities on a website. As of Jan. 26, 2018, the website URL is juntasupervision.pr.gov. It is desirable to know when new documents are posted and which category they belong to. Also, mainly due to the Board's website warranties (or lack thereof) (see [1]), it is appropriate to store the documents elsewhere and detect whether the content of an already posted document has changed.  
 
Thus, the objective of this scraper is to: 
1. Backup the documents in case they cannot be accessed or are modified after posting.  
2. Compare posted documents on the Board's website with previously downloaded copies to detect modifications after posting.  
3. Provide automatic tagging of data.  
4. Convert scanned documents into a machine-readable format. 
5. Notify interested parties of new document postings.  
 
 
Why? Some of the issues the non-profit has observed are: 
1. The Board sometimes post-dates "new" documents (they are _new_ but show up at an older date relative to other _newer_ documents making it hard to spot that they exist) 
2. The Board categorizes document based on filenames and NOT CONTENT.  
3. It is inefficient to check the Board's website every day to find out whether a new document has been posted or not. #1 above makes this task even harder.  
 
[1] Board's website disclaimer (retrieves Jan 26, 2018): 
"All information contained in this website is provided "as is" without warranty of any kind and, in particular, no representation or warranty, express or implied, is made or is to be inferred as to the accuracy, reliability, timeliness or completeness of any such information. **This website is to be used for informational purposes only and may not be relied upon for any other purpose.** No representation is made that any statistical or numerical information is without errors or omissions which may be considered material. Under no circumstances shall the Financial Oversight and Management Board for Puerto Rico, its members, directors, officers, agents, employees, or counsel assume any responsibility or liability for the use of the information provided herein." 
 
