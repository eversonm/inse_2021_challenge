from sqlalchemy import func, Boolean, Column, DateTime, INTEGER
from src.lib.database.connector_thread import Base, db_session

class BaseModel(Base):
    __abstract__ = True

    is_deleted = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(), nullable=False, default=func.now())
    updated_at = Column(
        DateTime(),
        nullable=False,
        default=func.now(),
        onupdate=func.now(),
        server_onupdate=func.now(),
    )

    def __iter__(self):
        for x in self.__class__.__table__.columns:
            yield x.name, self.__getattribute__(x.name)

    def __str__(self):
        fields = [f"{k}={v}" for k, v in dict(self).items() if k != "id"]
        str_fields = ", ".join(fields)
        return f"<{self.__class__.__name__} ({str_fields})>"

    def __repr__(self):
        return str(self)

    def save(self, commit=True):
        db_session.add(self)
        if commit:
            db_session.commit()
        return self

    def flush(self):
        db_session.add(self)
        db_session.flush(self)
        return self
    
    def delete(self, commit=True):
        db_session.delete(self)
        if commit:
            db_session.commit()
            
    def update(self, data, commit=True):
        for key, value in data.items():
            setattr(self, key, value)
        if commit:
            db_session.commit()
    
    @classmethod
    def soft_delete_by_id(cls, _id):
        query = cls.query.filter(cls.id == _id).first()
        query.is_deleted = True
        db_session.commit()
        
    def json(self, exclude=()):
        return {k: v for k, v in dict(self).items() if k not in exclude}
