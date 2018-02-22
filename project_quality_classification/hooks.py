def uninstall_hook(cr, registry):
    # convert priority from very high to high to avoid inconsistency
    # after the module is uninstalled
    cr.execute(
        "UPDATE project_task SET priority = '1' WHERE priority in ('3', '4')"
    )

    cr.execute(
        "UPDATE project_task SET priority = '0' WHERE priority in ('1', '2')"
    )
