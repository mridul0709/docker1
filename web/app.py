from flask import Flask
import psycopg2
import os
app = Flask(__name__)
@app.route('/')
def hello():
    os.system('curl consul:8500/v1/catalog/service/db\?pretty > consul')
    os.system("cat consul | grep ServiceAddress |awk -F '\"' '{print $4}' > db_ip")
    os.system("cat consul |grep ServicePort |awk -F ': ' '{print $2}' |awk -F ',' '{print $1}' > db_port")
    db_ip=os.popen('cat db_ip').read()
    db_port=os.popen('cat db_port').read()
    conn=psycopg2.connect(dbname="docker", user="docker", host=db_ip, port=db_port)
    cur=conn.cursor()
    cur.execute("select * from docker")
    one = cur.fetchone()
    return format(str(one[0]))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
