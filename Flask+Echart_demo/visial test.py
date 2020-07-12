from flask import Flask,render_template
import json
import pymysql

app = Flask(__name__)

@app.route('/')
def my_tem():
    return render_template('my_template1.html')
@app.route('/test',methods=['POST'])
#链接数据库
def my_test():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 passwd='199922',
                                 db='data',
                                 port=3306,
                                 charset='utf8')

    # 为test2的数据开启一个游标cur
    cur=connection.cursor()

    #访问test2表中的所有数据
    sql = 'SELECT * FROM test2'

    #执行sql中的语句，即获取test2表中的所有数据
    cur.execute(sql)

     #将获取到的sql数据全部显示出来
    see = cur.fetchall()
    # print(sql)
    # print(see)
    # print(cur)

    #定义需要用上的空数据数组，然后通过遍历数据库的数据将数据附上去
    y2017cos = []
    y2018cos = []
    ySaleIn2017 = []
    ySaleIn2018 = []
    jsonData = {}
    xdate = []

    #遍历test2表中的所有数据,see绑定了sql（也就是test2表中的所有数据），所以需要在see中遍历
    for data in see :
        #legname.append(data[0])
        xdate.append(data[0])
        ySaleIn2017.append(data[1])#data[1]是指test2表中第二列(SaleIn2017)的数据
        ySaleIn2018.append(data[2])#data[2]是指test2表中第三列(SaleIn2018)的数据
        y2017cos.append(data[3])#data[3]是指test2表中第四列(y2017cos)的数据
        y2018cos.append(data[4])#data[4]是指test2表中第四列(y2018cos)的数据

    # print(xdate)
    # print(ySaleIn2017)
    # print(ySaleIn2018)
    # print(y2017cos)
    # print(y2018cos)

    #将数据转化格式方便在HTML中调用
    jsonData['ySaleIn2017'] = ySaleIn2017
    jsonData['ySaleIn2018'] = ySaleIn2018
    jsonData['y2017cos'] = y2017cos
    jsonData['y2018cos'] = y2018cos
    jsonData['xdate'] = xdate

    j = json.dumps(jsonData)
    print(j)

    cur.close()
    connection.close()
    return (j)

if __name__ == '__main__':
    app.run(debug=True)