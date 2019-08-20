from app import db

class Stats(db.Model):
    __table__ = db.Model.metadata.tables['consumption_summary']

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return f'Record Id: {self.index} -- Insert Date: {self.insert_date}'