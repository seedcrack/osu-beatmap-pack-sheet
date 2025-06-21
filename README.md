setup guide

1. download all files in this repo
2. Install python on your PC (ossapi doesn't work on some IDE)
3. run `pip install ossapi` on cmd
4. Set up API key https://tybug.github.io/ossapi/creating-a-client.html
5. you now should have client ID and client secret which you need to input when running this code

How to use
1. Run search.py by running `python search.py` on cmd (open cmd on the folder containing the code and the text files)
2. Run hyperlink_maker.py by running `python hyperlink_maker.py`
3. The result should be on the `hyperlinks.txt` now you can import it to google sheet
4. On Google sheet File --> Import --> drag and drop `hyperlinks.txt`
5. Separator type : custom --> make semicolon `;` a common separator
6. Import data
7. Ctrl + F --> kebab menu to open Find and Replace
8. tick `Also search within formulas` delete all the leading apostrophes
