#coding=utf8

#连接MySQL

# 导入MySQL驱动:
import mysql.connector
# 注意把password设为你的root口令:
conn = mysql.connector.connect(user='root', password='456321', database='test', use_unicode=True)
cursor = conn.cursor()
# 创建user表:
#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
#cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
print cursor.rowcount

# 提交事务:
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
sql = 'select * from user where id = %s'
params = ('1',)
cursor.execute(sql, params)
values = cursor.fetchall()
for value in values:
	for v in value:
		print v,
# 关闭Cursor和Connection:
cursor.close()
conn.close()