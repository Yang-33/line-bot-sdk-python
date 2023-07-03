# coding: utf-8

"""
    Webhook Type Definition

    Webhook event definition of the LINE Messaging API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictBool

class DeliveryContext(BaseModel):
    """
    webhook's delivery context information
    """
    is_redelivery: StrictBool = Field(..., alias="isRedelivery", description="Whether the webhook event is a redelivered one or not.")

    __properties = ["isRedelivery"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> DeliveryContext:
        """Create an instance of DeliveryContext from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DeliveryContext:
        """Create an instance of DeliveryContext from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DeliveryContext.parse_obj(obj)

        _obj = DeliveryContext.parse_obj({
            "is_redelivery": obj.get("isRedelivery")
        })
        return _obj

