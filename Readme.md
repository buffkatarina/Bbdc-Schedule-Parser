# BBDC Schedule Parser
A schedule parser for BBDC. Outputs to an `ics` file.

# Usage
Go the the `Manage Booking` page on your BBDC account. Select the `All` tab. 
  
Open the console on your browser and run:
```
copy(document.body.innerHTML);
```
Paste the output to a text file
  
Clone the repository
```
git clone https://github.com/buffkatarina/Bbdc-Schedule-Parser
```
Install required libraries
```
pip install bs4
```
Run `BbdcScheduleParser.py`. 
```
python BbdcScheduleParser.py [filename] [output]
```
`output` defaults to `BBDCParsed.ics` if left unspecified 











