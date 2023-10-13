from uuid import uuid4

from django.db.models import DateTimeField, Model, UUIDField


class ModelUUIDBased(Model):
    id = UUIDField(primary_key=True, editable=False, default=uuid4)
    created_at = DateTimeField(
        auto_created=True, editable=False, auto_now_add=True, db_index=True)
    updated_at = DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True
