class ValvAssyWipCursors(object):
    """description of class"""

    def __init__(self):
        print('Initiating Sql')

    @staticmethod
    def curs1():
        return """SELECT DISTINCT TRANS_CDE concde
                      FROM PARTACTIVITY
                      WHERE TRANSTYPE_CLS = '4' AND
                            PRODLINE_CLS IN ('1','3','4','5','7') AND 
                            ENT_DAT = :actdat
                      ORDER BY TRANS_CDE"""

    @staticmethod
    def curs2():
        return """SELECT A.PN_CDE partactivity_pn_cde,
                         ACT_QTY actqty,
                         A.PRODLINE_CLS prodline,
                         A.STDMC_DOL tmc,
                         A.STDLC_DOL tlc,
                         NVL(INV_CLS,'X') inv_cls,
                         NVL(INV_LEVEL_CLS,'0') pnlevel,
                         A.STDMOC_DOL stdmoc_dol, 
                         A.STDLOC_DOL stdloc_dol
                    FROM PARTACTIVITY A,IMF B
                    WHERE TRANS_CDE = :concde AND A.ENT_DAT = :actdat AND 
                          TRANSTYPE_CLS = '4' AND 
                          B.PN_CDE(+) = A.PN_CDE
                    ORDER BY INV_LEVEL_CLS,A.PN_CDE"""

    @staticmethod
    def valvovhd_pct():
        return """SELECT TO_CHAR(VALVOVHD_PCT/100) valvovhdpct FROM CONTROLFILE"""

    @staticmethod
    def account_codes():
        return """SELECT MASSACCT_CDE massacctcde,
                         NVL(LASSACCT_CDE,'     ') lassacctcde,
                         NVL(LOASSACCT_CDE,'     ') loassacctcde,
                         MINVACCT_CDE minvacctcde,
                         NVL(LINVACCT_CDE,'     ') linvacctcde,
                         NVL(LOINVACCT_CDE,'     ') loinvacctcde
                    FROM INVACCT
                    WHERE PRODLINE_CLS = :prodlinecls1 AND
                    INV_LEVEL_CLS = :pnlevelcls"""
