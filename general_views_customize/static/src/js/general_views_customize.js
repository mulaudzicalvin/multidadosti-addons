odoo.define('general_views_customize.general_views_customize', function (require) {
"use strict";

    var WebClient = require('web.WebClient');
    var core = require('web.core');
    var Dialog = require('web.Dialog');

    var ExceptionHandler = {

        init: function(parent, error) {},
        display: function() {},
    };

    WebClient.include({
        init: function(parent, client_options) {
            this._super(parent, client_options);
            this.set('title_part', {"zopenerp": "ERP@VMulti"});
        },
    });

    core.Class.include({
         show_warning: function(error) {
            this._super(error);
            if (!this.active) {
                return;
            }
            new Dialog(this, {
                size: 'medium',
//              title: "Odoo " + (_.str.capitalize(error.type) || _t("Warning")),
                title: (_.str.capitalize(error.type) || _t("Warning")),
                subtitle: error.data.title,
                $content: $('<div>').html(QWeb.render('CrashManager.warning', {error: error}))
            }).open();
        },
        show_error: function(error) {
            this._super(error);
            if (!this.active) {
                return;
            }
            new Dialog(this, {
//              title: "Odoo " + _.str.capitalize(error.type),
                title: _.str.capitalize(error.type),
                $content: QWeb.render('CrashManager.error', {error: error})
            }).open();
        },
    });

    Dialog.Class.include(ExceptionHandler, {

        display: function() {
            this._super();
            var self = this;
            var error = this.error;
            error.data.message = error.data.arguments[0];

            new Dialog(this, {
                size: 'medium',
//              title: "Odoo " + (_.str.capitalize(error.type) || "Warning"),
                title: (_.str.capitalize(error.type) || "Warning"),
                buttons: [
                    {text: error.data.arguments[2], classes : "btn-primary", click: function() {
                        window.location.href = '#action='+error.data.arguments[1];
                        self.destroy();
                    }},
                    {text: _t("Cancel"), click: function() { self.destroy(); }, close: true}
                ],
                $content: QWeb.render('CrashManager.warning', {error: error}),
            }).open();
        }

    });

});