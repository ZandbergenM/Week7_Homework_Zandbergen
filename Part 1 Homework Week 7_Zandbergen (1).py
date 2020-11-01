#!/usr/bin/env python
# coding: utf-8

# In[1]:


#14.1
#Write a function called sed that takes as arguments a pattern string, a replacement
#string, and two filenames; it should read the first file and write the contents into the second file
#(creating it if necessary). If the pattern string appears anywhere in the file, it should be replaced
#with the replacement string.


# In[44]:


def main():
    string = 'No' #identify the string to be replaced
    replace = 'Every'#replaces that string
    file1 = '12.1.txt' #text file from previous week
    file2 = file1 + '.replaced' #new text file to be created that replaces a string from file1
   


# In[45]:


def sed(string, replace, file1, file2): #See above
    fin = open(file1, 'r') #mode 'r' for reading
    fout = open(file2, 'w') #write as mode 'w' as the second parameter to write a file
    for line in fin:
        line = line.replace(string, replace) #for each line in file1, "No" is replaced by "Every" (this changes the first line)
        fout.write(line) #for each line in fin writes a line in fout with the replaced string 
    fin.close() #close fin after four loop completes
    fout.close() #close fout after four loop compltes
    
    


# In[46]:


if __name__ == '__main__':
    main()


# In[ ]:




