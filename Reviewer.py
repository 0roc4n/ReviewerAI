# This reviewer AI is created by James Esparrago

# Import neccessary libraries
import PyPDF2
import openai

openai.api_key = "" # Insert your openAI API here

# You can modify this part :)
def response_user(prompt):
  response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="'" + prompt + "' from the text make a simple reviewer higlighting the important parts, dont make comments about the text just make a simple reviewer or summary if possible use bullets. Also in the Top portion make a title about the text", # we are just setting open ai response with the prompt
    max_tokens = 2000,
    stop=None,
    temperature=0.9, # You can modify the AI creative response
  )
  return response["choices"][0]["text"]

# Ask user input for specific file name or path
ufile = input("enter file name and path: ")

# Opening file pdf
filepdf = open(ufile, 'rb')
pdfReader = PyPDF2.PdfReader(filepdf)
x = len(pdfReader.pages)
pageobj = pdfReader.pages[x-1]
text = pageobj.extract_text()

# Passing extracted pdf file to response_user function
newtext = response_user(text)
print(newtext) # printing AI reviewer
# Make new pdf file with the reviewer
newFile = open(r"reviewer.pdf", "w")
newFile.writelines(newtext)
newFile.close()