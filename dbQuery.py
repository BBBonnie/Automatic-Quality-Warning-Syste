import sqlite3 as sql
import time


def listComponents():
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM componentTable")

            con.commit()
            response = cur.fetchall()
            msg = "done"
    except:
        con.rollback()
        msg = "failed"

    finally:
        con.close()
        return dict(response=response, msg=msg)


def addComponents(name, contact, manufacturer, failure_rate, price, quantity):
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO componentTable(name, contact, manufacturer, failure_rate, price, quantity)"
                " VALUES(?, ?, ?, ?, ?, ?)",
                (name, contact, manufacturer, failure_rate, price, quantity))

            con.commit()
            msg = "added comp"
    except:
        con.rollback()
        msg = "failed to add comp"

    finally:
        con.close()
        return dict(msg=msg)


def update_components(component_id, component_name, component_contact, component_manufacturer, component_failure_rate, component_price, component_quantity):
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute('UPDATE componentTable SET name = ?, contact = ?, '
                        'manufacturer = ?, failure_rate = ?, price = ?, quantity = ?'
                        ' WHERE id = ?',
                        (component_name, component_contact, component_manufacturer, component_failure_rate, component_price, component_quantity, component_id))
            con.commit()
            msg = "updated"
    except:
        con.rollback()
        msg = "failed to update"
    finally:
        con.close()
        return dict(msg=msg)


def removeComponent(cid):
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute(
                "DELETE FROM componentTable WHERE id=" + str(cid))

            con.commit()
            msg = "deleted component"
    except:
        con.rollback()
        msg = "failed to delete component"

    finally:
        con.close()
        return dict(msg=msg)


def listFailmodes():
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM failModesTable")

            con.commit()
            response = cur.fetchall()
            msg = "done"
    except:
        con.rollback()
        msg = "failed"

    finally:
        con.close()
        return dict(response=response, msg=msg)


def addFailMode(name, failcode):
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO failModesTable(name, code ) VALUES(?, ?)",
                        (name, failcode))
            con.commit()
            msg = "added fmode"
    except:
        con.rollback()
        msg = "failed to add fmode"

    finally:
        con.close()
        return dict(msg=msg)


def update_failmode(failmode_id, failmode_name, failmode_code):
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute('UPDATE failModesTable SET name = ?, code = ?'
                        ' WHERE id = ?',
                        (failmode_name, failmode_code, failmode_id))
            con.commit()
            msg = "updated"
    except:
        con.rollback()
        msg = "failed to update"
    finally:
        con.close()
        return dict(msg=msg)


def getComponentById(cid):
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM componentTable WHERE id=" + cid)
            component = cur.fetchone()
            component = component[1]
            con.commit()
    except:
        con.rollback()
        component = "fail"

    finally:
        con.close()
        return component


def getFailModeById(fid):
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM failModesTable WHERE id=" + fid)
            fail_mode = cur.fetchone()
            fail_mode = fail_mode[1]
            con.commit()
    except:
        con.rollback()
        fail_mode = "fail"

    finally:
        con.close()
        return fail_mode


def listMappings():
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM mappingTable")

            con.commit()
            response = cur.fetchall()
            msg = "done"
    except:
        con.rollback()
        msg = "fail"

    finally:
        con.close()
        return dict(response=response, msg=msg)


def addMapping(fail_code, component_id, fail_mode_id):
    component = getComponentById(component_id)
    failmode = getFailModeById(fail_mode_id)
    try:
        with sql.connect("database.db") as con:
            # print(fail_code, component, failmode, component_id, fail_mode_id, '#####')
            cur = con.cursor()
            cur.execute(
                "INSERT INTO mappingTable(fail_code, component, fail_mode) "
                "VALUES(?, ?, ?)",
                (fail_code, component, failmode))

            con.commit()
            msg = "done"
    except:
        con.rollback()
        msg = "failed"

    finally:
        con.close()
        return dict(msg=msg)


def removeMapping(mid):
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            print(mid)
            cur.execute(
                "DELETE FROM mappingTable WHERE id=" + str(mid))

            con.commit()
            msg = "deleted mapping"
    except:
        con.rollback()
        msg = "failed to delete mapping"

    finally:
        con.close()
        return dict(msg=msg)


def removeFailMode(fid):
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute(
                "DELETE FROM failModesTable WHERE id=" + str(fid))

            con.commit()
            msg = "deleted fmode"
    except:
        con.rollback()
        msg = "failed to delete fmode"

    finally:
        con.close()
        return dict(msg=msg)


