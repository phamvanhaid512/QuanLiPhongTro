
class BaseService:
    def __init__(self, repository, pk_field, prefix):
        self.repository = repository
        self.pk_field = pk_field
        self.prefix = prefix

    def generate_code(self):
        index = self.repository.model.objects.count() + 1

        while True:
            code = f"{self.prefix}{index:03d}"

            if not self.repository.exists(**{self.pk_field: code}):
                return code

            index += 1

    def prepare_data(self, data, auto_generate_pk=True):
        result = {}
        fields = {
            field.name: field
            for field in self.repository.model._meta.fields
        }

        for key, value in data.items():
            if key not in fields:
                continue

            field = fields[key]

            if field.many_to_one or field.one_to_one:
                result[f"{key}_id"] = value
            else:
                result[key] = value

        if auto_generate_pk:
            if self.pk_field not in result and f"{self.pk_field}_id" not in result:
                result[self.pk_field] = self.generate_code()

        return result

    def get_all(self):
        return self.repository.get_all()

    def get_detail(self, pk):
        return self.repository.get_by_id(pk)

    def create(self, data):
        prepared_data = self.prepare_data(data, auto_generate_pk=True)
        return self.repository.create(**prepared_data)

    def update(self, pk, data):
        prepared_data = self.prepare_data(data, auto_generate_pk=False)
        return self.repository.update(pk, **prepared_data)

    def delete(self, pk):
        return self.repository.delete(pk)