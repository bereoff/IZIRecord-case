from uuid import uuid4

from django.db.models import DateTimeField, Model, UUIDField


class ModelUUIDBased(Model):
    id = UUIDField(primary_key=True, editable=False, default=uuid4)
    created_at = DateTimeField(
        auto_created=True, editable=False, auto_now_add=True, db_index=True)
    updated_at = DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True

    @classmethod
    def to_json(cls):

        dictionary = {}
        for field in cls._meta.concrete_fields:

            dictionary[field.name] = cls.__getattribute__(field.name) if type(cls.__getattribute__(field.name)) in [int, float, dict, bool] \
                else str(cls.__getattribute__(field.name)) if cls.__getattribute__(field.name) else None  # NOQA

        return dictionary

    @staticmethod
    def remove_keys(obj: dict, keys: list) -> dict:
        [obj.pop(k, None) for k in keys]
        return obj

    @staticmethod
    def rename_keys(obj: dict, keys: dict) -> dict:
        [obj.update({v: obj.pop(k, None)}) for k, v in keys.items()]
        return obj

    @property
    def created_at_month(cls):
        return int(cls.created_at.strftime("%m"))

    @property
    def created_at_day(cls):
        return int(cls.created_at.strftime("%d"))

    @property
    def created_at_year(cls):
        return int(cls.created_at.strftime("%d"))

    AUTO_FIELDS = ['created_at', 'updated_at']
