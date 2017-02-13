odoo.define('general_views_customize.general_views_customize', function (require) {
"use strict";

    var WebClient = require('web.WebClient');

    WebClient.include({
        init: function(parent, client_options) {
            this._super(parent, client_options);
            this.set('title_part', {"zopenerp": "ERP@VMulti"});
        },
    });
});