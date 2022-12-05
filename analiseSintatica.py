#*********************************FUNCOES AUXILIARES*****************************************************
def casoAtribucao(exe, Lexema, Lexema2, OP, linha,tipo):
    i = 0
    cont = 0
    if (len(exe) == 2):
        verificaSimples(exe, Lexema, len(Lexema), linha) 
    elif(len(exe) == 4):
        for x in exe:
            if x != Lexema2[i] and Lexema2[i] == "Tipo_de_Variavel":
                if( verifica_folhas(OP,x)):
                    cont+=1
                    i+=1
                else: 
                    print("Erro: Espera-se"+Lexema2[i]+" "+tipo)
                    break
            elif x == Lexema2[i]:
                cont+=1
                i+=1
            else :
                print("Erro: Espera-se"+Lexema2[i])
                break
            
        lexemaCheck(cont,len(Lexema2),linha)
    else :
        print("error sintatica")

def verifica_folhas(regra,x):
    for iter in regra:
        if x == iter: 
            return True

def verificaSimples(exe, lexema, tamLexema, linha):
    cont = 0
    i = 0
    try:
        for x in exe:
            if x == lexema[i]:
                cont+= 1
                i+=1
            else: 
                print("Erro: Espera-se",lexema[i])
                break
    except:
        cont = None
    lexemaCheck(cont,tamLexema,linha)

def som(x,cont):
    x = None
    cont+=1
    return x, cont

def lexemaCheck(cont,tamanho,linha):
     if cont == tamanho : print("Regra: True") 
     else: print("Erro Regra Sintatica– Linha:", linha)

#*********************************REGRAS*****************************************************

def read(exe, linha):
    readLexema = ["TK_Read","TK_Abre_Parenteses","TK_Identificador","TK_Fecha_Parenteses"]   
    verificaSimples(exe,readLexema, len(readLexema),linha)

def write(exe, linha): 
    
    writeLexema = ["TK_Write","TK_Abre_Parenteses","Conteudo_A_Ser_Printado","TK_Fecha_Parenteses"] 
    
    P = ["TK_Identificador","TK_Entre_Aspas", "TK_Flutuante", "TK_Inteiro"] 
    i = 0
    cont = 0
    if(len(exe)==len(writeLexema)):
        for x in exe:
            if x != writeLexema[i] and writeLexema[i] == "Conteudo_A_Ser_Printado" :
                    if( verifica_folhas(P,x) ):                
                        cont+=1
                        i+=1
                    else:
                        print("Erro: Espera-se",writeLexema[i])
                        break
            elif x == writeLexema[i]:
                cont+=1
                i+=1
            else :
                print("Erro: Espera-se",writeLexema[i])
                break
    lexemaCheck(cont,len(writeLexema),linha)

def fecharChaves(exe, linha):  
    fechaChaveLexema = ["TK_Fecha_Chaves"]   
    verificaSimples(exe,fechaChaveLexema, len(fechaChaveLexema),linha)

def whileIf(exe, linha): 
    whileLexema = ["While_If","TK_Abre_Parenteses","OP","TK_Fecha_Parenteses","TK_Abre_Chaves"]

    OP = ["Operando","LOG","Operando"]
    Operando = ["TK_Inteiro", "TK_Identificador", "TK_Flutuante"]
    LOG = ["TK_Maior_Igual","TK_Verifica_Igual","TK_Verifica_Diferente","TK_Maior","TK_Menor","TK_Menor_Igual"]
    While_If = ["TK_While","TK_If"]

    tamLexema = 7
    i = 0
    j = 0
    cont = 0
    if(len(exe) == tamLexema):
        for x in enumerate(exe): 
            try :
                x = exe[j] 
                #print(x)
                if x == whileLexema[i+1] or x == whileLexema[i]:
                    cont +=1
                    i+=1
                    j+=1
                    x = exe[j] 
                elif x != whileLexema[i]: 
                    if whileLexema[i] == "While_If":
                        if(verifica_folhas(While_If,x)):
                            x , cont = som(x,cont)                  
                            i+= 1
                            j+=1
                            x = exe[j]
                        else : print("Erro: Espera-se While ou If")         
                    if whileLexema[i] == "OP":        
                        for op in OP:
                            if op ==  "Operando": 
                                if (verifica_folhas(Operando,x)):
                                    #x , cont = som(x,cont)
                                    cont += 1
                                    j+=1
                                    x = exe[j] 
                                else: 
                                    print("Erro: Espera-se:", Operando)
                                    OP.clear()
                                    break   
                            elif op ==  "LOG": 
                                if (verifica_folhas(LOG,x)):
                                    #x , cont = som(x,cont)
                                    cont += 1
                                    j+=1
                                    x = exe[j]
                                else: 
                                    print("Erro: Espera-se:", LOG) 
                                    OP.clear()
                                    break 
                    elif x != whileLexema[i] :
                        print ("Erro: Espera-se:", whileLexema[i]) 
                        lexemaCheck(cont,tamLexema, linha)
                        break        
            except: 
                                     
                lexemaCheck(cont,tamLexema, linha)
                break
    else : ("erro construcao sintatica")

