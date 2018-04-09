odoo.define('web_custom_dialogs.Dialog', function (require) {
"use strict";

    var Dialog = require('web.Dialog');
    var core = require('web.core');
    var _t = core._t;

    var CustomDialog = Dialog.include({
        init: function (parent, options) {
            options = _.defaults(options || {}, {
                title: _t('MultiERP'), subtitle: '',
                size: 'large',
                dialogClass: '',
                $content: false,
                buttons: [{ text: _t("Ok"), close: true }],
                technical: true,
            });

            options.title = options.title.replace('Odoo', 'MultiERP');
            options.subtitle = options.subtitle.replace('Odoo ', 'MultiERP ');
            if (options.$content && options.$content[0].innerHTML){
                options.$content[0].innerHTML = options.$content[0].innerHTML.replace('Odoo ', 'MultiERP ');
            }
            this._super(parent, options)
        },
    });
});
