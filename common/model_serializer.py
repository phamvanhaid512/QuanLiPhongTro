from datetime import date, datetime
from decimal import Decimal


class ModelSerializer:
    @staticmethod
    def clean_value(value):
        if isinstance(value, Decimal):
            return float(value)

        if isinstance(value, (date, datetime)):
            return value.isoformat()

        if isinstance(value, list):
            return [ModelSerializer.clean_value(item) for item in value]

        if isinstance(value, dict):
            return {
                key: ModelSerializer.clean_value(val)
                for key, val in value.items()
            }

        return value

    @staticmethod
    def serialize_object(obj):
        data = {}

        for field in obj._meta.fields:
            field_name = field.name

            if field.many_to_one or field.one_to_one:
                value = getattr(obj, f"{field_name}_id")
            else:
                value = getattr(obj, field_name)

            data[field_name] = ModelSerializer.clean_value(value)

        return data

    @staticmethod
    def serialize_queryset(queryset):
        return [
            ModelSerializer.serialize_object(obj)
            for obj in queryset
        ]