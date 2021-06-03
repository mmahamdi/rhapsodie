def macro2ortho(macrosent):
    
    # | -> ,
    # ^ -> rien
    # () -> , , 
    #[] et {} -> rien
    #< > -> rien
    # // -> .
    #" " -> , , 
    # = -> , 
    # #  -> .
    #ESPERLUETTE -> rien
    #ESPERLUETTE // -> …
    # $ et variations -> rien
    
    

    
    
    
    
    
    
    
    
    
    
    
    import re
    error = ''


    #print (macrosent)

    sent = (macrosent+"\n").replace("ESPERLUETTE //","…").replace('//\n','.').replace('#',' ').replace('&','…')
    

    #Speaker-related content
    sent = re.sub(r'\( *\$L\d .* *\) (\(.*\)) \( *\$L\d .* *\)',r'\1',sent)
    sent = re.sub(r'\( *\$L\d .* *\)(.*)\( *\$L\d .* // \)',r'\1',sent)
    sent = re.sub(r'\( *\$L\d .* // \)(.*)\( *\$L\d .* // \)',r'\1',sent)
    sent = re.sub(r'\( *\$L\d .* *\)','',sent)
    sent = re.sub(r'-?\$-?','',sent)
    sent = re.sub(r'L\d','',sent)
    
    
    
    #content btw brackets [] and {}

    sent = re.sub(r'\[(.+?)\]',r' \1 ', sent)
    sent = re.sub(r'\[(.+?)\]',r' \1 ', sent)
    if re.search(r'[\[\]]', sent):
        error += 'square brackets not matching. '
        sent = sent.replace('[',', ').replace(']',', ')
    sent = re.sub(r'\{(.+?)\}',r' \1 ', sent)
    sent = re.sub(r'\{(.+?)\}',r' \1 ', sent)
    sent = re.sub(r'\{(.+?)\}',r' \1 ', sent)
    if re.search(r'[\{\}]', sent):
        error += 'curly brackets not matching. '
        sent = sent.replace('{',' ').replace('}',' ')
    
    

    if re.search(r'[()]', sent) and not re.search(r'\(.+?\)', sent) :
        error += 'parenthesis not matching. '
        sent = sent.replace('(',' ').replace(')',' ')
        
    
    #---------------------------------------------------------------
    #IU and IC and | and ^

    sent = re.sub(r'//[+=]?',', ', sent)
    #sent = re.sub(r'[<>]\+?',', ', sent) orig
    sent = re.sub(r'<\+?',', ', sent) # modif march 2020
    sent = re.sub(r'>\+?',' ', sent) # modif march 2020
    sent = re.sub(r' \| ',', ', sent) # single |
    sent = re.sub(r'\|\|',', ', sent) # double ||
    sent = re.sub(r'\|[cra]?\b',', ', sent) # | with or without pile marker c r a
    sent = re.sub(r'\^','', sent)
    #------------------------------------------------------------------
   
 
    #--------------------------------------
    #inaudible content
    sent = re.sub(r'XXX','', sent)
    #-------------------------------------
    #esperluette
    sent = re.sub(r'ESPERLUETTE','', sent)
  # question marks and exclamation marks


    sent = sent.replace('!.','!').replace('?.','?')
    
  # discourse markers and insertions

    sent = re.sub(r'" *(.+?) *"',r', \1, ', sent) #no quotes for discourse markers
    sent = re.sub(r'\( *(.+?) *\)',r', \1, ', sent) #no parentheses for insertions
    #print(sent)
  # ---------------------------------------------------------------------------------
