from datetime import timedelta

import pytest
from django.contrib import auth
from django.http import Http404
from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils.timezone import now
from faker import Faker
from modeltranslation.manager import MultilingualManager

from lite_cms_core.managers import BaseEntityManager
from lite_cms_core.models import (
    CONTENT_STATUS_DRAFT,
    BaseEntity,
    _base_concrete_model,
    base_concrete_model,
    unique_slug,
    wrapped_manager,
)
from lite_cms_core_sample.models import BaseItem, SluggedItem

User = auth.get_user_model()


class TestItem(BaseEntity):
    """
    Objects for testing the BaseEntity model without search_fields and
    no method 'get_absolute_url'.
    """
    search_fields = {}


class BaseEntityTest(TestCase):

    def setUp(self) -> None:
        self.fake = Faker("de_DE")
        self.base_item = BaseItem.objects.create(
            title=" ".join(self.fake.words()),
        )
        self.slugged_item = SluggedItem.objects.create(
            title=" ".join(self.fake.words()),
        )
        self.test_item = TestItem(title=" ".join(self.fake.words()))

    def test_base_item_str(self):
        self.assertEqual(self.base_item.__str__(), self.base_item.title)

    def test_base_unique_slug(self):
        items = SluggedItem.objects.all()
        slug = unique_slug(items, "slug", self.slugged_item.slug)
        self.assertEqual(slug, f"{self.slugged_item.slug}-1")

    def test_base_unique_slug_multiple_existing(self):
        self.other_slugged_item = SluggedItem.objects.create(
            title=self.slugged_item.title,
        )
        items = SluggedItem.objects.all()
        slug = unique_slug(items, "slug", self.slugged_item.slug)
        self.assertEqual(slug, f"{self.slugged_item.slug}-2")

    def test_base_item_save_sets_publish_date(self):
        td = now() - self.base_item.publish_date
        # 1 minute ago counts as equal here...
        self.assertTrue(td < timedelta(minutes=1))

    def test_base_item_has_status(self):
        self.assertTrue(hasattr(self.base_item, "status"))

    def test_base_item_is_published(self):
        # Status default for BaseEntity is CONTENT_STATUS_PUBLISHED
        self.assertTrue(self.base_item.published)

    def test_base_item_not_published_by_status(self):
        self.base_item.status = CONTENT_STATUS_DRAFT
        self.base_item.save()
        self.assertFalse(self.base_item.published)

    def test_base_item_is_published_for_staff(self):
        self.base_item.status = CONTENT_STATUS_DRAFT
        self.base_item.save()
        self.user = User.objects.create(
            username=self.fake.user_name(),
            is_staff=True,
        )
        items = BaseItem.objects.published(for_user=self.user)
        self.assertIn(self.base_item, items)

    def test_base_item_get_by_natural_key(self):
        item = SluggedItem.objects.get_by_natural_key(slug=self.slugged_item.slug)
        self.assertEqual(item.title, self.slugged_item.title)

    def test_base_item_has_date_fields(self):
        self.assertTrue(hasattr(self.base_item, "publish_date"))
        self.assertTrue(hasattr(self.base_item, "expiry_date"))

    def test_base_item_not_published_by_publish_date(self):
        self.base_item.publish_date = now() + timedelta(days=1)
        self.base_item.save()
        self.assertFalse(self.base_item.published)

    def test_base_item_not_published_by_expiry_date(self):
        self.base_item.expiry_date = now() - timedelta(days=1)
        self.base_item.save()
        self.assertFalse(self.base_item.published)

    def test_base_item_get_next_by_publish_date(self):
        self.base_item.publish_date = now() - timedelta(days=2)
        self.base_item.save()
        newer_base_item = BaseItem.objects.create(
            title=" ".join(self.fake.words()),
            publish_date=now() - timedelta(days=1),
        )
        self.assertEqual(
            self.base_item.get_next_by_publish_date(),
            newer_base_item,
        )

    def test_base_item_get_previous_by_expiry_date(self):
        self.base_item.publish_date = now() - timedelta(days=1)
        self.base_item.save()
        older_base_item = BaseItem.objects.create(
            title=" ".join(self.fake.words()),
            publish_date=now() - timedelta(days=2),
        )
        self.assertEqual(
            self.base_item.get_previous_by_publish_date(),
            older_base_item,
        )

    def test_base_item_get_absolute_url(self):
        self.assertEqual(
            self.base_item.get_absolute_url(),
            reverse("base-item-detail", kwargs={"pk": self.base_item.pk}),
        )

    def test_base_item_no_get_absolute_url(self):
        with pytest.raises(NotImplementedError):
            self.test_item.get_absolute_url()

    def test__base_concrete_model_is_none(self):
        cls = _base_concrete_model(SluggedItem, BaseItem)
        self.assertIsInstance(cls, type(None))

    def test_base_get_slug_translation(self):
        with override_settings(USE_MODELTRANSLATION=True):
            slug = self.slugged_item.get_slug(attr="title")
            self.assertIsInstance(slug, str)

    def test_base_concrete_model(self):
        cls = base_concrete_model(BaseEntity, SluggedItem)
        self.assertIsInstance(self.slugged_item, cls)

    def test_base_prevnt_unpublished_access_detail_view_404(self):
        self.base_item.status = CONTENT_STATUS_DRAFT
        self.base_item.save()
        response = self.client.get(self.base_item.get_absolute_url())
        self.assertEqual(response.status_code, 404)

    def test_base_prevnt_unpublished_access_detail_view_200(self):
        response = self.client.get(self.base_item.get_absolute_url())
        self.assertEqual(response.status_code, 200)


class BaseEntityManagerTest(TestCase):

    def setUp(self) -> None:
        self.fake = Faker("de_DE")
        for _ in range(5):
            BaseItem.objects.create(
                title=" ".join(self.fake.words()),
            )
        self.base_item = BaseItem.objects.create(
            title="This is a text for testing",
        )

    def test_wrapped_manager_multilingual(self):
        with override_settings(USE_MODELTRANSLATION=True):
            cls = wrapped_manager(BaseEntityManager)
            self.assertIsInstance(cls, MultilingualManager)


    def test_base_item_search(self):
        self.assertEqual(
            BaseItem.objects.search("testing"),
            [self.base_item],
        )

    def test_base_item_search_no_search_field(self):
        self.assertEqual(
            BaseItem.objects.search("", search_fields={}),
            [],
        )

    def test_base_item_search_with_search_fields(self):
        self.assertEqual(
            BaseItem.objects.search("testing", search_fields=["title"]),
            [self.base_item],
        )
