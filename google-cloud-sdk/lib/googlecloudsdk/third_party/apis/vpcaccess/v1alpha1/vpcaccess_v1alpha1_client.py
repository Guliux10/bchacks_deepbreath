"""Generated client library for vpcaccess version v1alpha1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.vpcaccess.v1alpha1 import vpcaccess_v1alpha1_messages as messages


class VpcaccessV1alpha1(base_api.BaseApiClient):
  """Generated client library for service vpcaccess version v1alpha1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://vpcaccess.googleapis.com/'

  _PACKAGE = u'vpcaccess'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1alpha1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'VpcaccessV1alpha1'
  _URL_VERSION = u'v1alpha1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new vpcaccess handle."""
    url = url or self.BASE_URL
    super(VpcaccessV1alpha1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_connectors = self.ProjectsLocationsConnectorsService(self)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsConnectorsService(base_api.BaseApiService):
    """Service class for the projects_locations_connectors resource."""

    _NAME = u'projects_locations_connectors'

    def __init__(self, client):
      super(VpcaccessV1alpha1.ProjectsLocationsConnectorsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a Serverless VPC Access connector, returns an operation.

      Args:
        request: (VpcaccessProjectsLocationsConnectorsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations/{locationsId}/connectors',
        http_method=u'POST',
        method_id=u'vpcaccess.projects.locations.connectors.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1alpha1/{+parent}/connectors',
        request_field=u'connector',
        request_type_name=u'VpcaccessProjectsLocationsConnectorsCreateRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a Serverless VPC Access connector. Returns NOT_FOUND if the.
resource does not exist.

      Args:
        request: (VpcaccessProjectsLocationsConnectorsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations/{locationsId}/connectors/{connectorsId}',
        http_method=u'DELETE',
        method_id=u'vpcaccess.projects.locations.connectors.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'VpcaccessProjectsLocationsConnectorsDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets a Serverless VPC Access connector. Returns NOT_FOUND if the resource.
does not exist.

      Args:
        request: (VpcaccessProjectsLocationsConnectorsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Connector) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations/{locationsId}/connectors/{connectorsId}',
        http_method=u'GET',
        method_id=u'vpcaccess.projects.locations.connectors.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'VpcaccessProjectsLocationsConnectorsGetRequest',
        response_type_name=u'Connector',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists Serverless VPC Access connectors.

      Args:
        request: (VpcaccessProjectsLocationsConnectorsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListConnectorsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations/{locationsId}/connectors',
        http_method=u'GET',
        method_id=u'vpcaccess.projects.locations.connectors.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1alpha1/{+parent}/connectors',
        request_field='',
        request_type_name=u'VpcaccessProjectsLocationsConnectorsListRequest',
        response_type_name=u'ListConnectorsResponse',
        supports_download=False,
    )

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = u'projects_locations_operations'

    def __init__(self, client):
      super(VpcaccessV1alpha1.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (VpcaccessProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method=u'GET',
        method_id=u'vpcaccess.projects.locations.operations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'VpcaccessProjectsLocationsOperationsGetRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the.
server doesn't support this method, it returns `UNIMPLEMENTED`.

NOTE: the `name` binding allows API services to override the binding
to use different resource name schemes, such as `users/*/operations`. To
override the binding, API services can add a binding such as
`"/v1/{name=users/*}/operations"` to their service configuration.
For backwards compatibility, the default name includes the operations
collection id, however overriding users must ensure the name binding
is the parent resource, without the operations collection id.

      Args:
        request: (VpcaccessProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations/{locationsId}/operations',
        http_method=u'GET',
        method_id=u'vpcaccess.projects.locations.operations.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1alpha1/{+name}/operations',
        request_field='',
        request_type_name=u'VpcaccessProjectsLocationsOperationsListRequest',
        response_type_name=u'ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = u'projects_locations'

    def __init__(self, client):
      super(VpcaccessV1alpha1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (VpcaccessProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations',
        http_method=u'GET',
        method_id=u'vpcaccess.projects.locations.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1alpha1/{+name}/locations',
        request_field='',
        request_type_name=u'VpcaccessProjectsLocationsListRequest',
        response_type_name=u'ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(VpcaccessV1alpha1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
