GENERAL CALENDAR
==============

This module allows to merge differently calendars in a same calendar.

Through the 'general calendar line' object, you can specify which models have
to be merged in the general calendar. For each model, you have to define the
'description' and 'date_start' fields at least. Then you can define 'date_stop'
and the 'user_id' fields.

The 'general.calendar' object contains the merged calendars. The
'general.calendar' can be updated br PostgresSQL View.

This module is based in **Super Calendar** module by `OCA Server Tools <https://github.com/OCA/server-tools/tree/10.0/super_calendar>`_.


Configuration
=============

After installing the module you can go to

*General calendar > Configuration > Add Calendars*

and create a new calendar. The Calendar Events from `Calendar <https://github.com/multidadosti-erp/odoo/tree/10.0/addons/calendar>`_ module come by default.
For instance, if you want to see project tasks and sale orders, you can create the following lines

Project Task:

.. image:: general_calendar/static/description/project_task.png
   :width: 400 px

Sale Orders:

.. image:: general_calendar/static/description/sale_order.png
   :width: 400 px

You can visualize it in the 'general calendar' main menu.

Here is a sample monthly calendar:

.. image:: general_calendar/static/description/general_calendar.png
   :width: 400 px

IMPORTANT: After update calendar list, remember of update 'General Calendar' module in
models list.

As you can see, several filters are available. A typical usage consists in
filtering by 'Module' and by your user.
Once you filtered, you can save the filter as 'Advanced filter' or even
add it to a dashboard.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/multidadosti-erp/multidadosti-addons>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed feedback.

Credits
=======

Contributors
------------
* Michell Stuttgart <michellstut@gmail.com>
