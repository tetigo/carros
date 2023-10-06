from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory
from openai_api.client import get_car_ai_bio


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    print('### PRE SAVE ###')
    print(sender)
    print(instance)
    print(">>>bio",instance.bio, (instance.bio == None), (instance.bio is None), (instance.bio == ''), (instance.bio is ''), (instance.bio == ' '), (instance.bio is ' '))
    if not instance.bio:
        instance.bio = get_car_ai_bio(model=instance.model, brand=instance.brand, year=instance.factory_year) or 'Descrição não disponível'


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    print('### POST SAVE ###')
    print(sender)
    print(instance)


@receiver(pre_delete, sender=Car)
def car_pre_delete(sender, instance, **kwargs):
    print('### PRE DELETE ###')
    print(sender)
    print(instance)


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    print('### POST DELETE ###')
    print(sender)
    print(instance)
    

@receiver(post_save, sender=Car)
def car_post_save2(sender, instance, created, **kwargs):
    if created:
        cars_count = Car.objects.all().count()
        cars_value = Car.objects.aggregate(total_value=Sum('value'))['total_value']
        
        CarInventory.objects.create(cars_count=cars_count, cars_value=cars_value)
    else:
        print("OKOKOK", "UPDATED")
        
    

@receiver(post_delete, sender=Car)
def car_post_delete2(sender, instance, **kwargs):
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(total_value=Sum('value'))['total_value']
    
    CarInventory.objects.create(cars_count=cars_count, cars_value=cars_value)
    




