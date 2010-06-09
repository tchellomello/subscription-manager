#
# String constants for the Subscription Manager CLI/GUI
#
# Author: Pradeep Kilambi <pkilambi@redhat.com>
#
# Copyright (c) 2010 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public License,
# version 2 (GPLv2). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
# along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
#
# Red Hat trademarks are not licensed under GPLv2. No permission is
# granted to use or replicate Red Hat trademarks that are incorporated
# in this software or its documentation.
#
#

import gettext
_ = gettext.gettext

product_describe = """
PRODUCT INFO
=========================\n
Name               \t%-25s
Variant            \t%-25s
Architecture       \t%-25s
Version                  \t%-25s
\n 
"""

content_entitlement_describe = """
Name               \t%-25s
Label                    \t%-30s
Quantity                 \t%-25s
Flex Quantity      \t%-25s
Vendor             \t%-25s
URL                      \t%-30s
Enabled            \t%-25s
\n
"""

role_entitlement_describe = """
Name               \t%-25s
Description        \t%-25s
"""

subscribed_status = _("""
The subscription for %s is valid until %s.
""")

installed_product_status =  """
ProductName:        \t%-25s
Status:             \t%-25s
Expires:            \t%-25s
Subscription:       \t%-25s
ContractNumber:        \t%-25s
"""

available_subs_list = """
Name:              \t%-25s
ProductId:         \t%-25s
PoolId:            \t%-25s
quantity:          \t%-25s
Expires:           \t%-25s
"""

consumed_subs_list = """
Name:               \t%-25s
ContractNumber:       \t%-25s
SerialNumber:       \t%-25s
Active:             \t%-25s
Begins:             \t%-25s
Expires:            \t%-25s
"""

expired_status = _("""
The subscription for %s expired on %s. If you plan to continue using %s on this system you should update the subscription. If you no longer wish to use %s on this machine, you should unsubscribe and remove it from this system.
""")

unsubscribed_status = _("""
%s is installed but you are not subscribed to it. If you plan to use %s on this system, you should add a subscription. If you do not plan to use %s on this system, you should remove it from this system.
""")

not_installed_status = _(""" 
%s is not installed but you are subscribed to it. If you do not plan to use %s on this system, you should unsubscribe in order to avoid unnecessarily consuming entitlements. If you plan to use %s on this system, you should install it.\n
""")

WARN_SUBSCRIPTIONS = _("<b>\n %s subscriptions need your attention.\n\n</b>Add or Update subscriptions for products you are using.\n")

WARN_ONE_SUBSCRIPTION = _("<b>\n %s subscription need your attention.\n\n</b>Add or Update subscriptions for products you are using.\n")

COMPLIANT_STATUS = _("<b>\n All your subscriptions are in compliance.\n\n</b>Add or Update subscriptions for products you are using.")

UNSUBSCRIBE_ERROR = _("<b>Unable to perform unsubscribe.</b>\n\nPlease see /var/log/rhsm/rhsm.log for more information.")

SUBSCRIBE_REGTOKEN_ERROR = _("<b>\nCould not subscribe to token %s</b>\n\nPlease see /var/log/rhsm/rhsm.log for more information.")

SUBSCRIBE_REGTOKEN_SUCCESS = _("Successfully subscribed your system to token %s")

NO_SUBSCRIPTIONS_WARNING = _("<b>No subscriptions available for this account</b>")

NO_UPDATES_WARNING = _("<b>No subscriptions updates available</b>")

SUBSCRIBE_ERROR = _("<b>Unable to subscribe to product(s) %s</b>\n\nPlease see /var/log/rhsm/rhsm.log for more information.")

ATLEAST_ONE_SELECTION = _("<i><b>Please select atleast one subscription to apply</b></i>")

SUBSCRIBE_SUCCSSFUL = _("<i><b>Successfully consumed %s subscription(s)</b></i>")

UNEXPECTED_ERROR = _("This error shouldn't have happened. If you'd "
                                 "like to help us improve this program, please "
                                 "file a bug at bugzilla.redhat.com. Including "
                                 "the relevant parts of would be very "
                                 "helpful. Thanks!")
REGISTER_ERROR = _("<b>Unable to register the system.</b>\n\n %s\n\nPlease see /var/log/rhsm/rhsm.log for more information.")

CONFIRM_UNSUBSCRIBE = _("Are you sure you want to unsubscribe product %s")

REG_REMOTE_STATUS = _("This system is registered to <b>%s</b>")
REG_LOCAL_STATUS = _("This system's subscriptions are <b>locally-managed.</b>")

SELECT_STATUS = _("<b>Total of %s subscriptions selected for consumption.</b>")