def operacaoIdentificador2(exe, linha): 
    identificadorLexema2 = ["TK_Identificador","Operador"]
    
    Operador = ["TK_Incrementa_Um","TK_Decrementa_Um"]
    i = 0
    cont = 0
    if(len(exe)==len(identificadorLexema2)):
        for x in exe:
            if x != identificadorLexema2[i] and identificadorLexema2[i] == "Operador":
                if( verifica_folhas(Operador,x)):
                    cont+=1
                    i+=1
                else:
                    print("Erro: Espera-se",identificadorLexema2[i])
                    break
            elif x == identificadorLexema2[i]:
                cont+=1
                i+=1
            else :
                print("Erro: Espera-se",identificadorLexema2[i])
                break
    lexemaCheck(cont,len(identificadorLexema2),linha)

def operacaoIdentificador3(exe, linha): 
    identificadorLexema3 = ["TK_Identificador","TK_Atribui_Valor","tipo_variavel"]
    
    tipo_variavel = ["TK_Flutuante","TK_Inteiro","TK_Identificador"]
    i = 0
    cont = 0
    if(len(exe)==len(identificadorLexema3)):
        for x in exe:
            if x != identificadorLexema3[i] and  identificadorLexema3[i] == "tipo_variavel":
                if( verifica_folhas(tipo_variavel,x)):
                    cont+=1
                    i+=1
                else:
                    print("Erro: Espera-se",identificadorLexema3[i])
                    break
            elif x == identificadorLexema3[i]:
                cont+=1
                i+=1
            else :
                print("Erro: Espera-se",identificadorLexema3[i])
                break
    lexemaCheck(cont,len(identificadorLexema3),linha)

def operacaoIdentificador5(exe, linha):
    identLexema5 = ["TK_Identificador","TK_Atribui_Valor","OP"]
    
    OP = ["Operando","SIMMAT","Operando"]
    Operando = ["TK_Flutuante", "TK_Inteiro","TK_Identificador"]
    SIMMAT = ["TK_Soma","TK_Subtracao","TK_Multiplicacao","TK_Mod","TK_Divisao"]

    tamLexema = 5
    i = 0
    j = 0
    cont = 0
    if(len(exe) == tamLexema):
        for x in enumerate(exe): 
            try :
                x = exe[j] 
                #print(x)
                if x == identLexema5[i]:
                    cont +=1
                    i+=1
                    j+=1
                    x = exe[j] 
                elif x != identLexema5[i]:          
                    if identLexema5[i] == "OP":        
                        for op in OP:
                            if op ==  "Operando": 
                                if (verifica_folhas(Operando,x)):
                                    #x , cont = som(x,cont)
                                    cont += 1
                                    j+=1
                                    x = exe[j] 
                                else: 
                                    print("Erro: Espera-se:", Operando)
                                    OP.clear()
                                    break   
                            elif op ==  "SIMMAT": 
                                if (verifica_folhas(SIMMAT,x)):
                                    #x , cont = som(x,cont)
                                    cont += 1
                                    j+=1
                                    x = exe[j]
                                else: 
                                    print("Erro: Espera-se:", SIMMAT) 
                                    OP.clear()
                                    break 
                    elif x != identLexema5[i] :
                        print ("Erro: Espera-se:", identLexema5[i]) 
                        lexemaCheck(cont,tamLexema, linha)
                        break        
            except:                    
                lexemaCheck(cont,tamLexema, linha)
                break
    else : ("erro construcao sintatica")            

def atribuiInt(exe, linha):
    intLexema = ["TK_Int","TK_Identificador"]
    intLexema2 = ["TK_Int","TK_Identificador","TK_Atribui_Valor","Tipo_de_Variavel"]
    tipo = "Inteiro"
    OP =  ["TK_Inteiro","TK_Identificador"]

    casoAtribucao(exe, intLexema, intLexema2, OP, linha,tipo)

def atribuiFloat(exe, linha):
    floatLexema = ["TK_Float","TK_Identificador"]
    floatLexema2 = ["TK_Float","TK_Identificador","TK_Atribui_Valor","Tipo_de_Variavel"]
    tipo = "Flutuante"
    OP =  ["TK_Flutuante","TK_Identificador"]

    casoAtribucao(exe, floatLexema, floatLexema2, OP, linha,tipo)

def atribuiString(exe, linha):
    stringLexema = ["TK_String","TK_Identificador"]
    stringLexema2 = ["TK_String","TK_Identificador","TK_Atribui_Valor","Tipo_de_Variavel"]
    tipo = "String"
    OP =  ["TK_Entre_Aspas","TK_Identificador"]

    casoAtribucao(exe, stringLexema, stringLexema2, OP, linha,tipo)