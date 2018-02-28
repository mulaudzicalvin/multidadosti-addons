odoo.define('calendar.systray', function (require) {
"use strict";

var core = require('web.core');
var SystrayMenu = require('web.SystrayMenu');
var session = require('web.session');
var Widget = require('web.Widget');

var CalendarItem = Widget.extend({
    template:'calendar_systray_menu.CalendarItem',
    events: {
        "click": "on_click",
    },

    start: function () {
        return this._super();
    },

    on_click: function (event) {
        event.preventDefault();
        var self = this;

        self.trigger_up('hide_app_switcher');
        self.do_action('calendar.action_calendar_event', {clear_breadcrumbs: true})
        .then(function () {
            core.bus.trigger('change_menu_section')
        });
    },

});

SystrayMenu.Items.push(CalendarItem);

});
