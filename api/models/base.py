from .__init__ import PeeweeBaseModel
import peewee as p
import datetime

class MyBaseModel(PeeweeBaseModel):
    id =  p.PrimaryKeyField()
    created_at=p.DateTimeField(default=datetime.datetime.now())
    modified_at=p.DateTimeField(default=datetime.datetime.now())
    # created_by = p.IntegerField()
    # updated_at = p.DateTimeField()
    # updated_by = p.IntegerField()
    # deleted_at = p.DateTimeField()
    # deleted_by = p.IntegerField()
    is_active = p.BooleanField(default=True)