setup steps

1. Install python on your PC (ossapi doesn't work on some IDE)
2. Have python IDE (unless you eant to edit this code on notepad)
3. run pip install ossapi on cmd
4. Set up API key https://tybug.github.io/ossapi/creating-a-client.html
5. Edit the code by replacing `[redacted]` with your API key `api = Ossapi(client_id, client_secret)`

How to use
1. Run search.py by running `python search.py` on cmd (open cmd on the folder containing the code and the text)
2. Run hyperlink_maker.py by running `python hyperlink_maker.py`
3. The result should be on the `hyperlinks.txt` now you can import it to google sheet
4. On Google sheet File --> Import --> drag and drop `hyperlinks.txt`
5. Separator type : custom --> make semicolon (;) a common separator
6. Import data
