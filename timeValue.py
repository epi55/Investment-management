# Time Value Money (TVM)
# "Compound interest" ("interest on interest") is important to TVM
# Present Value (PV) and Future Value (FV)
# Measuring PV and FV will help compare investment alternatives
# DICTIONARY
# N = Number of compounding periods
# I/Y = Interest rate per compounding period
# PV = Present value
# FV = Future value
# PMT = Annuity payments, or constant periodic cash flow

# Effective annual rate (EAR)
def effectiveAnnualRate():

    annual_rate = float(input("What is the annual rate? Use decimals for percent. "))
    m = int(input("# of compounding periods per year? "))
    y = int(input("# of years invested at this rate? "))
    periodic_rate = (annual_rate / m)
    ear = (1 + periodic_rate) ** (m * y) - 1
    print(round(float(ear), 2))

    amount_invested = float(input("What is the amount invested at stated rate and timeline? "))
    eay = amount_invested * (1 + ear)
    print(round(float(eay), 2))
    # Effective annual yield (EAY)

def futureValue(presentValue, iy, n):
    # FV = PV(1 + I/Y)^N
    ## IY = rate of return per compounding period
    ## N = total number of compounding periods
    futureValue = presentValue * (1 + iy)**n
    print("Future value: {}.".format(futureValue))

#RUN
effectiveAnnualRate()
futureValue(200, 0.10, 2)