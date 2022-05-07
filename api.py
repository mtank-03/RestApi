
from flask import Flask, render_template,request,jsonify
from flask_mysqldb import MySQL,MySQLdb




app = Flask(__name__)
app.secret_key = "caircocoders-ednalan"
         
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'reportmines'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app) 


@app.route('/')
def index(): 
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    curr = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT DISTINCT product_type FROM product_sample")
    product = cur.fetchall() 
    curr.execute("SELECT DISTINCT color FROM product_sample")
    color= curr.fetchall()
    return render_template('index.html', product=product, color=color)
 
@app.route("/fetchrecords",methods=["POST","GET"])
def fetchrecords():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        query = request.form['action']
        minimum_price = request.form['minimum_price']
        maximum_price = request.form['maximum_price']
        #print(query)
        if query == '':
            cur.execute("SELECT * FROM product_sample ORDER BY product_id ASC")
            productlist = cur.fetchall()
            print('all list')
        else:
            cur.execute("SELECT * FROM product_sample WHERE price BETWEEN (%s) AND (%s)", [minimum_price, maximum_price])
            productlist = cur.fetchall()  
    return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})


@app.route("/fetchrecord",methods=["POST","GET"])
def fetchrecord():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        query = request.form['query']
        #print(query)
        if query == '':
            cur.execute("SELECT * FROM product_sample ORDER BY product_id ASC")
            productlist = cur.fetchall()
            print('all list')
        else:
            search_text = request.form['query']
            print(search_text)
            cur.execute("SELECT * FROM product_sample WHERE product_type IN (%s) ORDER BY product_id DESC", [search_text])
            productlist = cur.fetchall()  
    return jsonify({'htmlcategory': render_template('category.html', productlist=productlist)})


@app.route("/fetchcolor",methods=["POST","GET"])
def fetchcolor():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        query = request.form['query']
        #print(query)
        if query == '':
            cur.execute("SELECT * FROM product_sample ORDER BY product_id ASC")
            productlist = cur.fetchall()
            print('all list')
        else:
            search_text = request.form['query']
            print(search_text)
            cur.execute("SELECT * FROM product_sample WHERE color IN (%s) ORDER BY product_id DESC", [search_text])
            productlist = cur.fetchall()  
    return jsonify({'htmlcolor': render_template('color.html', productlist=productlist)})

@app.route("/fetchsort",methods=["POST","GET"])
def fetchsort():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        query = request.form['query']
        #print(query)
        if query == '':
            cur.execute("SELECT * FROM product_sample ORDER BY product_id ASC")
            productlist = cur.fetchall()
            print('all list')
        elif query == 'Price':
            cur.execute("SELECT * FROM product_sample ORDER BY price ASC")
            productlist = cur.fetchall()
            print('all list')    
        else:
            search_text = request.form['query']
            print(search_text)
            cur.execute("SELECT * FROM product_sample ORDER BY product_id ASC")
            productlist = cur.fetchall()  
    return jsonify({'htmlsort': render_template('sort.html', productlist=productlist)})

fetchsort

if __name__ == "__main__":
    app.run(threaded=True)
    