#weird punctuation combos
    sent = re.sub(r' \W$','.', sent)
    sent = re.sub(r'^ *\W','', sent)
    sent = re.sub(r'^ *,','', sent)
    sent = re.sub(r'^ *','', sent)
    sent = re.sub(r'[ ,]*\,[ ,]*',', ', sent)
    sent = re.sub(r'(\w) \, ','\1, ', sent)
    sent = re.sub(r'[ .]*…[ .]*','…', sent)
    sent = re.sub(r' +\.','.', sent)
    sent = re.sub(r' +\!','!', sent)
    sent = re.sub(r' +\?','?', sent)
    sent = re.sub(r',+\.','.', sent)
    sent = re.sub(r'\?\.','?', sent)
    sent = re.sub(r'\!\.','!', sent)
    sent = re.sub(r'\,\?','?', sent)
    sent = re.sub(r'\?\,',',', sent)
    sent = re.sub(r'\?\,',',', sent)
    sent = re.sub(r'\!\,',',', sent)
    sent = re.sub(r'\,\!','!', sent)
    sent = re.sub(r'  +',' ', sent)
    sent = re.sub(r' *\.','.', sent)
    sent = re.sub(r', \+',',', sent)
    sent = re.sub(r'…\+','…', sent)
    sent = re.sub(r'. \|$',',', sent)
    sent = sent.strip()
    
    #------------------------------------------------------------------------------------------
    #Capitalize the first letter
    #try:
        #sent=sent[0].upper()+sent[1::]
    #except:
        #error += 'empty. '
    #.replace('<',', ').replace('>',', ').replace('|c',', ').strip()
    
    #print(sent)
    #---------------------------------------------------------------------------------

    if '……' in sent:
        error += 'strange ellipsis'
        sent = sent.replace('……','…')
    if '|,' in sent:
        error += 'strange punctuation'
        sent = sent.replace('|,',',')
    if '".' in sent:
        error += 'strange punctuation'
        sent = sent.replace('".','.')
    if '??' in sent:
        error += 'strange punctuation'
        sent = sent.replace('??','?')
    if ' .' in sent:
        error += 'strange punctuation'
        sent = sent.replace(' .','.')


    #print (sent)
    #print("-----------------------")
    #print(sent)
    #print("-------------------------")
    #########testing
    tmacro = re.sub(r'\( *\$L\d .* *\) (\(.*\)) \( *\$L\d .* *\)',r'\1',macrosent)
    tmacro = re.sub(r'\( *\$L\d .* *\)(.*)\( *\$L\d .* // \)',r'\1',tmacro)
    tmacro = re.sub(r'\( *\$L\d .* // \)(.*)\( *\$L\d .* // \)',r'\1',tmacro)
    tmacro = re.sub(r'\( *\$L\d .* *\)','',tmacro)
    tmacro = re.sub(r'\W','',tmacro).replace('XXX','').replace("ESPERLUETTE",'').lower()
    tmacro = re.sub(r'l\d','',tmacro)
    
    tsent = re.sub(r'\( *\$L\d .* *\) (\(.*\)) \( *\$L\d .* *\)',r'\1',sent)
    tsent = re.sub(r'\( *\$L\d .* *\)(.*)\( *\$L\d .* // \)',r'\1',tsent)
    tsent = re.sub(r'\( *\$L\d .* // \)(.*)\( *\$L\d .* // \)',r'\1',tsent)
    tsent = re.sub(r'\( *\$L\d .* \)','',tsent)
    tsent = re.sub(r'\W','',sent).lower().replace('-,','').replace('~,','')
    tsent = re.sub(r'l\d','',tsent)
    
    if tmacro != tsent:
        print('test failed. letters have changed!')
        print(re.sub(r'\W','',macrosent))
        print(re.sub(r'\W','',sent))
        print(macrosent)
        print(sent)
        

    tsent = sent.replace(",","x").replace(' ','x').replace('-','x').replace('…','x').replace('”','x').replace('“','x').replace('"','x').replace("'",'x').replace(')','x').replace('[','x').replace(']','x').replace('a.m.','x').replace('p.m.','x').replace('~,','').replace('~?','').replace('~.','').replace('ó̠tò̠̠','').replace(" ","x")

    if re.search('\W\W',tsent):
        print('test failed. strange double punctuations remained!')
        print("macrosent:",macrosent)
        print("sent:",sent)
        print(tsent)
        
    return sent  # ,error


#ex = '( $L2 { mh | mh } ) -$ ^mais je pense surtout que "euh" [ dans le sixième arrondissement <+ les maternelles "euh" < il y a suffisamment d\'enseignants ] //+ $- { ^mais que | ^mais que } ( $L3 "oui" il faudrait qu\'ils puissent parler plus // ) -$'
#print(macro2ortho(ex))