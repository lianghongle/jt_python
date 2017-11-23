import sqlalchemy
from sqlalchemy import create_engine, desc, text
from sqlalchemy.orm import sessionmaker

from mappers.Fund import Fund

# 打印版本，确定是否可用
print(sqlalchemy.__version__)

# 需要驱动库，默认会调用MySQLDb ，我们昨天安装了pymysql
# engine = create_engine('mysql+pymysql://root:123456@localhost/jtthink', connect_args={"encoding":"utf8"})
engine = create_engine('mysql+pymysql://root:123456@localhost/jtthink', encoding="utf8")

# 执行原生 sql
result = engine.execute('select * from myfund')
# res = result.fetchall()
res = result.fetchone()
print(res)

Session = sessionmaker(bind=engine) #创建一个Session对象
session = Session() #实例化

# 1、查询
# result = session.query(Fund).all()
result_sql = session.query(Fund).limit(1)   # 打印 sql
result = session.query(Fund).limit(1).one()
print(result_sql)
print(result)
print(result.__dict__)  # 结果是一个对象,我们可以通过调用对象的__dict__内置属性，来获取类的对象

result = session.query(Fund).filter_by(id=2).limit(5).offset(0).all()
print(result)
#也可以使用 result=session.query(Fund).filter(Fund.news_id==2).first()
#  排序：
# session.query(Fund).order_by(Fund.id).all() #倒排序 session.query(Fund).order_by(desc(Fund.id)).all()

# 自定义过滤条件
print("自定义过滤条件")
result_sql = session.query(Fund).filter(text("id=:id or fname like '%"+":fname"+"%'")).params(id=2,fname=50).order_by(desc(Fund.id))
result = session.query(Fund).filter(text("id=:id or fname like '%"+":fname"+"%'")).params(id=2,fname=50).order_by(desc(Fund.id)).all()
print(result_sql)
print(result)

# 新增
# news=News(news_title='测试新闻')
# session.add(news)
# session.commit()
#
# 修改
# session.query(News).filter(News.news_id==21).update({"news_title":"222"})
# session.commit()




