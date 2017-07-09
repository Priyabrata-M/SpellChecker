# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 22:59:04 2017

@author: madhavi
"""

import web
import wsc
import ssc
   
urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

html_data="<html> <head> <link rel='stylesheet' type='text/css' href='./static/mystyle.css'> </head> <body>   <div align='center' class='div3'>  <div class='div1'>Spell Checker Project</div>  <div> <form action='http://127.0.0.1:8080' method='get' name='form1'> <table cellspacing='2' cellpadding='3'> <tr> <td>Enter an incorrect word/sentence:</td></tr> <tr> <td><input type='text' name='typo'></td> <td> <input type='submit' class='button' value='Correct It'> </td> </tr> </table> </form> </div>  <div class='div4' align='left'>Correct Suggestions:</div><div class='div5'> "
sentences="Shivani is a good girl <br> Shivani is a good girl"
html2="</div></div> <footer align='center' style='font-size:15px;font-style: italic;'>   <p><u>Project Submitted by:</u><br> Shivani Singh <br> Madhavi Srivastava</p> </footer>   </body>  <html>"

class hello:        
    def GET(self,name):
#        if not name: 
#            name = 'World'
#        return 'Hello, ' + name + '!'
        form = web.input()
        typo=web.websafe(form.typo)

        if len(typo.split(" "))==1: 
            correct_word=wsc.correct_words(typo)
            sentence="Incorrect Word: "+ typo +"<br><br>"
            i=0
            for item in correct_word:
                i=i+1
    #            sentence=sentence+ "Suggestion "+str(i)+": "+item[0]+"  Probability: "+str(item[1])+"<br>"
                sentence=sentence+ "Suggestion "+str(i)+": "+item[0]+"<br>"
        else:
            correct_sentences=ssc.sentenceCorrection(typo)
            sentence="Incorrect Sentence:<br>"+ typo +"<br><br>"
            i=0
            for item in correct_sentences:
                i=i+1
    #            sentence=sentence+ "Suggestion "+str(i)+": "+item[0]+"  Probability: "+str(item[1])+"<br>"
                sentence=sentence+ "Suggestion "+str(i)+": "+item[0]+"<br>"
            
        
        return html_data+sentence+html2
        


if __name__ == "__main__":
    app.run()