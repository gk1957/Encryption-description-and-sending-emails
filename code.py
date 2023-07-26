import smtplib
import time
import ssl

def mail(encrypted):
    server= smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("my-mail@gmail.com", "password")
    
    server.sendmail("my-mail@gmail.com", "friend-mail@gmail.com", encrypted)
    server.quit()
    
def dec(encrypted, value, series):
    decrypted=""
    for letter in encrypted:
        position2=series.find(letter)
        newp2= (position2-value)%52
        if letter==" ":
            decrypted+=" "
        else:
            decrypted+=series[newp2]
    print(decrypted)
    
def enc():
    message="I knew it was friendship at first sight when I knew we were the same kind a crazy about Python!!!"
    value=3
    encrypted=""
    series="abcdefghijklmnopqrstuvwxyz0123456789@#$%&"
    series+=series.upper()
    series+=" "
    
    for letter in message:
        position=series.find(letter)
        newp= (position+value)%52
        if letter==" ":
            encrypted+=" "
        else:
            encrypted+=series[newp]
    print(encrypted)
    mail(encrypted)  
    time.sleep(2)
    dec(encrypted, value, series)      
    
enc()    
    