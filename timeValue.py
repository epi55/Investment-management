# DICTIONARY
# N = Number of compounding periods
# I/Y = Interest rate per compounding period
# PMT = Annuity payments, or constant periodic cash flow

# EFFECTIVE ANNUAL RATE (EAR)
# https://www.investopedia.com/terms/e/effectiveinterest.asp
def effectiveAnnualRate(ar, cp, years, pr):
    # Periodic rate (pr) = nominal interest rate / number of periods
    # Number of periods = compounding periods per year * number of years
    # ear = (1 + periodic rate) ** (number of periods) - 1
    ear = (1 + pr) ** (cp * years) - 1
    print("Effective annual rate: {}.".format(round(float(ear), 2)))
    return(round(float(ear), 2))

# EFFECTIVE ANNUAL YIELD (EAY)
def effectiveAnnualRate(ear):
    # ALGORITHM
    eay = ai * (1 + ear)
    print("Effective annual yield: {}.".format(round(float(eay), 2)))
    return(eay)

# FUTURE VALUE (FV)
def futureValue(pv, iy, n):
    # fv = pv(1 + i/y)^N
    futureValue = presentValue * (1 + iy) ** n
    print("Future value: {}.".format(futureValue))

# RUN
# (1) annual rate, (2) compounding periods, (3) years, (4) periodic rate, (5) amount invested
effectiveAnnualRate(ar, cp, years, pr, ai)

#
effectiveAnnualYield(effectiveAnnualRate(ar, cp, years, pr, ai))

# (1) present value, (2) rate of return per compounding period, (3) total number of compounding periods
futureValue(pv, iy, n)