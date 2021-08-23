from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine("postgresql+psycopg2://postgres:1111@127.0.0.1:5432/mydb")

Base = declarative_base()

class Product(Base):
    __tablename__ = 'mydb'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    amount = Column(Integer)
    comment = Column(String)

    def __init__(self, name, price, amount, comment):
        self.name = name
        self.price  = price
        self.amount = amount
        self.comment = comment

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
product1 = Product('Cucumber', 4, 10, "Green")
product2 = Product('Cucumber', 3, 12, "Littel")
product3 = Product('Apple', 5, 14, "Green and red")


# session.add(product1)
# session.add(product2)
# session.add(product3)
def create_product():
    name = input("Введите имя продукта: ")
    price = input("Введите цену продукта:")
    amount = input("Введите кол-во продукта: ")
    comment = input("Добавьте комментарий")
    create_product = Product(name, price, amount, comment)
    session.add(create_product)
    session.commit

def updata_data():
    id = input("Введите id продукта котрый необходимо изменить: ")
    try:
        id = int(id)
    except ValueError as err:
        print(err)
    else:
        id = int(id)


    i = session.query(Product).get(id)
    i.name = input(f"Введите имя, старое имя - {i.name} ")
    i.price = int(input(f"Введите цену, старая цена - {i.price} "))
    i.amount = int(input(f"Введите кол-во, строе значение {i.amount}"))
    i.comment = input(f"Введите комментарий, старый комментарий {i.comment}")
    session.add(i)
    session.commit()

def delete_obj():
    id = input("Введите id продукта который необходимо удалить: ")

    i = session.query(Product).get(id)

    session.delete(i)
    session.commit()
def read_of_id():
    id = input("Введите id продукта для чтения: ")

    i = session.query(Product).get(id)
    try:
        i.name
    except AttributeError as err:
        print('нет такой записи')
    else:
        print(i.name, i.price, i.amount, i.comment)

#read_of_id(2)
#create_product()

#delete_obj()
#update_date()

def view():
    func = input("Выберите действие 1- создать , 2 - прочитать, 3 - обновить, 4 - удалить")
    dic_func = {"1":create_product, "2": read_of_id, "3": updata_data, "4": delete_obj}
    return dic_func[func]()


view()
person = session.query(Product.id, Product.name,Product.price, Product.amount, Product.comment).all()

for i in person:
    print(i)

session.commit()