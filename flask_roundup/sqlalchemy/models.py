from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class Cafe(db.Model):
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	category = db.Column(db.Enum('tea','coffe',name='cat_enum'),nullable=False, default='coffe')
	name = db.Column(db.String(50),nullable=False)
	price = db.Column(db.Numeric(precision=5,scale=2),nullable=False,default=999.99)

	def __repr__(self):
		return 'Cafe(%d,%s,%s,%5.2f)' %(self.id,self.category,self.name, self.price)


def local_db(db):
	db.drop_all()
	db.create_all()

	db.session.add_all([
			Cafe(name='Espresso',price=10),
			Cafe(name='Cappuccino',price=3.29),
			Cafe(name='Green Tea',category='tea',price=2.99)
		])
	db.session.commit()

	