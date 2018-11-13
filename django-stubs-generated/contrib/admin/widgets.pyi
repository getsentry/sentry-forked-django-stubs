from collections import OrderedDict
from datetime import datetime
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Union
from uuid import UUID

from django import forms
from django.contrib.admin.sites import AdminSite
from django.db.models.fields.reverse_related import ForeignObjectRel
from django.db.models.query_utils import Q
from django.forms.fields import Field
from django.forms.widgets import ChoiceWidget, Media, Widget
from django.http.request import QueryDict
from django.utils.datastructures import MultiValueDict


class FilteredSelectMultiple(forms.SelectMultiple):
    @property
    def media(self) -> Media: ...
    verbose_name: Any = ...
    is_stacked: Any = ...
    def __init__(
        self,
        verbose_name: str,
        is_stacked: bool,
        attrs: None = ...,
        choices: Tuple = ...,
    ) -> None: ...
    def get_context(
        self,
        name: str,
        value: Union[List[Any], str],
        attrs: Optional[Dict[str, str]],
    ) -> Dict[
        str,
        Union[
            Dict[
                str,
                Union[
                    Dict[str, Union[int, str]],
                    List[
                        Tuple[
                            None,
                            List[Dict[str, Union[Dict[Any, Any], int, str]]],
                            int,
                        ]
                    ],
                    bool,
                    str,
                ],
            ],
            Dict[str, Union[Dict[str, Union[int, str]], List[str], bool, str]],
        ],
    ]: ...

class AdminDateWidget(forms.DateInput):
    attrs: Dict[str, str]
    input_type: str
    @property
    def media(self) -> Media: ...
    def __init__(
        self,
        attrs: Optional[Dict[str, Union[int, str]]] = ...,
        format: None = ...,
    ) -> None: ...

class AdminTimeWidget(forms.TimeInput):
    attrs: Dict[str, str]
    input_type: str
    @property
    def media(self) -> Media: ...
    def __init__(
        self,
        attrs: Optional[Dict[str, Union[int, str]]] = ...,
        format: None = ...,
    ) -> None: ...

class AdminSplitDateTime(forms.SplitDateTimeWidget):
    attrs: Dict[Any, Any]
    widgets: List[django.forms.widgets.DateTimeBaseInput]
    template_name: str = ...
    def __init__(self, attrs: None = ...) -> None: ...
    def get_context(
        self,
        name: str,
        value: Optional[Union[List[str], datetime]],
        attrs: Optional[Dict[str, Union[bool, str]]],
    ) -> Dict[
        str,
        Union[
            Dict[
                str,
                Optional[
                    Union[
                        Dict[str, Union[bool, str]],
                        List[
                            Dict[
                                str,
                                Optional[
                                    Union[
                                        Dict[str, Union[bool, str]], bool, str
                                    ]
                                ],
                            ]
                        ],
                        bool,
                        str,
                    ]
                ],
            ],
            str,
        ],
    ]: ...

class AdminRadioSelect(forms.RadioSelect):
    attrs: Dict[str, str]
    template_name: str = ...

class AdminFileWidget(forms.ClearableFileInput):
    attrs: Dict[Any, Any]
    template_name: str = ...

def url_params_from_lookup_dict(
    lookups: Union[
        Dict[str, Callable],
        Dict[str, List[str]],
        Dict[str, Tuple[str, str]],
        Dict[str, bool],
        Dict[str, str],
        Q,
    ]
) -> Dict[str, str]: ...

class ForeignKeyRawIdWidget(forms.TextInput):
    attrs: Dict[Any, Any]
    template_name: str = ...
    rel: django.db.models.fields.reverse_related.ManyToOneRel = ...
    admin_site: django.contrib.admin.sites.AdminSite = ...
    db: None = ...
    def __init__(
        self,
        rel: ForeignObjectRel,
        admin_site: AdminSite,
        attrs: None = ...,
        using: None = ...,
    ) -> None: ...
    def get_context(
        self,
        name: str,
        value: Optional[Union[List[int], int, str, UUID]],
        attrs: Optional[Dict[str, Union[bool, str]]],
    ) -> Dict[
        str,
        Union[
            Dict[str, Optional[Union[Dict[str, Union[bool, str]], bool, str]]],
            str,
        ],
    ]: ...
    def base_url_parameters(self) -> Dict[str, str]: ...
    def url_parameters(self) -> Dict[str, str]: ...
    def label_and_url_for_value(
        self, value: Union[int, str, UUID]
    ) -> Tuple[str, str]: ...

