from datetime import datetime
from uuid import UUID

from sqlalchemy import inspect
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Base.metadata.schema = 'poll'


class BaseEntity:
    def as_dict(self, serialize_date=True, recurse=False, serialised_objects=None):
        """
        Transform LaunchPad entity object
        into dictionary with native and serializable types
        :return:
        """
        rval = {}
        for column in self.__table__.columns:
            value = getattr(self, column.name)

            if isinstance(value, UUID):
                value = str(value)

            if isinstance(value, datetime) and serialize_date:
                if value.tzinfo is not None:
                    value = datetime.isoformat(value.replace(tzinfo=None)) + 'Z'
                else:
                    value = datetime.isoformat(value) + 'Z'

            rval[column.name] = value

        if recurse:
            serialised_objects = [self] if not serialised_objects else serialised_objects
            variables = [i for i in vars(self) if not i[0] == '_']
            for var in variables:
                value = getattr(self, var)
                if isinstance(value, BaseEntity):
                    tmp_recurse = recurse and value not in serialised_objects
                    serialised_objects.append(value)
                    rval[var] = value.as_dict(
                        recurse=tmp_recurse,
                        serialised_objects=serialised_objects
                    )
                if isinstance(value, list):
                    for el in value:
                        if isinstance(el, BaseEntity):
                            if var not in rval:
                                rval[var] = []
                            tmp_recurse = recurse and el not in serialised_objects
                            serialised_objects.append(el)
                            rval[var].append(el.as_dict(
                                recurse=tmp_recurse,
                                serialised_objects=serialised_objects))
        return rval
