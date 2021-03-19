# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from iso8601 import ParseError
from iso8601 import iso8601

from .generated_media import GeneratedMedia
from .report_response import ReportResponse


class CheckResponse(object):
    """
    Represents the base attributes for a check for any given session
    """

    def __init__(self, data=None):
        """
        :param data: the data to parse
        :type data: dict or None
        """
        if data is None:
            data = dict()

        self.__id = data.get("id", None)
        self.__state = data.get("state", None)
        self.__type = data.get("type", None)
        self.__resources_used = data.get("resources_used", [])

        self.__report = (
            ReportResponse(data["report"])
            if data.get("report", None) is not None
            else None
        )
        self.__generated_media = [
            GeneratedMedia(media) for media in data.get("generated_media", [])
        ]

        self.__created = self.__parse_date(data.get("created", None))
        self.__last_updated = self.__parse_date(data.get("last_updated", None))

    @staticmethod
    def __parse_date(date):
        """
        Attempts to parse a date from string using the
        iso8601 library.  Returns None if there was an error

        :param date: the datestring to parse
        :type date: str
        :return: the parsed date
        :rtype: datetime.datetime or None
        """
        if date is None:
            return date

        try:
            return iso8601.parse_date(date)
        except ParseError:
            return None

    @property
    def id(self):
        """
        The ID of the check

        :return: the ID
        :rtype: str or None
        """
        return self.__id

    @property
    def type(self):
        """
        The type of the check

        :return: the type
        :rtype: str or None
        """
        return self.__type

    @property
    def state(self):
        """
        The state of the check, e.g. "COMPLETED"

        :return: the state
        :rtype: str or None
        """
        return self.__state

    @property
    def resources_used(self):
        """
        The resources used by the check

        :return: the list of resources used
        :rtype: list[str]
        """
        return self.__resources_used

    @property
    def created(self):
        """
        The date the check was created

        :return: the created date
        :rtype: datetime.datetime or None
        """
        return self.__created

    @property
    def last_updated(self):
        """
        The date the check was last updated

        :return: the last updated date
        :rtype: datetime.datetime or None
        """
        return self.__last_updated

    @property
    def generated_media(self):
        """
        The list of media generated by the check

        :return: the list of generated media
        :rtype: list[GeneratedMedia]
        """
        return self.__generated_media

    @property
    def report(self):
        """
        Report for the check

        :return: the report
        :rtype: ReportResponse or None
        """
        return self.__report


class AuthenticityCheckResponse(CheckResponse):
    """
    Represents a Document Authenticity check for a given session
    """

    pass


class FaceMatchCheckResponse(CheckResponse):
    """
    Represents a FaceMatch check for a given session
    """

    pass


class LivenessCheckResponse(CheckResponse):
    """
    Represents a Liveness check for a given session
    """

    pass


class TextDataCheckResponse(CheckResponse):
    """
    Represents a Text Data check for a given session
    """

    pass


class IDDocumentComparisonCheckResponse(CheckResponse):
    """
    Represents an Identity Document Comparison check for a given session
    """

    pass


class SupplementaryDocumentTextDataCheckResponse(CheckResponse):
    """
    Represents a Supplementary Document Text Data check for a given session
    """

    pass


class RequestedThirdPartyIdentityCheckResponse(CheckResponse):
    """
    Represents a third party identity check for a given session
    """

    pass