class ManyToManyRawIdWidget(ForeignKeyRawIdWidget):
    admin_site: django.contrib.admin.sites.AdminSite
    attrs: Dict[Any, Any]
    db: None
    rel: django.db.models.fields.reverse_related.ManyToManyRel
    template_name: str = ...
    def get_context(
        self,
        name: str,
        value: Optional[List[int]],
        attrs: Optional[Dict[str, str]],
    ) -> Dict[str, Union[Dict[str, Union[Dict[str, str], bool, str]], str]]: ...
    def url_parameters(self) -> Dict[Any, Any]: ...
    def label_and_url_for_value(self, value: List[int]) -> Tuple[str, str]: ...
    def value_from_datadict(
        self, data: QueryDict, files: MultiValueDict, name: str
    ) -> None: ...
    def format_value(self, value: Optional[List[int]]) -> str: ...

class RelatedFieldWidgetWrapper(forms.Widget):
    template_name: str = ...
    needs_multipart_form: bool = ...
    attrs: Dict[Any, Any] = ...
    choices: django.forms.models.ModelChoiceIterator = ...
    widget: django.contrib.admin.widgets.AutocompleteSelect = ...
    rel: django.db.models.fields.reverse_related.ManyToOneRel = ...
    can_add_related: bool = ...
    can_change_related: bool = ...
    can_delete_related: bool = ...
    can_view_related: bool = ...
    admin_site: django.contrib.admin.sites.AdminSite = ...
    def __init__(
        self,
        widget: ChoiceWidget,
        rel: ForeignObjectRel,
        admin_site: AdminSite,
        can_add_related: Optional[bool] = ...,
        can_change_related: bool = ...,
        can_delete_related: bool = ...,
        can_view_related: bool = ...,
    ) -> None: ...
    def __deepcopy__(
        self,
        memo: Dict[
            int, Union[List[Union[Field, Widget]], OrderedDict, Field, Widget]
        ],
    ) -> RelatedFieldWidgetWrapper: ...
    @property
    def is_hidden(self) -> bool: ...
    @property
    def media(self) -> Media: ...
    def get_related_url(
        self, info: Tuple[str, str], action: str, *args: Any
    ) -> str: ...
    def get_context(
        self,
        name: str,
        value: Optional[Union[int, str]],
        attrs: Optional[Dict[str, Union[bool, str]]],
    ) -> Dict[str, Union[bool, str]]: ...
    def value_from_datadict(
        self, data: QueryDict, files: MultiValueDict, name: str
    ) -> Optional[Union[List[str], str]]: ...
    def value_omitted_from_data(
        self, data: Dict[Any, Any], files: Dict[Any, Any], name: str
    ) -> bool: ...
    def id_for_label(self, id_: str) -> str: ...

class AdminTextareaWidget(forms.Textarea):
    attrs: Dict[str, str]
    def __init__(self, attrs: None = ...) -> None: ...

class AdminTextInputWidget(forms.TextInput):
    attrs: Dict[str, str]
    input_type: str
    def __init__(self, attrs: None = ...) -> None: ...

class AdminEmailInputWidget(forms.EmailInput):
    attrs: Dict[str, str]
    input_type: str
    def __init__(self, attrs: None = ...) -> None: ...

class AdminURLFieldWidget(forms.URLInput):
    attrs: Dict[str, str]
    input_type: str
    template_name: str = ...
    def __init__(self, attrs: None = ...) -> None: ...
    def get_context(
        self, name: str, value: Optional[str], attrs: Optional[Dict[str, str]]
    ) -> Dict[
        str, Union[Dict[str, Optional[Union[Dict[str, str], bool, str]]], str]
    ]: ...

class AdminIntegerFieldWidget(forms.NumberInput):
    attrs: Dict[str, str]
    input_type: str
    class_name: str = ...
    def __init__(self, attrs: None = ...) -> None: ...

class AdminBigIntegerFieldWidget(AdminIntegerFieldWidget):
    class_name: str = ...

SELECT2_TRANSLATIONS: Any

class AutocompleteMixin:
    url_name: str = ...
    rel: Any = ...
    admin_site: Any = ...
    db: Any = ...
    choices: Any = ...
    attrs: Any = ...
    def __init__(
        self,
        rel: ForeignObjectRel,
        admin_site: AdminSite,
        attrs: Optional[Dict[str, str]] = ...,
        choices: Tuple = ...,
        using: None = ...,
    ) -> None: ...
    def get_url(self) -> str: ...
    def build_attrs(
        self,
        base_attrs: Dict[str, str],
        extra_attrs: Optional[Dict[str, Union[bool, str]]] = ...,
    ) -> Dict[str, Union[bool, str]]: ...
    def optgroups(
        self,
        name: str,
        value: List[str],
        attr: Dict[str, Union[bool, str]] = ...,
    ) -> List[
        Tuple[
            None,
            List[Dict[str, Union[Dict[str, bool], Set[str], int, str]]],
            int,
        ]
    ]: ...
    @property
    def media(self) -> Media: ...

class AutocompleteSelect(AutocompleteMixin, forms.Select): ...
class AutocompleteSelectMultiple(AutocompleteMixin, forms.SelectMultiple): ...