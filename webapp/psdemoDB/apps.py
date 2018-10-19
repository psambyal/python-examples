'''
Created on 08-Jun-2018

@author: Pritika
'''
from flask import Flask,render_template, request , redirect
from time import ctime
from subprocess import check_output
from webapp.psdemoDB.psdemosqllite import select_all_persons


app =Flask(__name__) #instantiated flask obj

@app.route('/persons')
def list_persons():
    list_of_persons = select_all_persons() # return back the dictionary of persons
    return render_template('persons.html',persons=list_of_persons)

@app.route('/editperson/<id>')
def edit_persons():
    list_of_persons = select_all_persons() # return back the dictionary of persons
    return render_template('persons.html',persons=list_of_persons)

@app.route('/addperson')
def add_persons():
    return render_template('personsform.html')

@app.route('/addpersonaction')
def add_person_action():
    print(request.form) # shows form of request in dict format
    f_name =request.form['fname']
    l_name = request.form['lname']
    age = request.form['age']
    
    query ='insert into Person(first_name, last_name, age) values ("{}","{}",{})'
    query = query.format(f_name,l_name,age)
    import sqlite3
    conn =sqlite3.connect('june8.sqlite')
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()
    
    redirect('/persons')

@app.route('/job/<cmd>') #how to pass argument by url
def job_runner(cmd):
    return '<pre>{}</pre>'.format(check_output(cmd, shell =True).decode('ascii'))
    
@app.route('/') # url pattern to invoke this action method
def home():
    return '<h1> a flask demo </h1>' #response printed in response to url hit

@app.route('/ts')
def ts():
    return ctime()

if __name__ == '__main__':
    app.run(debug= True)