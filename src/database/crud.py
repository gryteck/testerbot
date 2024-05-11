import logging
from sqlalchemy import exc


def db_exception(function):
    def inner(self, *args, **kwargs):
        try:
            res = function(self, *args, **kwargs)
        except exc.SQLAlchemyError as e:
            logging.warning(e)
            self.close()
            self.__init__()
            res = None
        return res

    return inner


class Postgres:
    pass
