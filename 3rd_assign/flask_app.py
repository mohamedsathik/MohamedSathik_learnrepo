from flask import Flask , jsonify

from data.json_pg import read,show_the_write

app=Flask(__name__)

@app.route('/api/printHello')
def hello():
    data={'names':'Hello World!'}
    return jsonify(data)

@app.route('/api/orgiRecepie')
def orgrec(): 
    data=read()
    return jsonify(data)    

@app.route('/api/modifyRecepie')
def modrec():
    data=show_the_write()
    return jsonify(data)



if __name__ == '__main__':  
    app.run(debug = True)