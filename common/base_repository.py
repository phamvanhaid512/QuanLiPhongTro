class BaseRepository:
    def __init__(self,model):
        self.model = model
    
    def get_all(self):
        return self.model.objects.all()
    
    def get_by_id(self,pk):
        return self.model.objects.get(pk=pk)
    
    def fillter(self,**conditions):
        return self.model.objects.filter(**conditions)
    
    def first(self, **conditions):
        return self.model.objects.filter(**conditions).first()
    
    def exists(self, **conditions):
        return self.model.objects.filter(**conditions).exists()

    def create(self, **data):
        return self.model.objects.create(**data)

    def update(self, pk, **data):
        obj = self.get_by_id(pk)

        for key, value in data.items():
            setattr(obj, key, value)

        obj.save()
        return obj

    def delete(self, pk):
        obj = self.get_by_id(pk)
        obj.delete()
        return True