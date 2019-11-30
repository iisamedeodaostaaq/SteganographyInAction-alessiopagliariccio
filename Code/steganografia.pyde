i=0                            
p=0                            
lato_pixel=100                  
grandezza_img=lato_pixel*10    

def setup():
    global frase,i,p,lato_pixel
    i=0
    frase=[]
    size(grandezza_img,grandezza_img)     
    frase = input('scrivi  frase')      
    disegna()

def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)

def disegna():
    global i,p,lato_pixel
    loadPixels()  
        while i < (len(frase)):      
        if (i<len(frase)):       
            r=ord(frase[i])
        else:
                        
        if (i+1<len(frase)):     
            g=ord(frase[i+1])
        else:
       
        if (i+2<len(frase)):
            b=ord(frase[i+2])
        else:
       
        for x in range(lato_pixel):            
            for y in range (lato_pixel):       
                pixels[p+y+(grandezza_img*x)] = color(r, g, b) 
        p=p+lato_pixel                                       
        if(p%grandezza_img==0):                
            p=p+(grandezza_img*(lato_pixel-1))    
        print r                                  
        print g
        print b
    updatePixels()                 
    save("out.tiff")             
