"""
    Python 3.6 32bit
    Author: David Schulmeister
    Date: 08-DEC-2017

    Project--valv_assy_wip

    Batch program

    THIS PROGRAM PRINTS ACCOUNTING
    REPORT OF DOLLAR AMOUNT RELIEVED
    FOR THAT DAY

"""
# Import section
# from math import sin, cos, radians, tan, pi, isnan, isinf

from datetime import datetime
from builtins import float
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from ValvAssyWipCursors import *
from HeaderFooter import *
from OracleConnection import *

"""
    Variables and programm 
    start methods
    and file creation
"""
print(sys.version + '\n')
minimum_quantity = 65000


def main():
    h = HeaderFooter()
    v = ValvAssyWipCursors()

    if len(sys.argv) <= 1:
        ent_dat = today
    else:
        if sys.argv[1] == "":
            ent_dat = today
        else:
            ent_dat = sys.argv[1]
    # ent_dat = today.strftime('%d-%b-%y').upper()
    # ent_dat = '19-DEC-17'
    # Create PDF Canvas
    c = canvas.Canvas(pdffilename, pagesize=landscape(letter))

    r = 0
    total = 0
    """
        C class or D class total variables
    """
    classctotmc = classctotlc = classctotmoc = classctotloc = classctot = 0
    """
        Rough Castings total variables
    """
    gtotmc1 = gtotlc1 = gtotloc1 = gtot1 = 0
    """
        Raw Material total variables
    """
    gtotmc3 = gtotlc3 = gtotloc3 = gtot3 = 0
    """
        Purchased Parts total variables
    """
    gtotmc5 = gtotlc5 = gtotloc5 = gtot5 = 0
    """
       Manufactured parts total variables
    """
    gtotmcman = gtotlcman = gtotlocman = gtotman = 0
    """
        Grand Total variables
    """
    gtotmc = gtotmoc = gtotlc = gtotloc = gtot = 0
    """
        MATERIAL OVERHEAD Totals
    """
    vrc = vbs = vpp = vmp = gtotv = 0
    """
        Variables for pdf canvas
    """
    # puts line at top left
    x = 20
    y = 514
    # Set columns right position to add to x cord
    col2 = 90
    col3 = 250
    col4 = 335
    col5 = 420
    col6 = 515
    col7 = 590
    col8 = 665
    """
        Start retrieving data from database.
        Then put the data into respective variables.
        Print to pdf file.
    """
    curs1 = v.curs1()
    curs1_curs = conn.cursor()
    curs1_curs.execute(curs1, {'actdat': ent_dat})

    r = h.header(c, ent_dat)
    r = h.formheader1(c, r)
    r = h.formheader2(c, r)

    for curs1_curs in curs1_curs:
        y = y - 12
        c.setFont('Helvetica', 10, leading=None)
        c.drawString(x, y, curs1_curs[0])

        """
            Order total variables
        """
        ordtotmc = ordertotlc = ordtotmoc = ordtotloc = ordtot = 0

        concde = curs1_curs[0]
        # print(concde)
        """
            Return the select and execute the cursor
            for the data needed for the Order.
        """
        curs2 = v.curs2()
        curs2_curs = conn.cursor()
        curs2_curs.execute(curs2, {'concde': concde, 'actdat': ent_dat})

        for curs2_curs in curs2_curs:
            totmc = totlc = totmoc = totloc = tot = 0
            actqty = 0
            if curs2_curs[5] != 'X':
                """
                print(curs2_curs[0])  # partactivity_pn_cde
                print(curs2_curs[1])  # actqty
                print(curs2_curs[2])  # prodline
                print(curs2_curs[3])  # tmc TOTMC
                print(curs2_curs[4])  # tlc TOTLC
                print(curs2_curs[5])  # inv_cls
                print(curs2_curs[6])  # pnlevel
                print(curs2_curs[7])  # stdmoc_dol TOTLOC
                print(curs2_curs[8])  # stdloc_dol STD_OVERHEAD
                """

                """
                    Add the C Class parts
                """
                if curs2_curs[5] == 'C' or curs2_curs[5] == 'D':
                    classctotmc += (float(curs2_curs[1])*float(curs2_curs[3]))
                    classctotmoc += (float(curs2_curs[1]) * float(curs2_curs[7]))
                    classctotlc += (float(curs2_curs[1]) * float(curs2_curs[4]))
                    classctotloc += (float(curs2_curs[1]) * float(curs2_curs[8]))
                else:
                    """
                        Put curs2_curs objects into variables
                        curs2_curs.fetchone()[0]
                    """
                    pncode = curs2_curs[0]
                    actqty += float(curs2_curs[1])
                    totmc += (float(curs2_curs[1])*float(curs2_curs[3]))
                    totlc += (float(curs2_curs[1]) * float(curs2_curs[4]))
                    totmoc += (float(curs2_curs[1]) * float(curs2_curs[7]))
                    totloc += (float(curs2_curs[1]) * float(curs2_curs[8]))
                    tot += totmc+totlc+totmoc+totloc

                    if curs2_curs[6] == '1':
                        vrc += totmoc
                        gtotmc1 += totmc
                        gtotlc1 += totlc
                        gtotloc1 += totloc
                        gtot1 += totmc + totlc + totloc + totmoc
                    elif curs2_curs[6] == '3':
                        vbs += totmoc
                        gtotmc3 += totmc
                        gtotlc3 += totlc
                        gtotloc3 += totloc
                        gtot3 += totmc + totlc + totloc + totmoc
                    elif curs2_curs[6] == '5':
                        vpp += totmoc
                        gtotmc5 += totmc
                        gtotlc5 += totlc
                        gtotloc5 += totloc
                        gtot5 += totmc + totlc + totloc + totmoc
                    else:
                        vmp += totmoc
                        gtotmcman += totmc
                        gtotlcman += totlc
                        gtotlocman += totloc
                        gtotman += totmc + totlc + totloc + totmoc
                    # grant total for 1,3,5, and other inv level classes for material overhead

                    gtotv += totmoc

                """
                    Print the Part Number Totals
                """
                # Get data into pdf
                c.setFont('Helvetica', 10, leading=None)
                c.drawString(col2, y, pncode)
                c.drawRightString(col3, y, "{:>8.2f}".format(actqty))
                c.drawRightString(col4, y, "{:>8.2f}".format(totmc))
                c.drawRightString(col5, y, "{:>8.2f}".format(totmoc))
                c.drawRightString(col6, y, "{:>8.2f}".format(totlc))
                c.drawRightString(col7, y, "{:>8.2f}".format(totloc))
                c.drawRightString(col8, y, "{:>8.2f}".format(tot))
                # Incement y cord for next position and row(r) count
                y = y - 12
                r += 1
                # if row count is 43 or more start a new page
                if r >= 46:
                    x = 20
                    y = 502
                    c.line(20, 30, 750, 30)
                    c.setFont('Helvetica-Bold', 10, leading=None)
                    c.drawCentredString(400, 20, 'Continued on next Page')
                    c.showPage()
                    r = h.header(c, ent_dat)
                    r = h.formheader1(c, r)
                    r = h.formheader2(c, r)

                """
                    Add the Order Totals
                """
                ordtotmc += totmc
                ordertotlc += totlc
                ordtotmoc += totmoc
                ordtotloc += totloc
                ordtot += tot

        """
            Print the order total
        """
        c.drawString(col3 + 9, y + 11, 73 * '_')
        c.setFont('Helvetica', 10, leading=None)
        c.drawString(col2, y, 'TOTAL')
        c.drawRightString(col4, y, "{:>8.2f}".format(ordtotmc))
        c.drawRightString(col5, y, "{:>8.2f}".format(ordtotmoc))
        c.drawRightString(col6, y, "{:>8.2f}".format(ordertotlc))
        c.drawRightString(col7, y, "{:>8.2f}".format(ordtotloc))
        c.drawRightString(col8, y, "{:>8.2f}".format(ordtot))
        # Incement y cord for next position and row(r) count
        y = y - 12
        r += 2
        # if row count is 43 or more start a new page
        if r >= 46:
            x = 20
            y = 502
            c.line(20, 30, 750, 30)
            c.setFont('Helvetica-Bold', 10, leading=None)
            c.drawCentredString(400, 20, 'Continued on next Page')
            c.showPage()
            r = h.header(c, ent_dat)
            r = h.formheader1(c, r)
            r = h.formheader2(c, r)

    """
        Add totals together
    """
    gtotmc += gtotmc1 + gtotmc3 + gtotmc5 + gtotmcman
    gtotlc += gtotlc1 + gtotlc3 + gtotlc5 + gtotlcman
    gtotloc += gtotloc1 + gtotloc3 + gtotloc5 + gtotlocman
    gtot += gtot1 + gtot3 + gtot5 + gtotman
    classctot += classctotmc + classctotmoc + classctotlc + classctotloc

    """
        Last Page Totals
    """
    c.showPage()
    r = h.header(c, ent_dat)
    r = h.accountheader1(c, r)
    r = h.accountheader2(c, r)
    x = 20
    y = 502

    """
        ROUGH CASTINGS (1) section     
    """
    sql = v.account_codes()
    account_codescurs = conn.cursor()
    account_codescurs.execute(sql, {'prodlinecls1': '1', 'pnlevelcls':'1'})

    for account_codescurs in account_codescurs:
        minvacctcde = account_codescurs[3]
        linvacctcde = account_codescurs[4]
        loinvacctcde = account_codescurs[5]

    c.setFont('Helvetica', 10, leading=None)
    c.drawString(x, y, 'ROUGH CASTINGS (1)')
    c.drawRightString(240, y, minvacctcde)
    c.drawRightString(335, y, "{:>8.2f}".format(gtotmc1))
    c.drawRightString(400, y, linvacctcde)
    c.drawRightString(485, y, "{:>8.2f}".format(gtotlc1))
    c.drawRightString(560, y, loinvacctcde)
    c.drawRightString(640, y, "{:>8.2f}".format(gtotloc1))
    c.drawRightString(725, y, "{:>8.2f}".format(gtot1))
    y = y - 24
    r += 2

    """
        RAW MATERIAL (3) section
    """
    sql = v.account_codes()
    account_codescurs = conn.cursor()
    account_codescurs.execute(sql, {'prodlinecls1': '1', 'pnlevelcls': '3'})

    for account_codescurs in account_codescurs:
        minvacctcde = account_codescurs[3]
        linvacctcde = account_codescurs[4]
        loinvacctcde = account_codescurs[5]

    c.setFont('Helvetica', 10, leading=None)
    c.drawString(x, y, 'RAW MATERIAL (3)')
    c.drawRightString(240, y, minvacctcde)
    c.drawRightString(335, y, "{:>8.2f}".format(gtotmc3))
    c.drawRightString(400, y, linvacctcde)
    c.drawRightString(485, y, "{:>8.2f}".format(gtotlc3))
    c.drawRightString(560, y, loinvacctcde)
    c.drawRightString(640, y, "{:>8.2f}".format(gtotloc3))
    c.drawRightString(725, y, "{:>8.2f}".format(gtot3))
    y = y - 24
    r += 2

    """
        PURCHASED PARTS (5) section
    """
    sql = v.account_codes()
    account_codescurs = conn.cursor()
    account_codescurs.execute(sql, {'prodlinecls1': '1', 'pnlevelcls': '5'})

    for account_codescurs in account_codescurs:
        minvacctcde = account_codescurs[3]
        linvacctcde = account_codescurs[4]
        loinvacctcde = account_codescurs[5]

    c.setFont('Helvetica', 10, leading=None)
    c.drawString(x, y, 'PURCHASED PARTS (5)')
    c.drawRightString(240, y, minvacctcde)
    c.drawRightString(335, y, "{:>8.2f}".format(gtotmc5))
    c.drawRightString(400, y, linvacctcde)
    c.drawRightString(485, y, "{:>8.2f}".format(gtotlc5))
    c.drawRightString(560, y, loinvacctcde)
    c.drawRightString(640, y, "{:>8.2f}".format(gtotloc5))
    c.drawRightString(725, y, "{:>8.2f}".format(gtot5))
    y = y - 24
    r += 2

    """
        MANUFACTURED PARTS section
    """
    sql = v.account_codes()
    account_codescurs = conn.cursor()
    account_codescurs.execute(sql, {'prodlinecls1': '1', 'pnlevelcls': '4'})

    for account_codescurs in account_codescurs:
        minvacctcde = account_codescurs[3]
        linvacctcde = account_codescurs[4]
        loinvacctcde = account_codescurs[5]

    c.setFont('Helvetica', 10, leading=None)
    c.drawString(x, y, 'MANUFACTURED PARTS')
    c.drawRightString(240, y, minvacctcde)
    c.drawRightString(335, y, "{:>8.2f}".format(gtotmcman))
    c.drawRightString(400, y, linvacctcde)
    c.drawRightString(485, y, "{:>8.2f}".format(gtotlcman))
    c.drawRightString(560, y, loinvacctcde)
    c.drawRightString(640, y, "{:>8.2f}".format(gtotlocman))
    c.drawRightString(725, y, "{:>8.2f}".format(gtotman))
    y = y - 24
    r += 2

    c.drawString(262 + 9, y + 22, 12 * '_')
    c.drawString(410 + 9, y + 22, 12 * '_')
    c.drawString(565 + 9, y + 22, 12 * '_')
    c.drawString(650 + 9, y + 22, 12 * '_')

    """
        GRAND TOTAL section
    """
    sql = v.account_codes()
    account_codescurs = conn.cursor()
    account_codescurs.execute(sql, {'prodlinecls1': '1', 'pnlevelcls': '5'})

    for account_codescurs in account_codescurs:
        mwipacctcde = account_codescurs[0]
        lwipacctcde = account_codescurs[1]
        lowipacctcde = account_codescurs[2]

    c.setFont('Helvetica', 10, leading=None)
    c.drawString(100, y, 'GRAND TOTAL')
    c.drawRightString(240, y, mwipacctcde)
    c.drawRightString(335, y, "{:>8.2f}".format(gtotmc))
    c.drawRightString(400, y, lwipacctcde)
    c.drawRightString(485, y, "{:>8.2f}".format(gtotlc))
    c.drawRightString(560, y, lowipacctcde)
    c.drawRightString(640, y, "{:>8.2f}".format(gtotloc))
    c.drawRightString(725, y, "{:>8.2f}".format(gtot))
    y = y - 24
    r += 2

    """
        CLASS C PARTS section
        classctot += classctotmc + classctotmoc + classctotlc + classctotloc
    """
    c.setFont('Helvetica', 10, leading=None)
    c.drawRightString(420, y, 'MATL OVHD')
    y = y - 12
    c.drawString(20, y, 'TOTAL FOR CLASS C PARTS')
    c.drawRightString(335, y, "{:>8.2f}".format(classctotmc))
    c.drawRightString(410, y, "{:>8.2f}".format(classctotmoc))
    c.drawRightString(485, y, "{:>8.2f}".format(classctotlc))
    c.drawRightString(640, y, "{:>8.2f}".format(classctotloc))
    c.drawRightString(725, y, "{:>8.2f}".format(classctot))
    y = y - 36
    r += 3

    """
        MATERIAL OVERHEAD section
    """
    c.setFont('Helvetica', 10, leading=None)
    c.drawString(50, y, 'VALVE RAW CASTINGS--MATERIAL OVERHEAD')
    c.drawString(330, y, '13015')
    c.drawRightString(450, y, "{:>8.2f}".format(vrc))
    y = y - 12
    r += 1

    c.drawString(50, y, 'VALVE BAR STOCK - MATERIAL OVERHEAD')
    c.drawString(330, y, '13016')
    c.drawRightString(450, y, "{:>8.2f}".format(vbs))
    y = y - 12
    r += 1

    c.drawString(50, y, 'VALVE PURCHASED PARTS--MATERIAL OVERHEAD')
    c.drawString(330, y, '13017')
    c.drawRightString(450, y, "{:>8.2f}".format(vpp))
    y = y - 12
    r += 1

    c.drawString(50, y, 'VALVE MANUFACTURED PARTS--MATERIAL OVERHEAD')
    c.drawString(330, y, '13025')
    c.drawRightString(450, y, "{:>8.2f}".format(vmp))
    y = y - 24
    r += 2

    c.drawString(50, y, 'VALVE ASSEMBLY WIP--MATERIAL OVERHEAD')
    c.drawString(330, y, '13045')
    c.drawRightString(450, y, "{:>8.2f}".format(gtotv))

    c.save()
    # End of Main


if __name__ == "__main__":
    today = datetime.now().strftime('%d-%b-%y').upper()
    todaytime = datetime.now().strftime('%d-%b-%y_%H%M%S%f').upper()
    print('Valve Assembly Work in Proccess Report')
    print(today)
    oc = OracleConnection()
    # file variables creation
    filename = 'E:\DocsAndLogs\\valv_assy_wip_' + todaytime + '.log'
    pdffilename = 'E:\DocsAndLogs\\valv_assy_wip__' + todaytime + '.pdf'
    conn = oc.connect(filename)
    main()
    sys.exit()
