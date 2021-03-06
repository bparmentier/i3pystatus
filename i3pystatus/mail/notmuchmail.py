#!/usr/bin/env python
# -*- coding: utf-8 -*-

# note that this needs the notmuch python bindings. For more info see:
# http://notmuchmail.org/howto/#index4h2
import notmuch

from i3pystatus.mail import Backend


class Notmuch(Backend):
    """
    This class uses the notmuch python bindings to check for the
    number of messages in the notmuch database with the tags "inbox"
    and "unread"
    """

    settings = required = ("db_path",)

    def init(self):
        self.db = notmuch.Database(self.db_path)

    @property
    def unread(self):
        return notmuch.Query(self.db, "tag:unread and tag:inbox").count_messages()


Backend = Notmuch
