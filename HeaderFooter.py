class HeaderFooter(object):
    """description of class"""

    """
        Add Header, Sub Headers and Footers
        to the pdf report file per new Page   
    """
    def __init__(self):
        print('Initiating Header and Footer.')

    @staticmethod
    def header(c, ent_dat):
        c.setFont('Helvetica-Bold', 11, leading=None)
        c.drawCentredString(400, 600, 'CASHCO INCORPORATED')
        c.drawCentredString(400, 588, 'ELLSWORTH, KANSAS')
        c.drawCentredString(400, 576, 'RELIEVED CUSTOMER ORDER FOR ' + ent_dat)
        c.drawCentredString(400, 564, '')
        r = 5
        return r

    @staticmethod
    def formheader1(c, r):
        fill = "*"*25
        c.setFont('Helvetica', 10, leading=None)
        c.drawString(20, 538, 'ORDER')
        c.drawRightString(250, 538, 'QUANTITY')
        c.drawCentredString(400, 538, fill + ' TOTAL ' + fill)
        r = r + 1
        return r

    @staticmethod
    def formheader2(c, r):
        c.setFont('Helvetica', 10, leading=None)
        c.drawString(20, 526, 'NUMBER')
        c.drawString(90, 526, 'PART NUMBER')
        c.drawRightString(250, 526, 'RELIEVED')
        c.drawRightString(335, 526, 'MATERIAL')
        c.drawRightString(420, 526, 'MATL OVHD')
        c.drawRightString(515, 526, 'LABOR')
        c.drawRightString(590, 526, 'OVERHEAD')
        c.drawRightString(665, 526, 'TOTAL')
        r = r + 1
        return r

    @staticmethod
    def accountheader1(c, r):
        c.setFont('Helvetica', 10, leading=None)
        c.drawRightString(240, 538, 'ACCOUNT')
        c.drawRightString(400, 538, 'ACCOUNT')
        c.drawRightString(560, 538,' ACCOUNT ')
        r = r + 1
        return r

    @staticmethod
    def accountheader2(c, r):
        c.setFont('Helvetica', 10, leading=None)
        c.drawRightString(240, 526, 'NUMBER')
        c.drawRightString(335, 526, 'MATERIAL')
        c.drawRightString(400, 526, 'NUMBER')
        c.drawRightString(485, 526, 'LABOR')
        c.drawRightString(560, 526, 'NUMBER')
        c.drawRightString(640, 526, 'OVERHEAD')
        c.drawRightString(725, 526, 'TOTAL')
        r = r + 1
        return r
