'''
Created on 08-Jun-2018

@author: Pritika
'''
import requests
import multiprocessing
import smtplib
from email.mime.text import MIMEText

def send_alert_mail(from_address, to_address, subject, message):
    '''sending mail alert for failed requests'''
    
    mesg = MIMEText(message)
    mesg['From'] = from_address
    mesg['To'] =to_address
    mesg['Subject'] = subject
    
    smtp_server_address ='domain.server.net'
    smtp = smtplib.SMTP(smtp_server_address)
    smtp.sendmail(from_address, to_address, mesg.as_string())
    smtp.close()
    

def web_scrapper(q):
    '''web scrapping'''
    try:
        p_name = multiprocessing.current_process().name
        print("p_name waiting==>",p_name)
        url = q.get() # to get an url from queue object
        payload = requests.get(url).content [:128]   
        print("{} {} {}".format(p_name,url,payload))
    except requests.exceptions.ConnectionError as ex:
        subject ="{} :{}".format(p_name,url)
        message =str(ex)
        send_alert_mail('ps@localhost','abc.test@gmail.com',subject,message)
    

def main():
    '''main process'''
    urls =[
        'https://google.com','http://linux.org','http://kernel.org',
        'http://python.org','http://perlang.org'
        ]

    q = multiprocessing.Queue()
    
    for url in urls:
        p = multiprocessing.Process(target=web_scrapper, args=(q,))
        p.start()
    
    for url in urls:
        q.put(url) # add item into queue
        
    for child in multiprocessing.active_children():
        child.join()
        
if __name__ == '__main__':
    main()
    

