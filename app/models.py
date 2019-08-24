from app import db

class Planets(db.Model):
    __table__ = db.Model.metadata.tables['planets']

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return f'Star Name: {self.pl_hostname} -- Planet Name: {self.pl_name}'