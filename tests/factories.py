import factory

from django.db.models.signals import post_save
from faker import Factory as FakerFactory
from blogcms.settings.base import AUTH_USER_MODEL

faker = FakerFactory.create()


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.LazyAttribute(lambda x: f"manu")
    first_name = factory.LazyAttribute(lambda x: faker.first_name())
    last_name = factory.LazyAttribute(lambda x: faker.last_name())
    email = factory.LazyAttribute(lambda x: f"manu@testing.com")
    password = factory.LazyAttribute(lambda x: faker.password())
    is_active = True
    is_staff = False

    class Meta:
        model = AUTH_USER_MODEL

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        if "is_superuser" in kwargs:
            return manager.create_superuser(**kwargs["is_superuser"])
        else:
            return manager.create_user(*args, **kwargs)
