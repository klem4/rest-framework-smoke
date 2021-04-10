from typing import TYPE_CHECKING
from unittest import skip

from rest_framework.test import APITestCase

if TYPE_CHECKING:  # pragma: no cover
    CheckListTarget = APITestCase
else:
    CheckListTarget = object


class CommonAPICheckList(CheckListTarget):
    """
    A collection of tests for CRUDL API
    """

    @skip("Implement me")
    def test_authorization(self):
        """
        checks whether API performs client authorization
        """
        raise NotImplementedError()


class ReadAPICheckList(CommonAPICheckList):
    """
    A collection of tests for read-only API (list/detail)
    """
    @skip("Implement me")
    def test_read_permissions(self):
        """
        object list/detail API permissions check
        """
        raise NotImplementedError()

    @skip("Implement me")
    def test_list_default_filters(self):
        """
        check objects filtered by default in object list/detail API
        """
        raise NotImplementedError()


# noinspection PyAbstractClass
class ListAPICheckList(ReadAPICheckList):
    """
    A collection of tests for object list api
    """
    @skip("Implement me")
    def test_list_filter_params(self):
        """
        check object list filtering
        """
        raise NotImplementedError()

    @skip("Implement me")
    def test_list_ordering_params(self):
        """
        check ordering parametrization in object list API
        """
        raise NotImplementedError()

    @skip("Implement me")
    def test_list_default_ordering(self):
        """
        checks default ordering in object list API
        """
        raise NotImplementedError()

    @skip("Implement me")
    def test_list_format(self):
        """
        check object list API format
        """
        raise NotImplementedError()

    @skip("Implement me")
    def test_object_list_smoke(self):
        """
        check that object list API returns an object list
        """
        raise NotImplementedError()


# noinspection PyAbstractClass
class RetrieveAPICheckList(ReadAPICheckList):
    """
    A collection of tests for object detail API.
    """

    @skip("Implement me")
    def test_detail_format(self):
        """
        check object detail API format
        """
        raise NotImplementedError()

    @skip("Implement me")
    def test_retrieve_object_smoke(self):
        """
        check that object detail API returns an object
        """
        raise NotImplementedError()


# noinspection PyAbstractClass
class ReadOnlyAPICheckList(ReadAPICheckList):
    """
    A collection of tests for read-only API (without create/update/delete)
    """

    @skip("Implement me")
    def test_create_not_allowed(self):
        """
        check that API does not allow object creation
        """
        raise NotImplementedError()

    @skip("Implement me")
    def test_update_not_allowed(self):
        """
        check that API does not allow object partial and full update
        """
        raise NotImplementedError()

    @skip("Implement me")
    def test_delete_not_allowed(self):
        """
        check that API does not allow object deletion
        """
        raise NotImplementedError()


class CreateAPICheckList(CommonAPICheckList):
    """
    A collection of tests for create object API.
    """

    @skip("Implement me")
    def test_create_permissions(self):
        """
        check create object API permissions
        """
        raise NotImplementedError()

    @skip("Implement me")
    def test_create_validation(self):
        """
        check validation for object creation API
        """
        raise NotImplementedError()

    @skip("Implement me")
    def test_create_format(self):
        """
        check create objects API response format
        """
        raise NotImplementedError()

    @skip("Implement me")
    def test_create_object_smoke(self):
        """
        check that create API really creates an object in DB
        """
        raise NotImplementedError()


class UpdateAPICheckList(CommonAPICheckList):
    """
    A collection of tests for object update API.
    """

    @skip("Implement me")
    def test_update_permissions(self):
        """
        check update permissions
        """
        raise NotImplementedError()


# noinspection PyAbstractClass
class FullUpdateAPICheckList(UpdateAPICheckList):
    """
    A collection of tests for full update API.
    """

    @skip("Implement me")
    def test_full_update_validation(self):
        """
        check validation for object update API
        """
        raise NotImplementedError()

    @skip("Implement me")
    def test_full_update_format(self):
        """
        check update objects API response format
        """
        raise NotImplementedError()

    @skip("Implement me")
    def test_full_update_smoke(self):
        """
        check that update API really updates an object in DB
        """
        raise NotImplementedError()

    @skip("Implement me")
    def test_full_update_read_only_fields(self):
        """
        checks fields that are forbidden to update
        """
        raise NotImplementedError()


# noinspection PyAbstractClass
class PartialUpdateAPICheckList(UpdateAPICheckList):
    """
    A collection of tests for partial update API.
    """

    @skip("Implement me")
    def test_partial_update_validation(self):
        """
        check validation for object update API
        """
        raise NotImplementedError()

    @skip("Implement me")
    def test_partial_update_read_only_fields(self):
        """
        checks fields that are forbidden to update
        """
        raise NotImplementedError()

    @skip("Implement me")
    def test_partial_update_format(self):
        """
        check update objects API response format
        """
        raise NotImplementedError()

    @skip("Implement me")
    def test_partial_update_smoke(self):
        """
        check that update API partially updates an object in DB
        """
        raise NotImplementedError()


class DeleteAPICheckList(CommonAPICheckList):
    """
    A collection of tests for delete object API.
    """

    @skip("Implement me")
    def test_delete_permissions(self):
        """
        check delete object permissions
        """
        raise NotImplementedError()

    @skip("Implement me")
    def test_delete_object_smoke(self):
        """
        check that delete API really deletes an object in DB
        """
        raise NotImplementedError()


# noinspection PyAbstractClass
class CompleteAPICheckList(CreateAPICheckList,
                           RetrieveAPICheckList,
                           FullUpdateAPICheckList,
                           PartialUpdateAPICheckList,
                           DeleteAPICheckList,
                           ListAPICheckList):
    """
    A collection of tests for whole-CRUDL API.
    """
