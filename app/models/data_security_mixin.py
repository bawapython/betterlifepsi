# encoding=utf-8


class DataSecurityMixin(object):

    from flask_login import current_user

    """
    To control security on data level
    To decide whether a user could delete/edit a specific row.
    """

    def __init__(self):
        pass

    def can_delete(self):
        """
        Whether a user could delete a specif row.
        :return: True if can, otherwise false.
        """
        return True

    def can_edit(self, user=current_user):
        if hasattr(self, 'organization_id'):
            return (user.organization_id == self.organization_id or
                    self.organization in user.organization.all_children)
        return False

    def can_view_detail(self, user=current_user):
        if hasattr(self, 'organization_id'):
            return (user.organization_id == self.organization_id or
                    self.organization in user.organization.all_children)
        return False