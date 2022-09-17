from re import L
import requests
from bs4 import BeautifulSoup
import markdownify
import os


def tomarkdown(html,filename):
   h = markdownify.markdownify(html, heading_style="ATX")
   dirName=filename
   if not os.path.exists(dirName):
      os.mkdir(dirName)
      print("Directory " , dirName ,  " Created ")
   else:    
      print("Directory " , dirName ,  " already exists")
   
   if filename=="./":
       filename="Introduction..md"
   try:
     filename=filename.replace("html","md")
   except:
      filename=filename+".md"
   
   with open(f"./{dirName}/{filename}",'w') as f:
        f.write(h)

  

def directory(dir):
  dirName=f"{dir}"
  if not os.path.exists(dirName):
      os.mkdir(dirName)
      print("Directory " , dirName ,  " Created ")
  else:    
      print("Directory " , dirName ,  " already exists")

URL = "https://ttzztt.gitbooks.io/lc/content/"
r = requests.get(URL)
  
soup = BeautifulSoup(r.text,'html.parser') # If this line causes an error, run 'pip install html5lib' or install html5lib
html=soup.prettify()
#tomarkdown(html)
# Empty list to store the output
urls = []
dic={}
dire="files"
#print(html)
c=0
prevd=""
nextd=""
# For loop that iterates over all the <li> tags
for ultag in soup.findAll('ul', {'class': 'summary'}):
    #print(len(ultag.find_all('li')))
    # looking for anchor tag inside the <li>tag
    for litag in ultag.find_all('li',{'class': 'chapter'}):
         #print(litag.text.strip())
        
            #dir=litag.find('a').text.strip()
            #directory(dir)
            
            
            level=litag["data-level"]
            
            try:
              
              path=litag["data-path"]
              f=litag.find('a').text.strip()
              
            except:
              #path=litag["data-level"]
              path=""
              f=litag.find('span').text.strip()
              
              

            if (f=="Introduction"):
              pass
            else:
              
              pass
            '''try:
              
              #print(litag.find('a').text.strip())
              f=litag.find('a').text.strip()
            except:
               #print(litag.find('span').text.strip())
               pass'''
            
            print(f)
            #directory(f)
            print(path)
            urls.append(f)


            
            
            '''if c<level.count("."):
              dire=litag["data-path"].replace("html","")
              directory(dire)
            elif c==level.count("."):
              dire=litag["data-path"].replace("html","")
              directory(dire)'''

            #if c !=level.count(".")
              
              #urls.append(litag["data-path"])
            #dic[]
            '''print(c)
            if c<level.count("."):
                try: 
                  if litag["data-path"]=="./":
                       pass
                  else:
                    x = litag["data-path"].rfind("/")
                    if x !=-1:
                      filename=litag["data-path"][x+1:]
                      dire+="/"+filename.replace(".html","")
                    else:
                      dire+="/"+litag["data-path"].replace(".html","")
                    #print(dire)
                    #directory(dire)
                except KeyError:
                   dir=litag.find('span').text
                   #directory(dire)
                #print(dire)
                c+=1

            elif c==level.count("."):
                #print(dire)
                
                pass
            elif level.count(".")==1:
                #dire+="/"+litag["data-path"].replace("html","")
                try:
                 dire="files/"+litag["data-path"].replace(".html","")
                except:
                  dir="files/"+litag.find('span').text
                #print(dire)
                #directory(dire)
                c=1
            
            directory(dire)'''
         
        
         #for i in  litag.find('ul',{'class': 'articles'}).find_all('li'):
          #    urls.append(litag["data-path"])
         
         # print (litag.text.strip())

    '''for ulsubtag in ultag.find_all('ul'):
          for lisubtag in ulsubtag.find_all('li'):
             print (lisubtag.text)'''
'''try:
          
        # looking for href inside anchor tag
        if 'href' in a.attrs:
              
            # storing the value of href in a separate 
            # variable
            url = a.get('href')
              
            # appending the url to the output list
            urls.append(url)'''
      
    # if the list does not has a anchor tag or an anchor 
    # tag does not has a hr

'''urls=[]
for div in soup.findAll('div', {'class': 'book-body'}):
    print(div)
    for a in div.findAll('a', {'class': 'navigation navigation-next navigation-unique'}):
        print(a)
        try:
            
            # looking for href inside anchor tag
            if 'href' in a.attrs:
                
                # storing the value of href in a separate variable
                url = a.get('href')
                
                # appending the url to the output list
                urls.append(url)
                
        # if the list does not has a anchor tag or an anchor tag
        # does not has a href params we pass
        except:
            pass

print(urls)'''


'''for url in urls:
    BASE=URL+url
    print(url)
    r = requests.get(BASE)
    try:
      soup = BeautifulSoup(r.text,'html.parser')
    
      html=soup.find('div', {'class': 'page-inner'}).prettify()
    except AttributeError:
        continue
    tomarkdown(html,str(url))'''
  

#print(urls)
prev=""
next=""
for url in urls:
  print(url)