import MetaTrader5 as mt5
import pandas as pd

if not mt5.initialize():
    print("initialize() failed")
    mt5.shutdown()

##
# MT5 não traz nenhuma forma de filtrar 
# Papeis que estão nessa lista são os que travam no método copy_rates_from por não ter nenhum dado
# Não retorna erro
# ##
listaPapeisExcluidos = ("!ALEF3B,!APTI3,!APTI3,!ATCR11,!BAUH3,!BBAS11,!BBAS12,!BDRX11,!BETP3B,!BMII11,!CABI3B,!CACO3B,!CATA3,!CATA*,!CEEB*,!CMSA*,!COCE*,!CORR*,!CRTE*," +
                       '!DTCY*,!ESUD*,!ESUT*,!ESUU*,!FNCN*,!FRRN*,!HBTS*,!HOOT*,!IBRA*,!IBXX*,!ICO*,!IDIV*,!IEEX*,!IFIX*,!IFNC*,!IGC*,!IGNM*,!IMAT*,!IMOB*,!INDX*,!ISEE*,' +
                       '!ITAG*,!IVBX*,!IVPR*,!LTEL*,!MCRJ*,!MGEL*,!MLCX*,!MMAQ*,!MNZC*,!NEMO*,!NRTQ*,!ODER*,!OPEQ*,!OPGM*,!OPH*,!OPSE*,!OPTS*,!PINE*,!PPAR*,!PRMN*,!PRPT*,' +
                       '!QUSW*,!QVQP*,!RSUL*,!SFND*,!SMLL*,!TAXA*,!TKNO*,!UPKP*,!UTIL*,!VLJS*,!VPSI*,!VSPT*,!FINF*,!BRHT*,!PMSP*,!MSRO*,!STKF*,!TF*,!BRQB*,!CNSY*,!CTCA*,' +
                       '!LUPA*,!PLAS*,!PLPF*,!UNAG*,!IFIL*,!PCAR*,!*32,!*33,!*34,!*35,!*36,!*37,!*38,!*39,*3,*4, BPAC*, !KLAS3, !TEGA3,!LLBI3,!PASS3')

symbols = mt5.symbols_get(group=listaPapeisExcluidos)
arrayAVista = []
#Mais alguns filtros para remover tickers
for s in symbols:
    if ("BOVESPA\\A VISTA\\" in s.path and 'Deprecated' not in s.path and 'USD' not in s.currency_base and 'FII ' not in s.description and ' MA' not in s.description 
        and ' M2' not in s.description and ' MB' not in s.description):
        arrayAVista.append(s.name)

dfFinal = pd.DataFrame(arrayAVista, columns=["ticker"])
dfFinal.to_excel('./bovespa/bovespastocks.xlsx')

# concluímos a conexão ao terminal MetaTrader 5
mt5.shutdown()